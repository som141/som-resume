#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PORTFOLIO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
PRINT_SOURCE="${SCRIPT_DIR}/PORTFOLIO_PRINT.md"
MARKDOWN_PATH="${PORTFOLIO_DIR}/PORTFOLIO.md"
HTML_PATH="${PORTFOLIO_DIR}/portfolio.html"
PDF_PATH="${PORTFOLIO_DIR}/Yoon_Youngju_Backend_Portfolio.pdf"

python3 "${SCRIPT_DIR}/export_markdown.py" "${PRINT_SOURCE}" "${MARKDOWN_PATH}"

pandoc "${PRINT_SOURCE}" \
  --from=markdown+fenced_divs+pipe_tables+raw_html+link_attributes \
  --to=html5 \
  --standalone \
  --metadata pagetitle="윤영주 Backend Portfolio" \
  --css="pdf/portfolio.css" \
  --output="${HTML_PATH}"

node "${SCRIPT_DIR}/render_pdf.js" "${HTML_PATH}" "${PDF_PATH}"

if grep -q '^:::' "${MARKDOWN_PATH}"; then
  echo "Markdown export still contains print-only fenced divs." >&2
  exit 1
fi

PAGE_COUNT="$(pdfinfo "${PDF_PATH}" | awk '/^Pages:/ {print $2}')"
if [[ "${PAGE_COUNT}" != "32" ]]; then
  echo "Expected 32 PDF pages, got ${PAGE_COUNT}." >&2
  exit 1
fi

pdfinfo "${PDF_PATH}" | grep -E '^(Pages|Page size|File size):'
