# 전사통합IT자산관리 - AI 도입 프로젝트 흐름도

이 문서는 사용자 요청에 따라 권한을 확인하고, AP 담당자 정보를 제공하는 흐름을 Mermaid로 시각화한 것입니다.






flowchart TD
    Start["🟢 사용자 질문 입력 (Streamlit Web)"]
    Start --> LoadPrompt["📄 system_prompt.txt 로 프롬프트 로드"]
    LoadPrompt --> QueryInput["💬 사용자 입력 수집"]

    QueryInput --> SearchTrigger["🔍 Azure AI Search로 usernm 기준 조회"]
    SearchTrigger --> SearchResult{"🔎 owner 정보 일치 여부 확인"}
    
    SearchResult -- "owner 일치" --> GetServiceCode["🗂️ 표준서비스코드 → 단위서비스코드 매핑"]
    GetServiceCode --> VectorSearch["📡 벡터 임베딩 기반 검색 (embedding 필드)"]
    VectorSearch --> SemanticCheck{"🧠 의미 기반 일치 여부 확인"}

    SemanticCheck -- "일치" --> CheckAuth{"🔐 사용자 권한 확인 (owner 기준)"}
    SemanticCheck -- "불일치" --> FailReason["🚫 관련 데이터 없음 응답"]

    CheckAuth -- "보유" --> LookupCode["📋 CODE 테이블에서 담당자(AP/BA/PO) 조회"]
    CheckAuth -- "미보유" --> AuthGuide["🛂 권한 없음 메시지 출력"]

    LookupCode --> CheckAP{"📌 AP 담당자 존재 여부"}
    CheckAP -- "있음" --> ShowAP["✅ AP 담당자 정보 출력"]
    CheckAP -- "없음" --> ShowPOBA["✅ PO / BA 정보만 출력"]

    ShowAP --> GPTResponse["💡 GPT가 응답 구성 및 출력"]
    ShowPOBA --> GPTResponse
    AuthGuide --> GPTResponse
    FailReason --> GPTResponse

    GPTResponse --> Done["🏁 사용자에게 응답 출력"]
