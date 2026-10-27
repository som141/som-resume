# 개인 학습 저장소 공개 전환

2026-10-27 확인 기준입니다. **공개 전환은 아직 완료되지 않았습니다.** 연결된 GitHub 인증으로 저장소 설정 변경을 요청했지만 `403 Resource not accessible by integration`이 반환됐습니다. 소유자 계정의 저장소 설정 권한이 필요합니다. 코드 수정·문서 반영과 저장소 공개 범위 변경은 별도 권한입니다.

## 이력서와 연결되는 공개 대상

| 저장소 | 내용 | 공개 설정 |
| --- | --- | --- |
| [bj.cpp](https://github.com/som141/bj.cpp) | C/C++ 자료구조·알고리즘 연습 | [Settings](https://github.com/som141/bj.cpp/settings#danger-zone) |
| [ex-2](https://github.com/som141/ex-2) | Spring 의존성 주입·빈·생명주기 실습 | [Settings](https://github.com/som141/ex-2/settings#danger-zone) |
| [sv1](https://github.com/som141/sv1) | Servlet·프런트 컨트롤러 실습 | [Settings](https://github.com/som141/sv1/settings#danger-zone) |
| [sp1](https://github.com/som141/sp1) | Spring MVC 요청·응답 실습 | [Settings](https://github.com/som141/sp1/settings#danger-zone) |
| [SecondWeb](https://github.com/som141/SecondWeb) | 상품 등록·조회·수정 예제 | [Settings](https://github.com/som141/SecondWeb/settings#danger-zone) |
| [bookstore-query-lab](https://github.com/som141/bookstore-query-lab) | JPA·PostgreSQL 실습 환경 구성 | [Settings](https://github.com/som141/bookstore-query-lab/settings#danger-zone) |

각 Settings의 **Danger Zone → Change repository visibility → Change to public**에서 진행합니다. 공개 후에는 로그인하지 않은 브라우저에서 저장소 링크가 열리는지 확인하면 됩니다.

다음 저장소도 학습·환경 연습용으로 분류했습니다. 내용이 짧거나 기본 코드·컴파일 결과물 위주이므로 이력서의 주요 이력에는 넣지 않았습니다.

- [sS](https://github.com/som141/sS): 회원·주문 예제, 다른 Spring 실습과 중복
- [spring-practice](https://github.com/som141/spring-practice): 범위가 좁고 미완성 부분이 있는 빈 스코프 예제
- [OrderService](https://github.com/som141/OrderService): 초기 Spring 기본 코드
- [UMC](https://github.com/som141/UMC): 초기 개발 환경 파일
- [wslTest](https://github.com/som141/wslTest): C·WSL 환경 확인
- [som-s_toe](https://github.com/som141/som-s_toe): 현재는 컴파일 결과물만 있고 소스는 과거 이력에 남은 Swing 예제

## 공개 전 확인한 범위

위 12개와 아래 `lab3`를 합한 작은 비공개 저장소 13개의 전체 브랜치·태그 Git 이력을 Gitleaks 8.30.1 기본 규칙으로 검사했습니다. 저장소 자체의 예외 규칙과 인라인 검사 제외를 적용하지 않았으며, 탐지 결과는 0건이었습니다. 설정의 인증 관련 항목은 환경변수 참조나 로컬 예제 값인지 추가로 구분했습니다. 파일 구성도 확인했으며, 자동 탐지 결과를 모든 파일의 공개 적합성 보장으로 해석하지 않았습니다.

## 비공개 유지 대상

- **`-pdf`:** 강의 슬라이드·교재·과제와 개인 노트가 섞인 자료 모음입니다. 일부 파일명에는 학적 식별 정보도 있습니다. 전체 공개 대상에서 제외했으며, 개인 노트에서 확인한 학습 내용만 요약했습니다.
- **`lab3`:** 원본 작성자가 다른 강의 과제 안내 PDF가 Git 이력에 있습니다. 재배포 허용이 확인되지 않아 공개하지 않았습니다.
- 빈 저장소·단순 텍스트 저장소와 학습용으로 확인되지 않은 별도 앱은 공개 대상을 넓혀 포함하지 않았습니다.

공개 범위를 바꾸기 위해 과거 커밋을 삭제하거나 다시 쓰지는 않았습니다.
