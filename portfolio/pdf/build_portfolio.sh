#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PORTFOLIO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HTML_PATH="${PORTFOLIO_DIR}/portfolio.html"
PDF_PATH="${PORTFOLIO_DIR}/Yoon_Youngju_Backend_Portfolio.pdf"

pandoc "${PORTFOLIO_DIR}/PORTFOLIO.md" \
  --from=markdown+fenced_divs+pipe_tables+raw_html+link_attributes \
  --to=html5 \
  --standalone \
  --metadata pagetitle="윤영주 Backend Portfolio" \
  --css="pdf/portfolio.css" \
  --output="${HTML_PATH}"

node "${SCRIPT_DIR}/render_pdf.js" "${HTML_PATH}" "${PDF_PATH}"

pdfinfo "${PDF_PATH}" | grep -E '^(Pages|Page size|File size):'
