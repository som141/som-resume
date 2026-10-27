# Personal Study

코드와 개인 노트가 남아 있는 학습 기록을 연도별로 정리했습니다. 날짜는 커밋 작성일과 해당 파일의 이력을 기준으로 했습니다. 강의·과제·개인 연습을 포함하며, 저장소 생성일만으로 학습 기간을 늘리지 않았습니다.

아래 내용은 작성한 코드와 문서의 범위입니다. 이번 문서 정리에서 모든 예제를 다시 실행한 것은 아닙니다. **비공개**로 표시한 링크는 소유자 계정에서만 열립니다. 공개 전환은 [설정 안내](docs/REPOSITORY_VISIBILITY.md)에 정리했습니다.

## 2024

### Spring의 객체 구성과 의존성 주입 · 3–5월 중심, 8월 후속 기록

[hello-Spring](https://github.com/som141/hello-Spring) · [ex-2](https://github.com/som141/ex-2) — ex-2 비공개

- 회원 저장소·서비스와 주문·할인 정책 예제로 객체의 역할과 의존성을 나누었습니다.
- 직접 객체를 조립하는 방식과 설정 클래스를 통한 빈 등록, 컴포넌트 스캔을 비교했습니다.
- 빈 조회·스캔 필터·생명주기 콜백을 실습하고, 회원 중복과 할인 결과 등을 확인하는 JUnit 코드를 작성했습니다.

대표 기록: [서비스 테스트](https://github.com/som141/hello-Spring/blob/29bc293dca3c81deb15aa40bb963c620d9548123/src/test/java/hello/hello/Spring/service/serviceTest.java) · [컴포넌트 스캔 실습 커밋](https://github.com/som141/ex-2/commit/0cff5d8d43764978127e00ce00538164f46fbadd)

### C/C++ 자료구조·알고리즘 · 5–8월

[bj.cpp](https://github.com/som141/bj.cpp) — 비공개

- 연결 리스트와 스택·계산기, 큐·덱의 기본 연산을 코드로 연습했습니다.
- 이진 트리 순회와 행렬 곱셈 순서 등 동적 계획법 예제를 작성했습니다.
- 저장소의 실행 파일은 학습 분량으로 세지 않고, C/C++ 소스만 기준으로 정리했습니다.

대표 기록: [연결 리스트](https://github.com/som141/bj.cpp/blob/ab7a75cdb289925585df4c5fe44f697900c8b72a/Lists/cLinkedList.c) · [트리 순회](https://github.com/som141/bj.cpp/blob/ab7a75cdb289925585df4c5fe44f697900c8b72a/tree/hWe.cpp) · [동적 계획법 실습 커밋](https://github.com/som141/bj.cpp/commit/9a3b46f911a0b3fbeca142b0ca5f5e6f57fa6ad8)

### Java 알고리즘·동시성 · 8–12월

[bj.java](https://github.com/som141/bj.java)

- BFS/DFS, 백트래킹, DP, 최단 경로, 최소 신장 트리, 문자열 탐색과 구간 합 문제를 연습했습니다.
- 제네릭·람다와 함께 동기화 방식, AtomicInteger, 생산자·소비자 큐를 코드로 비교했습니다.
- BlockingQueue와 Executor·Callable·Future 예제로 작업 실행과 결과 수신을 실습했습니다.

대표 기록: [구간 합·갱신](https://github.com/som141/bj.java/blob/3726b61ccb1d954de820074f313b56380f56cff1/src/segmentTree/SegmentTree.java) · [BlockingQueue 예제](https://github.com/som141/bj.java/blob/3726b61ccb1d954de820074f313b56380f56cff1/src/Threads1/cas/sync/boundedQ/BQ6.java) · [Callable 예제](https://github.com/som141/bj.java/blob/3726b61ccb1d954de820074f313b56380f56cff1/src/Threads1/cas/executor/Executor/poll/CallableMainV1.java)

### 파일 시스템 노트 · 11월

파일 오프셋과 디스크 블록, inode, 직접·간접 주소 지정 방식을 개인 노트로 정리했습니다. 관련 원본은 비공개 자료 저장소에 있어 공개 코드 링크와 구분했습니다.

기록: [노트 저장 커밋](https://github.com/som141/-pdf/commit/9d6d43a1cc4418ab3b1a57bb856d82fa78aa9cdd) — 비공개

## 2025

### Servlet에서 Spring MVC까지 · 1–5월

[sv1](https://github.com/som141/sv1) · [sp1](https://github.com/som141/sp1) · [SecondWeb](https://github.com/som141/SecondWeb) — 모두 비공개

- Servlet 기반 회원 예제를 프런트 컨트롤러 방식으로 바꾸고, 모델과 뷰를 분리했습니다.
- 핸들러 어댑터를 연결하는 예제로 요청을 받는 공통 부분과 개별 처리 부분을 나누었습니다.
- Spring MVC의 요청 파라미터·JSON 본문 바인딩과 응답 처리를 연습했습니다.
- Thymeleaf 상품 화면에서 등록·목록·상세·수정을 구현하고, 메모리 저장소의 저장 동작을 확인하는 테스트를 작성했습니다.

대표 기록: [핸들러 어댑터 추가](https://github.com/som141/sv1/commit/c4453ae) · [요청 본문 처리](https://github.com/som141/sp1/blob/96e2156bcd1c1bbd347e10b596fb5927a5b9fc4c/src/main/java/sp1/sp1/basic/request/RequestBodyJsonController.java) · [상품 예제](https://github.com/som141/SecondWeb/blob/c67b0ecfbeda9805d5ba1c8d6bed13fd4a13cf81/src/main/java/com/example/secondweb/domain/web/basic/BasicItemController.java)

### 운영체제와 게시판 설계 노트 · 3–4월

- CPU·메모리 가상화, 동시성, 파일 쓰기를 통한 영속성을 예제와 개인 노트로 정리했습니다. 공유 카운터의 실행 결과가 예상보다 작아지는 사례도 기록했습니다.
- 게시판의 사용자·게시글·댓글 관계와 Controller–Service–Repository 구성을 클래스 다이어그램으로 정리하고 수정했습니다.

기록: [운영체제 노트](https://github.com/som141/-pdf/commit/5447496d84bd26ae5f41308ee391cc295f3cb8f2) · [게시판 설계 수정](https://github.com/som141/-pdf/commit/fd778b1aa22ad8e7bb2101cb66061ab2c806e08d) — 비공개

### Java 함수형 프로그래밍 · 3–9월

[JavaAdvance3](https://github.com/som141/JavaAdvance3)

- 람다·함수형 인터페이스·제네릭을 이용해 컬렉션 처리 코드를 작성했습니다.
- Predicate·Function을 받아 filter/map을 연결하는 학습용 클래스를 만들었습니다.
- 표준 Stream의 flatMap, Optional 예제를 작성했습니다.

대표 기록: [학습용 filter/map 구현](https://github.com/som141/JavaAdvance3/blob/d2024d6df1e6518011befce2398a5bf2f9c32c34/src/lamda/lamdaS/MyStreamV3.java) · [flatMap](https://github.com/som141/JavaAdvance3/blob/d2024d6df1e6518011befce2398a5bf2f9c32c34/src/stream/flatMap.java) · [Optional](https://github.com/som141/JavaAdvance3/blob/d2024d6df1e6518011befce2398a5bf2f9c32c34/src/stream/optional.java)

### 게시판·설계 패턴 실습 · 3–4월, 9–10월

[thWeb](https://github.com/som141/thWeb) · [design_p1](https://github.com/som141/design_p1)

- 회원·게시글·댓글을 JPA 엔티티로 표현하고, 저장소와 Thymeleaf 화면을 연결하는 게시판 예제를 작성했습니다.
- Observer로 날씨 상태 변경을 구독하는 예제, Decorator로 음료와 추가 재료의 가격을 조합하는 예제를 구현했습니다.

대표 기록: [게시글 서비스](https://github.com/som141/thWeb/blob/e5d1c84f7ee6f9a07c1b04e89ecca139d21fdb90/src/main/java/sp1/thweb/Service/PostService.java) · [Observer 예제](https://github.com/som141/design_p1/blob/dc39ff3df2603fb61551c441fec868a3ed8e99fa/design_pattern_example/observer/WeatherData.java)

### DB 복제·분산 스토리지 · 11–12월

[distruibute-processing-as](https://github.com/som141/distruibute-processing-as)

- MySQL 복제 구성과 수동 승격, MongoDB Replica Set과 샤딩의 설치·구성 스크립트를 작성했습니다.
- 복제 전후 데이터 확인, 장애 후 역할 전환·복구 절차를 보고서로 정리했습니다.
- CephFS와 RBD 구성, 파일·블록 장치 마운트, 노드 중단·복구 확인 과정을 기록했습니다.

스크립트와 실습 보고서를 근거로 한 항목입니다. 운영 서비스의 고가용성 구축이나 장애 복구 시간·성능 개선 수치를 주장하지 않습니다.

2024년에 시작한 [Java 알고리즘 풀이](https://github.com/som141/bj.java)도 2025년에 구현·탐색·문자열 문제를 추가하며 이어갔습니다.

## 2026

### Spring AMQP 메시지 처리 코드 · 3월

[rabbitmq-hello](https://github.com/som141/rabbitmq-hello)

- DTO를 JSON 메시지로 발행하고 소비하는 코드를 작성했습니다.
- 작업 큐와 실패 메시지 보관 큐를 구성하고, 실패 메시지 거부와 x-death 헤더 확인 흐름을 구현했습니다.

대표 기록: [실패 메시지 소비 코드](https://github.com/som141/rabbitmq-hello/blob/9a8f47a5ece13aa927d54336ca94525d742a6423/src/main/java/rabbittest/rabbitmqhello/consumer/DlqExampleConsumer.java)

### JPA·PostgreSQL 쿼리 실습 환경 구성 · 7월

[bookstore-query-lab](https://github.com/som141/bookstore-query-lab) — 비공개

- 도서·회원·주문 등 JPA 도메인과 학습용 데이터 생성 스크립트를 구성했습니다.
- 실행 시간·JDBC PreparedStatement 준비 횟수·엔티티 로드 수를 모으는 측정 코드와 PostgreSQL 실행 계획을 JSON으로 조회하는 API를 작성했습니다.
- 챕터 안내와 실습 결과를 확인할 수 있는 학습 화면을 구성했습니다.

대표 기록: [환경 구성 커밋](https://github.com/som141/bookstore-query-lab/commit/dca3b89fab5f079a21d2d8bec69849a43768c39f) · [측정 코드](https://github.com/som141/bookstore-query-lab/blob/b64287e0c6170015da81ef0211736fd849e8205f/src/main/java/bookstore/spring/learning/measurement/PerformanceMeasurementService.java)

여기서 확인되는 것은 **실습 환경 구성**입니다. N+1 해결·인덱스 튜닝 과제 완료나 성능 향상을 확인한 측정 결과는 포함하지 않았습니다.
