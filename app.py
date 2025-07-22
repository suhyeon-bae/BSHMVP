import os
import streamlit as st
from dotenv import load_dotenv
from openai import AzureOpenAI

# 1. 환경 변수 로드
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_AZURE_ENDPOINT = os.getenv("OPENAI_AZURE_ENDPOINT")
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")

# 2. OpenAI 클라이언트 초기화
client = AzureOpenAI(
    api_key=OPENAI_API_KEY,
    api_version=OPENAI_API_VERSION,
    azure_endpoint=OPENAI_AZURE_ENDPOINT,
)

# 3. system_prompt.txt 파일에서 시스템 프롬프트 불러오기
def load_system_prompt(file_path="system_prompt.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return "시스템 프롬프트를 불러오지 못했습니다. 에러: " + str(e)

system_prompt = load_system_prompt()

# 4. Streamlit UI 구성
st.set_page_config(page_title="ITAM 서비스 담당자 도우미")
st.title("💼 ITAM 서비스 담당자 도우미")

user_input = st.text_input("질문을 입력하세요:", placeholder="예: 나는 배수현1입니다. ITAM 담당자 알려주세요")

if st.button("질문하기") and user_input:
    with st.spinner("응답 생성 중..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4o",  # 배포한 Azure OpenAI 모델 이름
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )
            st.markdown("### 🧠 답변")
            st.success(response.choices[0].message.content)

        except Exception as e:
            st.error(f"❌ 오류 발생: {str(e)}")
