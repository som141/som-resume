#!/usr/bin/env python3
"""Render the three high-level architecture diagrams with a fixed, readable layout."""

from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parent
INK = "#252a30"
MUTED = "#626970"
LINE = "#8a9299"
SOFT = "#f6f3ee"
ORANGE = "#a6502b"
PURPLE = "#5965a8"
TEAL = "#347683"
GREEN = "#55795a"
BLUE = "#536c87"
BROWN = "#80675c"


def icon(kind: str, cx: float, cy: float, color: str) -> str:
    common = f'fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"'
    if kind == "user":
        shape = f'<circle cx="{cx}" cy="{cy-6}" r="7" {common}/><path d="M {cx-13} {cy+13} Q {cx} {cy+1} {cx+13} {cy+13}" {common}/>'
    elif kind == "gateway":
        shape = f'<path d="M {cx-14} {cy-9} H {cx+5} M {cx+5} {cy-9} l -6 -6 M {cx+5} {cy-9} l -6 6 M {cx+14} {cy+9} H {cx-5} M {cx-5} {cy+9} l 6 -6 M {cx-5} {cy+9} l 6 6" {common}/>'
    elif kind == "queue":
        shape = f'<rect x="{cx-14}" y="{cy-12}" width="28" height="24" rx="3" {common}/><path d="M {cx-9} {cy-5} H {cx+8} M {cx-9} {cy+1} H {cx+8} M {cx-9} {cy+7} H {cx+3}" {common}/>'
    elif kind == "audio":
        shape = f'<path d="M {cx-14} {cy+2} V {cy-2} A 14 14 0 0 1 {cx+14} {cy-2} V {cy+2}" {common}/><rect x="{cx-16}" y="{cy}" width="6" height="13" rx="2" {common}/><rect x="{cx+10}" y="{cy}" width="6" height="13" rx="2" {common}/>'
    elif kind == "stock":
        shape = f'<path d="M {cx-15} {cy+12} H {cx+16} M {cx-12} {cy+7} l 8 -8 7 5 11 -15" {common}/><path d="M {cx+8} {cy-11} H {cx+14} V {cy-5}" {common}/>'
    elif kind == "database":
        shape = f'<ellipse cx="{cx}" cy="{cy-10}" rx="15" ry="6" {common}/><path d="M {cx-15} {cy-10} V {cy+10} M {cx+15} {cy-10} V {cy+10} M {cx-15} {cy} C {cx-8} {cy+7},{cx+8} {cy+7},{cx+15} {cy} M {cx-15} {cy+10} C {cx-8} {cy+17},{cx+8} {cy+17},{cx+15} {cy+10}" {common}/>'
    elif kind == "web":
        shape = f'<rect x="{cx-16}" y="{cy-12}" width="32" height="24" rx="3" {common}/><path d="M {cx-16} {cy-5} H {cx+16} M {cx-11} {cy-9} h 1 M {cx-6} {cy-9} h 1" {common}/>'
    elif kind == "worker":
        shape = f'<circle cx="{cx}" cy="{cy}" r="7" {common}/><path d="M {cx} {cy-15} V {cy-10} M {cx} {cy+10} V {cy+15} M {cx-15} {cy} H {cx-10} M {cx+10} {cy} H {cx+15} M {cx-11} {cy-11} l 4 4 M {cx+7} {cy+7} l 4 4 M {cx+11} {cy-11} l -4 4 M {cx-7} {cy+7} l -4 4" {common}/>'
    elif kind == "model":
        shape = f'<path d="M {cx-13} {cy-10} H {cx+13} V {cy+10} H {cx-13} Z M {cx-6} {cy-3} l -5 3 5 3 M {cx+6} {cy-3} l 5 3 -5 3 M {cx+2} {cy-6} l -4 12" {common}/>'
    elif kind == "book":
        shape = f'<path d="M {cx} {cy-10} C {cx-7} {cy-15},{cx-14} {cy-12},{cx-14} {cy-6} V {cy+11} C {cx-7} {cy+7},{cx-3} {cy+8},{cx} {cy+12} M {cx} {cy-10} C {cx+7} {cy-15},{cx+14} {cy-12},{cx+14} {cy-6} V {cy+11} C {cx+7} {cy+7},{cx+3} {cy+8},{cx} {cy+12} Z" {common}/>'
    elif kind == "quiz":
        shape = f'<circle cx="{cx}" cy="{cy}" r="15" {common}/><path d="M {cx-5} {cy-5} Q {cx-3} {cy-12},{cx+4} {cy-9} Q {cx+10} {cy-5},{cx+2} {cy} V {cy+4} M {cx+2} {cy+10} h .1" {common}/>'
    else:
        shape = f'<circle cx="{cx}" cy="{cy}" r="14" {common}/>'
    return shape


