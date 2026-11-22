# 포트폴리오 빌드와 검증

본문의 기준은 [PORTFOLIO_PRINT.md](PORTFOLIO_PRINT.md)다. 이력서는 저장소 루트의 [README](../../README.md)를 별도로 편집한다. 생성한 PORTFOLIO.md나 PDF만 수정하지 않는다.

## 산출물

- [PORTFOLIO.md](../PORTFOLIO.md): GitHub에서 읽는 버전. export_markdown.py로 인쇄 전용 표기를 제거한다.
- `portfolio.html`: Pandoc 중간 산출물. 로컬에서 재생성하며 Git 추적 대상은 아니다.
- [PDF](../Yoon_Youngju_Backend_Portfolio.pdf): Chromium으로 인쇄한 A4 문서. 현재 37쪽이다.
- [그림 생성기](../assets/diagrams/build_system_diagrams.py): 전체 시스템 및 DIS 운영 SVG를 재생성한다. DIS 모듈 도식은 Java 모듈 범위이며 Node 경계는 본문·전체 도식에 표시한다.

## 빌드

Python 3, Pandoc, Node.js, Chromium/Chrome, Poppler(pdfinfo)가 필요하다. 먼저 이 디렉터리에서 `npm ci --ignore-scripts`로 playwright-core를 설치한다. 저장소 루트에서 다음을 실행한다.

```bash
CHROMIUM_PATH=/usr/bin/chromium bash portfolio/pdf/build_portfolio.sh
```

`CHROMIUM_PATH`는 로컬 Chrome 실행 파일로 바꿀 수 있다. Linux 기본값은 `/usr/bin/chromium`이다. 빌드는 그림 → Markdown → HTML → PDF 순서로 진행하며, 인쇄 원문의 `.page` 수와 실제 PDF 쪽 수가 일치해야 한다. 쪽을 추가하면 표지·목차·본문의 페이지 참조도 함께 수정한다.

`render_pdf.js`는 이미지 로딩, 글꼴 준비, 본문이 인쇄 영역을 벗어나는지 확인하고 실패하면 PDF 생성을 중단한다. 표지 하단 연락처는 의도적으로 배치한 footer이므로 별도로 확인한다. PDF를 PNG로 렌더해 한글·표·그림·잘림을 눈으로도 검사한다. 검사 통과는 내용의 사실성 검증을 대신하지 않는다.

## 2026-11-22 내용 대조

DIS 구현 기준은 PR #28 병합 커밋 `29ebb0a`다. 메이플은 인증, 검색·감시·복구, PostgreSQL 상태, 장비·세트 계산의 문제·원인·개선·한계를 보강했다. 2026-11-17의 CI 124개 성공은 당시 기록으로만 썼다. 전 직업 실전 딜 정확도, 전 아이템 메타데이터 완전성, 100명 동시 처리, 정확히 한 번 DM 전달은 검증된 성과로 기재하지 않았다.
