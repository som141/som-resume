const { chromium } = require("playwright-core");
const http = require("node:http");
const fs = require("node:fs/promises");
const path = require("node:path");

const MIME_TYPES = {
  ".css": "text/css; charset=utf-8",
  ".html": "text/html; charset=utf-8",
  ".png": "image/png",
  ".svg": "image/svg+xml",
};

async function startStaticServer(rootDir) {
  const root = path.resolve(rootDir);
  const server = http.createServer(async (request, response) => {
    try {
      const pathname = decodeURIComponent(new URL(request.url, "http://localhost").pathname);
      const relative = pathname === "/" ? "portfolio.html" : pathname.slice(1);
      const filePath = path.resolve(root, relative);
      if (!filePath.startsWith(`${root}${path.sep}`) && filePath !== root) {
        response.writeHead(403).end();
        return;
      }
      const content = await fs.readFile(filePath);
      response.writeHead(200, { "Content-Type": MIME_TYPES[path.extname(filePath)] || "application/octet-stream" });
      response.end(content);
    } catch {
      response.writeHead(404).end();
    }
  });

  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  return server;
}

async function main() {
  const [, , htmlPath, pdfPath] = process.argv;
  if (!htmlPath || !pdfPath) {
    throw new Error("Usage: node render_pdf.js <html> <pdf>");
  }

  const server = await startStaticServer(path.dirname(htmlPath));
  const { port } = server.address();
  const browser = await chromium.launch({
    headless: true,
    executablePath: process.env.CHROMIUM_PATH || "/usr/bin/chromium",
    args: ["--no-sandbox", "--disable-dev-shm-usage"],
  });

  try {
    const page = await browser.newPage();
    await page.goto(`http://127.0.0.1:${port}/${path.basename(htmlPath)}`, { waitUntil: "load" });
    await page.emulateMedia({ media: "print" });
    await page.evaluate(() => document.fonts.ready);
    const layout = await page.evaluate(() => {
      const brokenImages = [...document.images].filter(img => !img.complete || !img.naturalWidth).map(img => img.getAttribute("src"));
      const overflow = [...document.querySelectorAll(".page")].flatMap((sheet, index) => {
        const box = sheet.getBoundingClientRect();
        const style = getComputedStyle(sheet);
        const bottom = box.bottom - parseFloat(style.paddingBottom);
        const right = box.right - parseFloat(style.paddingRight);
        const elements = [...sheet.querySelectorAll("h1,h2,h3,p,table,pre,ul,ol,figure,img")];
        const failures = elements.filter(el => {
          if (el.closest(".cover-meta")) return false; // Cover footer is intentionally positioned in the bottom margin.
          const rect = el.getBoundingClientRect();
          return rect.bottom > bottom + 1 || rect.right > right + 1;
        });
        return failures.length ? [{ page: index + 1, elements: failures.map(el => el.textContent.slice(0, 70) || el.getAttribute("src")) }] : [];
      });
      return { pages: document.querySelectorAll(".page").length, brokenImages, overflow };
    });
    if (layout.brokenImages.length || layout.overflow.length) {
      throw new Error(`Print layout validation failed: ${JSON.stringify(layout)}`);
    }
    console.log(`Validated ${layout.pages} pages: no missing images or content overflow.`);
    await page.pdf({
      path: pdfPath,
      format: "A4",
      printBackground: true,
      preferCSSPageSize: true,
      margin: { top: "0", right: "0", bottom: "0", left: "0" },
    });
  } finally {
    await browser.close();
    await new Promise((resolve) => server.close(resolve));
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