def card(x: int, y: int, w: int, h: int, title: str, sub: str, kind: str, color: str) -> str:
    lines = sub.split("\n") if sub else []
    text = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#ffffff" stroke="#c8ccd0" stroke-width="2"/>',
        f'<rect x="{x}" y="{y}" width="7" height="{h}" rx="3.5" fill="{color}"/>',
        f'<circle cx="{x+38}" cy="{y+38}" r="24" fill="{color}" opacity="0.12"/>',
        icon(kind, x + 38, y + 38, color),
        f'<text x="{x+72}" y="{y+31}" class="title">{escape(title)}</text>',
    ]
    for index, line in enumerate(lines):
        text.append(f'<text x="{x+72}" y="{y+53+index*19}" class="sub">{escape(line)}</text>')
    return "".join(text)


def band(
    x: int,
    y: int,
    w: int,
    title: str,
    columns: list[tuple[str, str]],
    label_width: int = 150,
) -> str:
    column_w = (w - label_width) / len(columns)
    out = [
        f'<rect x="{x}" y="{y}" width="{w}" height="88" rx="12" fill="{SOFT}" stroke="#d2cec7" stroke-width="2"/>',
        f'<circle cx="{x+38}" cy="{y+44}" r="24" fill="{BLUE}" opacity="0.12"/>',
        icon("database", x + 38, y + 41, BLUE),
        f'<text x="{x+70}" y="{y+39}" class="title">{escape(title)}</text>',
        f'<text x="{x+70}" y="{y+61}" class="tiny">STATE / DATA</text>',
    ]
    start = x + label_width
    for i, (head, detail) in enumerate(columns):
        cx = start + i * column_w
        if i:
            out.append(f'<line x1="{cx}" y1="{y+17}" x2="{cx}" y2="{y+71}" stroke="#d4d0ca" stroke-width="1.5"/>')
        out.append(f'<text x="{cx+18}" y="{y+35}" class="band-head">{escape(head)}</text>')
        out.append(f'<text x="{cx+18}" y="{y+58}" class="sub">{escape(detail)}</text>')
    return "".join(out)


def arrow(x1: int, y1: int, x2: int, y2: int, label: str = "", dashed: bool = False, both: bool = False) -> str:
    dash = ' stroke-dasharray="8 6"' if dashed else ""
    start = ' marker-start="url(#arrowBack)"' if both else ""
    midx, midy = (x1 + x2) / 2, (y1 + y2) / 2 - 9
    out = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{LINE}" stroke-width="2.2" marker-end="url(#arrow)"{start}{dash}/>'
    if label:
        width = max(58, len(label) * 9)
        out += f'<rect x="{midx-width/2}" y="{midy-13}" width="{width}" height="21" rx="10" fill="#ffffff"/><text x="{midx}" y="{midy+2}" class="label">{escape(label)}</text>'
    return out


def base(body: str, height: int = 500) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}">
<defs>
  <marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="{LINE}"/></marker>
  <marker id="arrowBack" markerWidth="9" markerHeight="9" refX="1" refY="4.5" orient="auto"><path d="M9,0 L0,4.5 L9,9 Z" fill="{LINE}"/></marker>
  <style>
    text {{ font-family: "Noto Sans CJK KR", "Noto Sans KR", sans-serif; fill: {INK}; }}
    .title {{ font-size: 21px; font-weight: 700; }}
    .sub {{ font-size: 15px; fill: {MUTED}; }}
    .tiny {{ font-size: 11px; font-weight: 700; letter-spacing: 1.4px; fill: {MUTED}; }}
    .band-head {{ font-size: 16px; font-weight: 700; }}
    .label {{ font-size: 13px; font-weight: 650; text-anchor: middle; fill: {MUTED}; }}
  </style>
