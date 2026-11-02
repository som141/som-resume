#!/usr/bin/env python3
"""Create the GitHub-readable portfolio from the print layout source."""

from pathlib import Path
import re
import sys


def export(source: Path, destination: Path) -> None:
    lines: list[str] = []
    page_count = 0
    for line in source.read_text(encoding="utf-8").splitlines():
        if line.startswith("::: {.page"):
            if page_count:
                lines.extend(["", "---", ""])
            page_count += 1
            continue
        if re.fullmatch(r":::(?: \{[^}]+\})?", line):
            continue
        if re.fullmatch(r'<div class="page-no">\d+</div>', line):
            continue

        eyebrow = re.fullmatch(r'<div class="eyebrow">(.+)</div>', line)
        if eyebrow:
            lines.append(f"**{eyebrow.group(1)}**")
            continue

        line = re.sub(r"(\]\([^)]+\))\{[^}]+\}", r"\1", line)
        lines.append(line)

    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    destination.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: export_markdown.py PRINT_SOURCE OUTPUT")
    export(Path(sys.argv[1]), Path(sys.argv[2]))
