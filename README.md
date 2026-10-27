# 윤영주

Java 백엔드 개발자를 지향하는 소프트웨어 전공 학생입니다. 직접 사용하는 Discord 봇을 만들고, 지인들과 사용하며 발견한 문제를 개선하고 있습니다. 팀 프로젝트에서는 사용자별 데이터 관리와 작업 처리, 외부 서비스 연동을 맡았습니다.

![프로필](image.png)

- 연락처:010-8977-9897
- GitHub: [som141](https://github.com/som141)
- 학력: 단국대학교 소프트웨어 전공 · 2023.03 입학

## Skills

| 구분 | 사용 기술 |
| --- | --- |
| 언어 | **Java** · C/C++ · Python · Kotlin |
| 백엔드 | Spring Boot · Spring Data JPA/Hibernate · JDA · LavaPlayer · REST API · gRPC |
| 데이터·메시징 | PostgreSQL · MySQL · MongoDB · Redis · RabbitMQ |
| 개발·배포 | Git · GitHub Actions · Gradle · Docker Compose · Linux/WSL · GCP |
| 테스트 | JUnit |
| 모니터링·로그 | Prometheus · Grafana · Loki · Alloy |

Java와 Spring을 주로 사용합니다. C/C++은 자료구조·알고리즘 실습, Python은 수업 실습, Kotlin은 Android 앱 개발에 사용했습니다.

## Projects

### DIS · Discord 음악·주식 모의투자 봇

개인 프로젝트 · 개발 및 운영 · 개발 기록 2025.06~\
[저장소](https://github.com/som141/dis)

2024년 사용하던 Discord 봇들이 동작하지 않던 경험을 계기로 직접 쓸 음악 봇을 만들었습니다. 음악 검색·재생에 주식 모의투자 기능을 더했고, 현재 지인 약 30명과 사용하고 있습니다.

- **재생 안내만 나오고 소리가 들리지 않는 문제를 해결했습니다.** 서버 로그를 따라 YouTube 인증과 음원 요청 방식을 확인해 재생을 복구했습니다. 요청이 접수된 뒤 발생한 재생 실패도 사용자에게 전달하도록 응답 흐름을 개선했습니다.
- **작업 결과를 요청자에게 돌려주는 순서를 정리했습니다.** 답변할 위치를 먼저 저장하고 작업을 보내도록 바꾸고, 작업이 빠르게 끝나는 경우에도 이 순서가 유지되는지 테스트 코드로 확인했습니다.
- **외부 라이브러리 다운로드 문제로 막힌 빌드·배포를 복구했습니다.** 같은 버전의 공식 배포 파일을 사용하고 파일 검증을 추가했으며, 이후 자동 빌드와 서버 배포 성공을 확인했습니다.

사용 기술: Java · Spring Boot · JDA · LavaPlayer · RabbitMQ · Redis · PostgreSQL · Docker Compose · GitHub Actions

### LawGround · 법령 근거 기반 기출문제 분석

팀 프로젝트 · Spring 백엔드·DB 및 AI 서비스 연동 · 기여 기록 2026.10~\
[저장소](https://github.com/lawground-team/LawGround) · [개인 구현 보고서](https://github.com/lawground-team/LawGround/blob/main/docs/reports/youngju-integrated-week-08.md)

공인중개사 기출문제의 정답 근거를 법령에서 확인하고 관련 문제를 추천하는 서비스입니다.

- Google 로그인과 사용자별 문제 등록·조회·수정·삭제, 개인 라이브러리를 구현했습니다. 다른 사용자의 데이터에 접근하거나 같은 문제를 중복 등록하는 경우를 검사했습니다.
- 오래 걸리는 분석을 작업 큐로 처리하고, 중복 요청·재시도·처리 중 중단에 대응하는 저장 및 재개 흐름을 구현했습니다.
- 법령 검색과 팀원의 AI 분석 API를 연결했습니다. 분석 결과와 인용 근거를 함께 저장하고, 선지별 설명·관련 문제 추천을 화면에서 확인하도록 연결했습니다.

사용 기술: Java · Spring Boot · Spring Data JPA · PostgreSQL/pgvector · RabbitMQ · Docker

### 버블리(Verbly) · 영어 일기 첨삭·복습 서비스

팀 프로젝트 · 개인 라이브러리·복습 퀴즈 백엔드 · 기여 기록 2026.01–2026.02\
[백엔드 저장소](https://github.com/Verbly-Official/BE)

AI와 원어민의 영어 일기 첨삭 결과를 개인 라이브러리와 퀴즈로 복습하는 서비스입니다.

- 구문·예문을 보관하는 개인 라이브러리의 등록·조회·삭제와 검색·북마크·페이징 API를 구현했습니다. 사용자별 소유권과 중복 구문을 검사했습니다.
- 저장한 예문으로 빈칸·객관식 문제를 만들고, 퀴즈 시작·채점·결과 조회·오답 재도전 API를 구현했습니다.
- 첨삭 데이터를 라이브러리의 구문·예문·원문 출처로 저장하는 연계 메서드를 구현하고, 여러 예문을 한 번에 입력받도록 확장했습니다.

사용 기술: Java · Spring Boot · Spring Data JPA · MySQL

## Personal Study

실제 코드·문서와 커밋 기록을 기준으로 정리한 학습 이력입니다. 기본 생성 코드나 짧은 환경 확인 예제는 제외했습니다. [연도별 상세 기록](PERSONAL_STUDY.md)

### 2024

- **자료구조·알고리즘:** C/C++로 연결 리스트·스택·큐·트리 순회를 연습하고, Java로 탐색·DP·최단 경로·문자열 문제 풀이를 이어갔습니다. [Java 기록](https://github.com/som141/bj.java)
- **Spring 기초:** 회원·주문 예제로 의존성 주입, 빈 등록·조회, 컴포넌트 스캔과 생명주기 콜백을 실습하고 JUnit 테스트를 작성했습니다. [기초 예제](https://github.com/som141/hello-Spring)
- **Java 동시성:** 스레드 동기화, AtomicInteger, 생산자·소비자 큐, Executor·Future 예제를 작성했습니다. [학습 코드](https://github.com/som141/bj.java)

### 2025

- **웹 요청 처리:** Servlet에서 프런트 컨트롤러·모델/뷰·핸들러 어댑터로 구조를 바꾸고, Spring MVC 요청 바인딩과 상품 등록·조회·수정을 실습했습니다.
- **Java 함수형 프로그래밍:** 람다·함수형 인터페이스·제네릭으로 컬렉션 처리를 작성하고 Stream·flatMap·Optional을 연습했습니다. [JavaAdvance3](https://github.com/som141/JavaAdvance3)
- **DB·스토리지:** MySQL 복제·수동 승격, MongoDB 복제·샤딩, CephFS·RBD 구성과 장애·복구 확인 절차를 스크립트와 보고서로 정리했습니다. [실습 기록](https://github.com/som141/distruibute-processing-as)

### 2026

- **메시지 처리:** JSON 메시지 발행·소비, 작업 큐와 실패 메시지 보관 큐를 구성하는 Spring AMQP 예제를 작성했습니다. [RabbitMQ 실습](https://github.com/som141/rabbitmq-hello)
- **JPA·PostgreSQL 실습 환경:** 도서·주문 도메인과 시드 데이터, Hibernate 통계 수집 및 실행 계획 조회 API가 있는 학습 환경을 구성했습니다.

일부 학습 저장소는 비공개입니다. 상세 기록에 접근 상태를 표시했고, [공개 전환 대상과 설정 안내](docs/REPOSITORY_VISIBILITY.md)를 별도로 정리했습니다.

## University Projects

| 프로젝트 | 구현 내용 | 사용 기술 |
| --- | --- | --- |
| [날씨 앱·위젯](https://github.com/som141/weather_) | 외부 날씨·미세먼지 API를 연결한 Android 앱과 홈 화면 위젯 | Kotlin · Android |
| [전자결재 시스템](https://github.com/som141/advancedProgramingAs) | 직원 관리·결재 요청·처리·알림을 네 앱으로 나눈 수업 프로젝트 | Java · Spring Boot · MySQL · MongoDB · gRPC |

[작성 근거와 확인 범위](docs/RESUME_SOURCES.md)
