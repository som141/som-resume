# 개인 학습 기록

학교 수업과 개인 연습을 하며 남긴 학습 내용을 연도별로 정리했습니다.

## 2024

### Spring의 객체 구성과 의존성 주입 · 3–5월 중심, 8월 후속 기록

[hello-Spring](https://github.com/som141/hello-Spring)

- 회원 저장소·서비스와 주문·할인 정책 예제로 객체의 역할과 의존성을 나누었습니다.
- 직접 객체를 조립하는 방식과 설정 클래스를 통한 빈 등록, 컴포넌트 스캔을 비교했습니다.
- 빈 조회·스캔 필터·생명주기 콜백을 실습하고, 회원 중복과 할인 결과 등을 확인하는 JUnit 코드를 작성했습니다.

[서비스 테스트](https://github.com/som141/hello-Spring/blob/29bc293dca3c81deb15aa40bb963c620d9548123/src/test/java/hello/hello/Spring/service/serviceTest.java)

### C/C++ 자료구조·알고리즘 · 5–8월

- 연결 리스트와 스택·계산기, 큐·덱의 기본 연산을 코드로 연습했습니다.
- 이진 트리 순회와 행렬 곱셈 순서 등 동적 계획법 예제를 작성했습니다.

### Java 알고리즘·동시성 · 8–12월

[bj.java](https://github.com/som141/bj.java)

- BFS/DFS, 백트래킹, DP, 최단 경로, 최소 신장 트리, 문자열 탐색과 구간 합 문제를 연습했습니다.
- 제네릭·람다와 함께 동기화 방식, AtomicInteger, 생산자·소비자 큐를 코드로 비교했습니다.
- BlockingQueue와 Executor·Callable·Future 예제로 작업 실행과 결과 수신을 실습했습니다.

[구간 합·갱신](https://github.com/som141/bj.java/blob/3726b61ccb1d954de820074f313b56380f56cff1/src/segmentTree/SegmentTree.java) · [BlockingQueue 예제](https://github.com/som141/bj.java/blob/3726b61ccb1d954de820074f313b56380f56cff1/src/Threads1/cas/sync/boundedQ/BQ6.java) · [Callable 예제](https://github.com/som141/bj.java/blob/3726b61ccb1d954de820074f313b56380f56cff1/src/Threads1/cas/executor/Executor/poll/CallableMainV1.java)

### 파일 시스템 노트 · 11월

파일 오프셋과 디스크 블록, inode, 직접·간접 주소 지정 방식을 개인 노트로 정리했습니다.

## 2025

### Servlet에서 Spring MVC까지 · 1–5월

- Servlet 기반 회원 예제를 프런트 컨트롤러 방식으로 바꾸고, 모델과 뷰를 분리했습니다.
- 핸들러 어댑터를 연결하는 예제로 요청을 받는 공통 부분과 개별 처리 부분을 나누었습니다.
- Spring MVC의 요청 파라미터·JSON 본문 바인딩과 응답 처리를 연습했습니다.
- Thymeleaf 상품 화면에서 등록·목록·상세·수정을 구현하고, 메모리 저장소의 저장 동작을 확인하는 테스트를 작성했습니다.

### 운영체제와 게시판 설계 노트 · 3–4월

- CPU·메모리 가상화, 동시성, 파일 쓰기를 통한 영속성을 예제와 개인 노트로 정리했습니다. 공유 카운터의 실행 결과가 예상보다 작아지는 사례도 기록했습니다.
- 게시판의 사용자·게시글·댓글 관계와 Controller–Service–Repository 구성을 클래스 다이어그램으로 정리하고 수정했습니다.

### Java 함수형 프로그래밍 · 3–9월

[JavaAdvance3](https://github.com/som141/JavaAdvance3)

- 람다·함수형 인터페이스·제네릭을 이용해 컬렉션 처리 코드를 작성했습니다.
- Predicate·Function을 받아 filter/map을 연결하는 학습용 클래스를 만들었습니다.
- 표준 Stream의 flatMap, Optional 예제를 작성했습니다.

[filter/map 구현](https://github.com/som141/JavaAdvance3/blob/d2024d6df1e6518011befce2398a5bf2f9c32c34/src/lamda/lamdaS/MyStreamV3.java) · [flatMap](https://github.com/som141/JavaAdvance3/blob/d2024d6df1e6518011befce2398a5bf2f9c32c34/src/stream/flatMap.java) · [Optional](https://github.com/som141/JavaAdvance3/blob/d2024d6df1e6518011befce2398a5bf2f9c32c34/src/stream/optional.java)

### 게시판·설계 패턴 실습 · 3–4월, 9–10월

[thWeb](https://github.com/som141/thWeb) · [design_p1](https://github.com/som141/design_p1)

- 회원·게시글·댓글을 JPA 엔티티로 표현하고, 저장소와 Thymeleaf 화면을 연결하는 게시판 예제를 작성했습니다.
- Observer로 날씨 상태 변경을 구독하는 예제, Decorator로 음료와 추가 재료의 가격을 조합하는 예제를 구현했습니다.

[게시글 서비스](https://github.com/som141/thWeb/blob/e5d1c84f7ee6f9a07c1b04e89ecca139d21fdb90/src/main/java/sp1/thweb/Service/PostService.java) · [Observer 예제](https://github.com/som141/design_p1/blob/dc39ff3df2603fb61551c441fec868a3ed8e99fa/design_pattern_example/observer/WeatherData.java)

### DB 복제·분산 스토리지 · 11–12월

[distruibute-processing-as](https://github.com/som141/distruibute-processing-as)

- MySQL 복제 구성과 수동 승격, MongoDB Replica Set과 샤딩의 설치·구성 스크립트를 작성했습니다.
- 복제 전후 데이터 확인, 장애 후 역할 전환·복구 절차를 보고서로 정리했습니다.
- CephFS와 RBD 구성, 파일·블록 장치 마운트, 노드 중단·복구 확인 과정을 기록했습니다.

2024년에 시작한 [Java 알고리즘 풀이](https://github.com/som141/bj.java)도 2025년에 구현·탐색·문자열 문제를 추가하며 이어갔습니다.

## 2026

### Spring AMQP 메시지 처리 코드 · 3월

[rabbitmq-hello](https://github.com/som141/rabbitmq-hello)

- DTO를 JSON 메시지로 발행하고 소비하는 코드를 작성했습니다.
- 작업 큐와 실패 메시지 보관 큐를 구성하고, 실패 메시지 거부와 x-death 헤더 확인 흐름을 구현했습니다.

[실패 메시지 소비 코드](https://github.com/som141/rabbitmq-hello/blob/9a8f47a5ece13aa927d54336ca94525d742a6423/src/main/java/rabbittest/rabbitmqhello/consumer/DlqExampleConsumer.java)

### JPA·PostgreSQL 쿼리 실습 환경 구성 · 7월

- 도서·회원·주문 등 JPA 도메인과 학습용 데이터 생성 스크립트를 구성했습니다.
- 실행 시간·JDBC PreparedStatement 준비 횟수·엔티티 로드 수를 모으는 측정 코드와 PostgreSQL 실행 계획을 JSON으로 조회하는 API를 작성했습니다.
- 챕터 안내와 실습 결과를 확인할 수 있는 학습 화면을 구성했습니다.
