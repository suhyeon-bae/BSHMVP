# 전사통합IT자산관리 - AI 도입 프로젝트 흐름도

이 문서는 사용자 요청에 따라 권한을 확인하고, AP 담당자 정보를 제공하는 흐름을 Mermaid로 시각화한 것입니다.

```mermaid
flowchart TD
    Start["사용자 질문 입력"] --> CheckAuth{"사용자 권한 확인"}
    CheckAuth -- "보유" --> LookupCode["CODE 테이블에서 AP 담당자 조회"]
    CheckAuth -- "미보유" --> AuthGuide["권한 신청 안내 출력"]

    LookupCode --> CheckAP{"AP 담당자 존재 확인"}
    CheckAP -- "있음" --> ShowAP["AP 담당자 정보 출력"]
    CheckAP -- "없음" --> ShowPOBA["PO / BA 정보 출력"]

