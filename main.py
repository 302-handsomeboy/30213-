import streamlit as st
import pandas as pd

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="도마뱀 백과 & 추천", page_icon="🦎", layout="wide")

st.title("🦎 파충류 집사를 위한 도마뱀 종합 가이드")
st.caption("수행평가 프로젝트 | 스트리밋 기반 도마뱀 데이터 도감 및 맞춤형 추천 시스템")

# 2. 데이터 불러오기 (CSV 파일 활용)
@st.cache_data
def load_data():
    # CSV 파일을 불러옵니다.
    df = pd.read_csv("lizards.csv")
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("`lizards.csv` 파일을 찾을 수 없습니다. 같은 폴더에 CSV 파일을 생성해 주세요.")
    st.stop()

# 3. 사이드바 메뉴 구성
st.sidebar.header("📌 메뉴")
menu = st.sidebar.radio("원하는 기능을 선택하세요", ["📖 도마뱀 도감", "🔍 나에게 맞는 도마뱀 찾기"])

# -------------------------------------------------------------------
# [메뉴 1] 도마뱀 도감
# -------------------------------------------------------------------
if menu == "📖 도마뱀 도감":
    st.header("📖 도마뱀 종류별 상세 가이드")
    
    # 도마뱀 선택 박스
    selected_lizard = st.selectbox("알아보고 싶은 도마뱀을 선택하세요", df["name"].tolist())
    
    # 선택된 도마뱀 데이터 추출
    info = df[df["name"] == selected_lizard].iloc[0]
    
    # 레이아웃 분할 (이미지 / 정보)
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.image(info["image_url"], caption=info["name"], use_column_width=True)
        
    with col2:
        st.subheader(info["name"])
        
        # 지표(Metric) 형태로 핵심 정보 표시
        m1, m2 = st.columns(2)
        m1.metric("사육 난이도", info["difficulty"])
        m2.metric("성체 크기", info["size"])
        
        m3, m4 = st.columns(2)
        m3.metric("주요 먹이", info["food"])
        m4.metric("적정 사육 온도", info["temp"])
        
        st.write("---")
        st.write(f"**상세 특징:**\n{info['description']}")

# -------------------------------------------------------------------
# [메뉴 2] 나에게 맞는 도마뱀 찾기
# -------------------------------------------------------------------
elif menu == "🔍 나에게 맞는 도마뱀 찾기":
    st.header("🔍 나에게 어울리는 도마뱀 매칭 테스트")
    st.write("몇 가지 질문에 답하면 당신의 환경에 가장 잘 맞는 도마뱀을 추천해 드립니다.")
    
    with st.form("lizard_quiz"):
        q1 = st.radio(
            "1. 생먹이(귀뚜라미, 밀웜 등 곤충)를 공급할 수 있나요?",
            ["네, 문제없습니다.", "아니요, 곤충은 부담스럽습니다."]
        )
        
        q2 = st.radio(
            "2. 사육 환경 온도를 높게(30°C 이상) 유지할 온열 장비를 사용할 수 있나요?",
            ["네, 온열 램프/매트를 사용할 수 있습니다.", "아니요, 일반 방 안 온도(상온)에서 키우고 싶습니다."]
        )
        
        q3 = st.radio(
            "3. 희망하는 도마뱀의 크기는 어느 정도인가요?",
            ["소형 (손바닥 크기 이하)", "중대형 (사육장이 크고 당당한 크기)"]
        )
        
        submit_button = st.form_submit_button("추천 도마뱀 결과 보기")
        
    if submit_button:
        st.subheader("💡 추천 결과")
        
        # 추천 로직 수행
        if q1 == "아니요, 곤충은 부담스럽습니다.":
            recommended = df[df["food"].str.contains("슈퍼푸드")]
            st.success("👉 **인공사료(슈퍼푸드)로 사육 가능한 도마뱀**을 추천합니다!")
        elif q3 == "중대형 (사육장이 크고 당당한 크기)":
            recommended = df[df["size"].str.contains("중대형")]
            st.success("👉 **사육하는 맛이 있는 중대형 도마뱀**을 추천합니다!")
        elif q2 == "네, 온열 램프/매트를 사용할 수 있습니다.":
            recommended = df[df["temp"].str.contains("28|30|32|35")]
            st.success("👉 **따뜻한 환경에서 활발하게 움직이는 도마뱀**을 추천합니다!")
        else:
            recommended = df[df["difficulty"] == "쉬움"]
            st.success("👉 **입문용으로 가장 적합한 쉬운 도마뱀**을 추천합니다!")
            
        # 추천된 도마뱀 목록 출력
        for idx, row in recommended.iterrows():
            with st.expander(f"🦎 {row['name']} (난이도: {row['difficulty']})"):
                st.write(f"- **먹이:** {row['food']}")
                st.write(f"- **적정 온도:** {row['temp']}")
                st.write(f"- **특징:** {row['description']}")
