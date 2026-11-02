#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for source in "${SCRIPT_DIR}"/*.dot; do
  output="${source%.dot}.svg"
  dot -Tsvg "${source}" -o "${output}"
done

echo "Rendered $(find "${SCRIPT_DIR}" -maxdepth 1 -name '*.svg' | wc -l) diagrams."