</defs>{body}</svg>'''


def dis() -> str:
    body = [
        card(25, 125, 175, 105, "Discord", "명령 · 응답", "user", PURPLE),
        card(245, 125, 205, 105, "Gateway", "입력 검사 · defer\n응답 위치 저장", "gateway", ORANGE),
        card(500, 125, 180, 105, "RabbitMQ", "command / result", "queue", BROWN),
        card(740, 35, 205, 105, "Audio Node", "player · queue\n음성 송신", "audio", TEAL),
        card(740, 225, 205, 105, "Stock Node", "시세 · 거래\n시즌 · 순위", "stock", GREEN),
        card(990, 35, 185, 105, "음원 경계", "YouTube · cipher\nDiscord Voice", "web", TEAL),
        card(990, 225, 185, 105, "시장·거래 DB", "Finnhub\nPostgreSQL", "database", GREEN),
        arrow(200, 177, 245, 177, "명령 / 응답", both=True),
        arrow(450, 177, 500, 177, "저장 후 발행"),
        arrow(680, 160, 740, 87, "음악 ↔ 결과", both=True),
        arrow(680, 195, 740, 277, "주식 ↔ 결과", both=True),
        arrow(945, 87, 990, 87),
        arrow(945, 277, 990, 277),
        band(245, 385, 700, "Redis", [("Gateway", "pending 응답"), ("Audio", "음악 상태 · lock"), ("Stock", "시세 · 랭킹 캐시")]),
    ]
    return base("".join(body))


def lawground() -> str:
    body = [
        card(25, 115, 175, 105, "Web 사용자", "로그인 · 문제 관리\n분석 상태 조회", "user", PURPLE),
        card(245, 115, 210, 105, "Spring API", "소유권 · CRUD\nrun 접수 · 결과 공개", "web", ORANGE),
        card(505, 115, 175, 105, "RabbitMQ", "작업 신호", "queue", BROWN),
        card(730, 115, 205, 105, "Job Worker", "lease · fencing\ncheckpoint · 재시도", "worker", TEAL),
        card(985, 115, 190, 105, "Python AI", "embed · rerank\nverify HTTP 계약", "model", GREEN),
        arrow(200, 167, 245, 167, "HTTP", both=True),
        arrow(455, 167, 505, 167, "run 저장 후 발행"),
        arrow(680, 167, 730, 167, "claim"),
        arrow(935, 167, 985, 167, "계산 요청 / 응답", both=True),
        band(245, 315, 690, "PostgreSQL", [("API DATA", "회원 · 문제 · 선지"), ("JOB STATE", "run · lease · checkpoint"), ("SEARCH / PGVECTOR", "법령 · FTS · vector")], label_width=190),
        '<line x1="350" y1="220" x2="350" y2="315" stroke="#b1b6bb" stroke-width="1.8" stroke-dasharray="6 5"/>',
        '<line x1="833" y1="220" x2="833" y2="315" stroke="#b1b6bb" stroke-width="1.8" stroke-dasharray="6 5"/>',
    ]
    return base("".join(body), 430)


def verbly() -> str:
    body = [
        card(25, 115, 175, 105, "학습자", "첨삭 확인 · 복습", "user", PURPLE),
        card(245, 115, 190, 105, "Spring API", "인증 · 소유권\n요청 검증", "web", ORANGE),
        card(480, 115, 205, 105, "Correction", "교정 문장 · 원문\n자동 채우기 출처", "book", BLUE),
        card(730, 115, 205, 105, "Library", "표현 · 뜻 · 예문\n교정 / 게시글 출처", "book", TEAL),
        card(980, 115, 195, 105, "Quiz Review", "session · 문제\n답안 · 오답 재도전", "quiz", GREEN),
        arrow(200, 167, 245, 167, "HTTP", both=True),
        arrow(435, 167, 480, 167, "소유권 확인"),
        arrow(685, 167, 730, 167, "autofill"),
        arrow(935, 167, 980, 167, "출제"),
        band(245, 315, 930, "MySQL", [("CORRECTION", "첨삭 결과"), ("LIBRARY", "item · example · source"), ("REVIEW", "task · question · answer")]),
        '<line x1="582" y1="220" x2="582" y2="315" stroke="#b1b6bb" stroke-width="1.8" stroke-dasharray="6 5"/>',
        '<line x1="832" y1="220" x2="832" y2="315" stroke="#b1b6bb" stroke-width="1.8" stroke-dasharray="6 5"/>',
        '<line x1="1077" y1="220" x2="1077" y2="315" stroke="#b1b6bb" stroke-width="1.8" stroke-dasharray="6 5"/>',
    ]
    return base("".join(body), 430)


for name, content in {
    "dis-system.svg": dis(),
    "lawground-system.svg": lawground(),
    "verbly-system.svg": verbly(),
}.items():
    (ROOT / name).write_text(content, encoding="utf-8")
