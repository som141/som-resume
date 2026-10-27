# 작성 근거와 확인 범위

확인일: 2026-10-27. 실제 저장소의 코드·커밋과 작성자 본인의 설명을 기준으로 이력서를 정리했습니다. 팀 전체의 기능 소개와 개인 구현 범위를 구분했습니다.

## 프로젝트

| 항목 | 근거 | 표현 범위 |
| --- | --- | --- |
| DIS 제작 계기·사용 범위 | 작성자 설명: 2024년 기존 봇들이 동작하지 않던 경험, 현재 지인 약 30명과 사용 | 개인적인 제작 계기와 실사용 범위. 동시 접속자·활성 사용자 수로 바꾸지 않음 |
| DIS 개발 기록 | [초기 커밋](https://github.com/som141/dis/commit/c0935ef66325701679b005fa75dfe78b05b7f4ca) | Git 이력에서 확인되는 2025.06부터 표시 |
| DIS 재생 복구 | 작성자가 공유한 실패 로그·정상화 확인, [인증 설정](https://github.com/som141/dis/commit/b0a4bfcef266dbb05c8594fd8d80e6adcea6eea5), [음원 요청 호환성 수정](https://github.com/som141/dis/commit/41b2044ebb20ba8c19f878379d28d516434db5fc) | 해당 환경에서의 재생 복구. 모든 곡의 가용성·성공률 수치는 없음 |
| DIS 응답 순서 | [변경 커밋](https://github.com/som141/dis/commit/569a51fffb15c64b019ead925a09fe0efe6509bf)와 회귀 테스트 | 응답 정보를 저장한 후 작업 발행. 실제 대규모 메시지 유실 건수는 없음 |
| DIS 빌드·배포 복구 | [같은 버전의 공식 파일 사용·검증](https://github.com/som141/dis/commit/32df09c84365726d5c110472738f913bdef25fae), [성공한 자동 빌드·배포](https://github.com/som141/dis/actions/runs/39726968148) | 외부 라이브러리 공급 문제 대응. 무중단·자동 롤백 배포로 표현하지 않음 |
| LawGround 역할 | [팀 역할과 개인 구현 보고서](https://github.com/lawground-team/LawGround/blob/ab87fc422f72bdb43a3b4ac39d3cac5ba419a6d8/docs/reports/youngju-integrated-week-08.md) | Spring 백엔드·DB·AI 서비스 연동. 팀원의 Python 모델 구현은 개인 성과에서 제외 |
| LawGround 기여 기간 | 본인 작성 후 병합된 [PR #3](https://github.com/lawground-team/LawGround/pull/3)부터 [PR #30](https://github.com/lawground-team/LawGround/pull/30)까지 | 확인 가능한 개인 기여는 2026.10부터. 실제 법률 정확도·이용자 수·상용 운영 성과는 미확인 |
| LawGround 분석 흐름 | [작업 처리](https://github.com/lawground-team/LawGround/pull/19), [판정·인용 저장](https://github.com/lawground-team/LawGround/pull/21), [추천](https://github.com/lawground-team/LawGround/pull/25), [화면·배치](https://github.com/lawground-team/LawGround/pull/30) | 현재 구현 범위. 재시도 대응을 장애가 전혀 없는 처리로 확대하지 않음 |
| Verbly 역할·기간 | [팀 소개](https://github.com/Verbly-Official/BE/blob/62a008a3cf5883fc050f723b22ff24b8e6e29a3c/README.md), 본인 작성 PR | 본인 기여 기록 2026.01–02, 라이브러리·복습 기능 담당 |
| Verbly 라이브러리·퀴즈 | [PR #25](https://github.com/Verbly-Official/BE/pull/25), [#51](https://github.com/Verbly-Official/BE/pull/51), [#106](https://github.com/Verbly-Official/BE/pull/106) | 개인 구문·예문 관리, 저장 예문 기반 퀴즈와 채점·오답 재도전 |
| Verbly 첨삭 연계 | [PR #122](https://github.com/Verbly-Official/BE/pull/122), [#137](https://github.com/Verbly-Official/BE/pull/137) | 전달받은 첨삭 데이터를 라이브러리에 저장하는 메서드. AI 첨삭·예문 생성 전체를 직접 개발했다고 쓰지 않음 |

DIS의 정상 재생 확인과 제작 계기는 작성자가 직접 알려준 사실입니다. 해당 대화의 공개 URL은 없으며, 공개 코드만으로 실제 청취 결과나 사용 인원을 검증했다고 표현하지 않았습니다.

## 학습 기록

[Personal Study](../PERSONAL_STUDY.md)에 대표 코드·커밋을 연결했습니다. 저장소 파일의 존재, 작성한 실습 코드, 측정으로 확인한 결과를 구분했습니다.

- 컴파일 결과물·중복 복사본을 별도 학습 이력으로 세지 않았습니다.
- 기본 생성 코드·단순 환경 확인·빈 저장소는 본문에서 제외했습니다.
- 개인 노트의 향후 계획과 체크하지 않은 학습 목록을 완료한 활동으로 쓰지 않았습니다.
- 쿼리 실습 저장소는 측정 환경 구성까지만 기술했습니다. 최적화 과제와 빈 성능 보고서 양식은 개선 성과의 근거로 사용하지 않았습니다.
- 학습 예제 전체의 정확성이나 현재 실행 성공을 보장하는 설명은 넣지 않았습니다.
- 기술 목록은 프로젝트와 실습에서 사용한 범위이며, 모든 기술의 전문성을 같은 수준으로 주장하지 않습니다.
