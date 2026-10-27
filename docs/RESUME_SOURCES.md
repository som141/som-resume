# 작성 근거와 확인 범위

확인일: 2026-10-27. 실제 저장소의 코드·커밋과 작성자 본인의 설명을 기준으로 이력서를 정리했습니다. 팀 전체의 기능 소개와 개인 구현 범위를 구분했습니다.

## 프로젝트

| 항목 | 근거 | 표현 범위 |
| --- | --- | --- |
| DIS 제작 계기·사용 범위 | 작성자 설명: 2024년 기존 봇들이 동작하지 않던 경험, 현재 지인 약 30명과 사용 | 개인적인 제작 계기와 실사용 범위. 동시 접속자·활성 사용자 수로 바꾸지 않음 |
| DIS 개발 기록 | [초기 커밋](https://github.com/som141/dis/commit/c0935ef66325701679b005fa75dfe78b05b7f4ca) | Git 이력에서 확인되는 2025.06부터 표시 |
| DIS 음성 보안 대응 · 2026.03.13–15 | 작성자가 설명한 음성 보안 문제, [JDA 업그레이드·연결 진단](https://github.com/som141/dis/commit/1c83d23d894edc445d9e3bc8e8682bb20eb744cd), [DAVE 세션 적용](https://github.com/som141/dis/commit/27387d73b9fb51c354ce98ad9b3eb47e35e60d9f), [컨테이너 환경 정합](https://github.com/som141/dis/commit/59b4e4dfea09561e510bfd2a31982a39c3abe668) | Discord 음성 연결의 보안 호환성 대응. 특정 오류 코드·장애 시간은 미확인 |
| DIS 모놀리식 → MSA · 2026.03.17–18 | [초기 서비스 분리 PR #10](https://github.com/som141/dis/pull/10), [분리 목적·단계 문서](https://github.com/som141/dis/blob/c7dae08e92a14684512a9b09523a831b425c60f2/discord_msa_codex_instructions.md), [앱·빌드·이미지 분리 PR #19](https://github.com/som141/dis/pull/19) | 명령 처리·음악 재생의 역할별 실행과 상태 복구를 위한 구조 변경. 실측 성능 향상이나 완전한 장애 격리 성과로 확대하지 않음 |
| DIS 서버 IP·ngrok 재생 복구 | [로컬·서버의 재생 차이와 IP/ASN·anti-bot 원인 가설 기록](https://github.com/som141/dis/blob/dd90abe/README.md#L300), 작성자 설명: 서버 IP 차단을 ngrok을 이용한 별도 접속 경로로 해결 | IP/ASN 차이는 당시 공개 운영 기록, 원인 확정과 ngrok 복구 경험은 작성자 직접 설명에 근거. 해결 날짜와 상세 연결 구성은 공개 기록에서 미확인 |
| LawGround 역할 | [팀 역할과 개인 구현 보고서](https://github.com/lawground-team/LawGround/blob/ab87fc422f72bdb43a3b4ac39d3cac5ba419a6d8/docs/reports/youngju-integrated-week-08.md) | Spring 백엔드·DB·AI 서비스 연동. 팀원의 Python 모델 구현은 개인 성과에서 제외 |
| LawGround 기여 기간 | 본인 작성 후 병합된 [PR #3](https://github.com/lawground-team/LawGround/pull/3)부터 [PR #30](https://github.com/lawground-team/LawGround/pull/30)까지 | 확인 가능한 개인 기여는 2026.10부터. 실제 법률 정확도·이용자 수·상용 운영 성과는 미확인 |
| LawGround 분석 흐름 | [작업 처리](https://github.com/lawground-team/LawGround/pull/19), [판정·인용 저장](https://github.com/lawground-team/LawGround/pull/21), [추천](https://github.com/lawground-team/LawGround/pull/25), [화면·배치](https://github.com/lawground-team/LawGround/pull/30) | 현재 구현 범위. 재시도 대응을 장애가 전혀 없는 처리로 확대하지 않음 |
| Verbly 역할·기간 | [팀 소개](https://github.com/Verbly-Official/BE/blob/62a008a3cf5883fc050f723b22ff24b8e6e29a3c/README.md), 본인 작성 PR | 본인 기여 기록 2026.01–02, 라이브러리·복습 기능 담당 |
| Verbly 라이브러리·퀴즈 | [PR #25](https://github.com/Verbly-Official/BE/pull/25), [#51](https://github.com/Verbly-Official/BE/pull/51), [#106](https://github.com/Verbly-Official/BE/pull/106) | 개인 구문·예문 관리, 저장 예문 기반 퀴즈와 채점·오답 재도전 |
| Verbly 첨삭 연계 | [PR #122](https://github.com/Verbly-Official/BE/pull/122), [#137](https://github.com/Verbly-Official/BE/pull/137) | 전달받은 첨삭 데이터를 라이브러리에 저장하는 메서드. AI 첨삭·예문 생성 전체를 직접 개발했다고 쓰지 않음 |

DIS의 제작 계기·사용 범위, 음성 보안으로 막혔던 경험과 ngrok을 통한 재생 복구는 작성자가 직접 알려준 사실입니다. 해당 대화의 공개 URL은 없습니다. 공개 코드로 확인한 변경 사항과 작성자가 설명한 실제 운영 경험을 구분했습니다.

## DIS 변경 과정

### 1. Discord 음성 보안 대응

2026년 3월 13일 JDA를 5.6.1에서 6.3.1로 올리고 음성 연결 상태 로그를 추가했습니다. 이어 DAVE 세션 팩토리를 JDA의 음성 설정에 연결했습니다. 로컬 Windows와 서버 컨테이너의 실행 환경 차이도 조정했으며, 3월 15일 기록에서는 Alpine 이미지와 Linux musl용 음성 라이브러리 구성을 확인할 수 있습니다.

이 항목은 Discord 음성 연결의 암호화 호환성 문제입니다. 이후 별도로 발생한 YouTube 인증·음원 접근 실패와 같은 원인으로 묶지 않았습니다.

### 2. 모놀리식에서 역할별 서비스로 전환

기존 봇은 명령 수신과 음악 재생을 한 Java 프로세스에서 처리했습니다. 분리 문서에는 단일 프로세스 구조를 바꾸고, 대기열·재생 상태를 외부에 보관해 재시작 후 복구를 지원하려는 목표가 남아 있습니다.

1. 명령 접수·검증을 담당하는 게이트웨이와 음악 재생을 담당하는 오디오 노드로 역할을 나눴습니다.
2. RabbitMQ로 서비스 사이의 명령·결과를 전달하고, Redis에 대기열·재생 상태를 저장하는 흐름으로 바꿨습니다.
3. 공통 코드는 `common-core`에 두고, 각 앱의 진입점·설정·실행 파일·Docker 이미지를 분리했습니다. 자동 빌드·배포도 두 이미지에 맞춰 수정했습니다.
4. [3월 18일 작업 기록](https://github.com/som141/dis/blob/88c5fdd/docs/CODEX_WORK_LOG.md#L508)에는 앱별 컴파일·패키징 성공과 게이트웨이·오디오 노드·Redis·RabbitMQ 컨테이너의 정상 상태 확인이 남아 있습니다.
5. 주식 노드는 [4월의 후속 기능 추가](https://github.com/som141/dis/commit/d4b92af)입니다. 최초 모놀리식 봇에 있던 주식 기능을 3월에 떼어냈다고 설명하지 않았습니다.

역할별 실행과 복구 지원은 설계 목적이며, 모든 상황에서 재생이 복구된다거나 응답 속도가 얼마나 빨라졌다는 수치로 바꾸지 않았습니다.

### 3. 로컬·서버 환경 차이와 ngrok 접속 경로

3월 18~24일의 문서에는 원격 서버에서만 YouTube 재생이 실패하는 현상과 서버 IP/ASN·anti-bot 응답 차이를 의심한 기록이 있습니다. 작성자는 서버 IP 차단이 원인이었고 ngrok을 이용한 별도 접속 경로로 재생을 복구했다고 설명했습니다.

공개 저장소에서 당시 ngrok 경로의 구체적인 구성과 해결 날짜는 확인하지 못했습니다. 따라서 특정 PC·중계 서버·프록시 종류나 자동 IP 변경 기능을 임의로 덧붙이지 않았습니다. ngrok 터널 자체가 YouTube 요청의 송신 IP를 자동으로 바꾸는 기능이라고 설명하지 않습니다.

## 학습 기록

[Personal Study](../PERSONAL_STUDY.md)에 대표 코드·커밋을 연결했습니다. 저장소 파일의 존재, 작성한 실습 코드, 측정으로 확인한 결과를 구분했습니다.

- 컴파일 결과물·중복 복사본을 별도 학습 이력으로 세지 않았습니다.
- 기본 생성 코드·단순 환경 확인·빈 저장소는 본문에서 제외했습니다.
- 개인 노트의 향후 계획과 체크하지 않은 학습 목록을 완료한 활동으로 쓰지 않았습니다.
- 쿼리 실습 저장소는 측정 환경 구성까지만 기술했습니다. 최적화 과제와 빈 성능 보고서 양식은 개선 성과의 근거로 사용하지 않았습니다.
- 학습 예제 전체의 정확성이나 현재 실행 성공을 보장하는 설명은 넣지 않았습니다.
- 기술 목록은 프로젝트와 실습에서 사용한 범위이며, 모든 기술의 전문성을 같은 수준으로 주장하지 않습니다.
