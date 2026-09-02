
import streamlit as st

# 1. 페이지 기본 설정 및 디자인 스타일 적용
st.set_page_config(
    page_title="🦎 파충류 백과사전 - 추천 입문 가이드",
    page_icon="🦎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS 스타일링
st.markdown("""
<style>
    .main {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .header-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
    }
    .badge-easy {
        background-color: #059669;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: bold;
    }
    .badge-medium {
        background-color: #d97706;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: bold;
    }
    .badge-hard {
        background-color: #dc2626;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: bold;
    }
    .stat-card {
        background-color: #1e293b;
        border-left: 4px solid #3b82f6;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 12px;
    }
    .stat-title {
        font-size: 12px;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .stat-value {
        font-size: 17px;
        font-weight: bold;
        color: #f8fafc;
    }
    .icon-box {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #1e293b;
        border-radius: 8px 8px 0 0;
        color: #94a3b8;
    }
    .stTabs [aria-selected="true"] {
        background-color: #3b82f6 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# 2. 파충류 10종 데이터베이스 구축 (분양가 추가)
REPTILE_DB = {
    "크레스티드 게코": {
        "category": "도마뱀",
        "en_name": "Crested Gecko",
        "scientific_name": "Correlophus ciliatus",
        "icon": "🦎",
        "difficulty": "초급 (입문용 강추)",
        "difficulty_badge": "badge-easy",
        "price": "5만 ~ 20만원 (노멀 기준)",
        "temp": "22°C - 26°C",
        "humidity": "60% - 80%",
        "size": "20cm - 25cm",
        "lifespan": "15년 - 20년",
        "diet_type": "잡식 (슈퍼푸드 가루 사료 위주)",
        "cage_size": "30x30x45cm (높이형)",
        "summary": "곤충 생먹이 없이 가루 사료(슈퍼푸드)만으로 키울 수 있는 최고의 입문 도마뱀입니다. 상온 사육이 가능해 별도 온열 장치가 크게 필요 없습니다.",
        "env_info": """
        - **사육장**: 나무를 타는 붙붙이 게코이므로 **세로로 높은 사육장**이 필요합니다.
        - **온도 관리**: 고온에 약하므로 **28°C 이상 올라가지 않도록** 유의하세요.
        - **구조물**: 덩굴, 유목, 인조 잎사귀 등 은신처와 이동 통로를 빽빽하게 구성해주세요.
        """,
        "diet_info": """
        - **주식**: 크레스티드 게코 전용 슈퍼푸드를 물에 타서 격일로 급여합니다.
        - **특식**: 주 1회 칼슘 처리된 귀뚜라미를 주면 성장 속도가 빨라집니다.
        """,
        "tips": ["꼬리가 잘리면 다시 자라지 않으므로 과도한 핸들링은 자제하세요.", "저녁 시간에 벽면에 물을 분무해주면 물방울을 핥아 마십니다."]
    },
    "레오파드 게코": {
        "category": "도마뱀",
        "en_name": "Leopard Gecko",
        "scientific_name": "Eublepharis macularius",
        "icon": "🐆",
        "difficulty": "초급 (입문용 강추)",
        "difficulty_badge": "badge-easy",
        "price": "4만 ~ 15만원 (노멀 기준)",
        "temp": "핫존 30°C-32°C / 쿨존 24°C-26°C",
        "humidity": "30% - 40%",
        "size": "20cm - 28cm",
        "lifespan": "15년 - 20년",
        "diet_type": "육식 (귀뚜라미, 밀웜 등 생먹이)",
        "cage_size": "45x30x30cm (가로형)",
        "summary": "통통한 꼬리와 웃는 듯한 귀여운 얼굴이 특징인 지상성 도마뱀입니다. 순한 성격으로 핸들링이 쉽습니다.",
        "env_info": """
        - **열원 필수**: 바닥 1/3 영역에 **하부 장판/필름히터**를 까는 것이 필수입니다.
        - **은신처**: 건식 은신처와 탈피를 돕는 **습식 은신처**를 모두 마련해주세요.
        """,
        "diet_info": """
        - **주식**: 귀뚜라미 또는 밀웜.
        - **필수 영양제**: 뼈 질환(MBD) 예방을 위해 먹이에 **D3 칼슘 가루**를 반드시 묻혀서 급여하세요.
        """,
        "tips": ["통통한 꼬리는 영양 저장소입니다.", "눈꺼풀이 있어 눈을 끔뻑이는 귀여운 모습을 볼 수 있습니다."]
    },
    "비어디 드래곤": {
        "category": "도마뱀",
        "en_name": "Bearded Dragon",
        "scientific_name": "Pogona vitticeps",
        "icon": "🐉",
        "difficulty": "중급 (공간/장비 필요)",
        "difficulty_badge": "badge-medium",
        "price": "10만 ~ 30만원",
        "temp": "바스킹존 38°C-42°C / 쿨존 26°C-28°C",
        "humidity": "30% - 40%",
        "size": "45cm - 60cm",
        "lifespan": "10년 - 15년",
        "diet_type": "잡식 (성체는 채식 위주)",
        "cage_size": "120x60x60cm (4자 대형)",
        "summary": "주인 알아보는 도마뱀으로 불릴 만큼 온순하고 교감이 잘 됩니다. 다만 커다란 사육장과 강력한 조명 장비가 필요합니다.",
        "env_info": """
        - **조명 필수**: 주행성이므로 **UVB 램프**와 일광욕용 **스팟 램프**를 매일 10~12시간 켜주어야 합니다.
        """,
        "diet_info": """
        - **어린 개체**: 곤충 70% + 야채 30%
        - **성체 개체**: 야채 70% (청경채, 치커리 등) + 곤충 30%
        """,
        "tips": ["손을 동그랗게 돌리는 암 웨이빙(Arm Waving) 행동은 인사나 복종의 의미입니다."]
    },
    "사바나 모니터": {
        "category": "도마뱀",
        "en_name": "Savannah Monitor",
        "scientific_name": "Varanus exanthematicus",
        "icon": "🐊",
        "difficulty": "중상급 (대형종)",
        "difficulty_badge": "badge-hard",
        "price": "8만 ~ 20만원",
        "temp": "바스킹존 45°C 이상 / 쿨존 28°C",
        "humidity": "40% - 60%",
        "size": "80cm - 120cm",
        "lifespan": "10년 - 15년",
        "diet_type": "육식 (곤충, 쥐, 메추리)",
        "cage_size": "150x75x75cm 이상",
        "summary": "소형 공룡을 연상시키는 왕도마뱀 계열입니다. 순들순들하게 길들일 수 있지만 크기가 크게 자라므로 충분한 공간 확보가 필수입니다.",
        "env_info": """
        - **땅파기 습성**: 흙이나 흙 혼합 바닥재를 두껍게 깔아주는 것이 좋습니다.
        """,
        "diet_info": """
        - 야생에서는 곤충 위주로 먹으나 사육 시 쥐, 귀뚜라미, 냉동 닭 등을 급여합니다. (비만 주의)
        """,
        "tips": ["어릴 때부터 지속적인 핸들링을 통해 길들여야 성체가 되어서도 온순합니다."]
    },
    "무어리시 게코": {
        "category": "도마뱀",
        "en_name": "Moorish Gecko",
        "scientific_name": "Tarentola mauritanica",
        "icon": "🦎",
        "difficulty": "초급",
        "difficulty_badge": "badge-easy",
        "price": "3만 ~ 7만원",
        "temp": "26°C - 30°C",
        "humidity": "40% - 50%",
        "size": "12cm - 15cm",
        "lifespan": "10년 - 15년",
        "diet_type": "육식 (소형 곤충)",
        "cage_size": "30x30x30cm",
        "summary": "악어 같은 입체적 비늘 표면을 가진 소형 벽면 부착성 게코입니다. 입문용으로 분양가가 매우 저렴하고 사육이 쉽습니다.",
        "env_info": """
        - 벽에 잘 붙으므로 코르크 보드나 코코넛 은신처를 벽면에 배치해주세요.
        """,
        "diet_info": """
        - 소형 귀뚜라미나 밀웜에 칼슘 파우더를 묻혀 급여합니다.
        """,
        "tips": ["빠르고 소심하므로 관상용으로 키우는 것을 추천합니다."]
    },
    "베일드 카멜레온": {
        "category": "도마뱀",
        "en_name": "Veiled Chameleon",
        "scientific_name": "Chamaeleo calyptratus",
        "icon": "🦎",
        "difficulty": "상급 (섬세한 관리)",
        "difficulty_badge": "badge-hard",
        "price": "10만 ~ 25만원",
        "temp": "25°C - 28°C (바스킹 33°C)",
        "humidity": "50% - 70% (통풍 필수)",
        "size": "35cm - 50cm",
        "lifespan": "5년 - 8년",
        "diet_type": "육식 (움직이는 곤충)",
        "cage_size": "60x60x120cm (망 사육장)",
        "summary": "머리 위 높은 투구와 360도 따로 움직이는 눈, 긴 혀가 매력적인 파충류입니다. 환기가 잘 안 되면 병에 걸리기 쉽습니다.",
        "env_info": """
        - 밀폐 유리장 대신 **망(Mesh) 사육장**을 사용하는 것이 환기에 좋습니다.
        """,
        "diet_info": """
        - 고인 물을 먹지 않으므로 나뭇잎에 떨어지는 물방울(드립 시스템/미스팅)을 마시게 해야 합니다.
        """,
        "tips": ["핸들링 스트레스가 크므로 관상 위주 사육을 권장합니다."]
    },
    "푸른혀 도마뱀": {
        "category": "도마뱀",
        "en_name": "Blue-tongued Skink",
        "scientific_name": "Tiliqua scincoides",
        "icon": "👅",
        "difficulty": "중급",
        "difficulty_badge": "badge-medium",
        "price": "25만 ~ 50만원",
        "temp": "바스킹존 35°C / 쿨존 25°C",
        "humidity": "40% - 60%",
        "size": "40cm - 60cm",
        "lifespan": "15년 - 20년",
        "diet_type": "잡식 (고기, 야채, 과일 등)",
        "cage_size": "120x60x45cm",
        "summary": "파란색 혀가 인상적이며 통통한 소시지 몸매를 자랑합니다. 무엇이든 잘 먹고 순해서 매니아층이 두껍습니다.",
        "env_info": """
        - 땅을 파는 습성이 있으므로 코코칩이나 바크를 두껍게 깔아주세요.
        """,
        "diet_info": """
        - 강아지 습식 사료, 야채 다진 것, 곤충 등을 섞어주면 아주 잘 먹습니다.
        """,
        "tips": ["위협을 느끼면 푸른 혀를 내밀며 쉭쉭 소리를 냅니다."]
    },
    "콘스네이크": {
        "category": "뱀",
        "en_name": "Corn Snake",
        "scientific_name": "Pantherophis guttatus",
        "icon": "🐍",
        "difficulty": "초급 (뱀 입문 최강)",
        "difficulty_badge": "badge-easy",
        "price": "8만 ~ 20만원",
        "temp": "25°C - 29°C",
        "humidity": "40% - 50%",
        "size": "120cm - 150cm (슬림함)",
        "lifespan": "15년 - 20년",
        "diet_type": "육식 (해동 냉동 쥐)",
        "cage_size": "90x45x45cm",
        "summary": "뱀 입문자에게 가장 추천하는 종입니다. 온순한 성격, 화려한 색상, 1주일에 1번만 먹이를 주면 되는 쉬운 관리가 장점입니다.",
        "env_info": """
        - 탈출 명수이므로 **사육장 잠금장치**가 완벽해야 합니다.
        """,
        "diet_info": """
        - 5~7일에 1회 따뜻한 물에 해동한 냉동 쥐를 급여합니다.
        """,
        "tips": ["먹이를 먹은 직후 2~3일간은 거식이나 토함을 방지하기 위해 핸들링을 금지하세요."]
    },
    "볼파이톤": {
        "category": "뱀",
        "en_name": "Ball Python",
        "scientific_name": "Python regius",
        "icon": "🐍",
        "difficulty": "초중급",
        "difficulty_badge": "badge-medium",
        "price": "10만 ~ 30만원 (기본 모프)",
        "temp": "핫존 31°C - 33°C / 쿨존 26°C",
        "humidity": "50% - 60%",
        "size": "120cm - 150cm (통통함)",
        "lifespan": "20년 - 30년",
        "diet_type": "육식 (해동 냉동 쥐)",
        "cage_size": "90x45x45cm",
        "summary": "겁이 많아 위협을 느끼면 공처럼 몸을 동그랗게 말아 '볼' 파이톤이라 불립니다. 순하고 통통한 매력이 있습니다.",
        "env_info": """
        - 몸을 숨길 수 있는 딱 맞는 은신처를 매우 좋아합니다.
        """,
        "diet_info": """
        - 주 1회 해동 쥐를 급여하며, 겨울철에 거식(먹이 거부)을 하는 경우가 종종 있습니다.
        """,
        "tips": ["순해서 사람을 물 가능성이 극히 낮습니다."]
    },
    "동부 호스필드 육지거북": {
        "category": "거북",
        "en_name": "Russian Tortoise",
        "scientific_name": "Testudo horsfieldii",
        "icon": "🐢",
        "difficulty": "초중급 (육지거북 입문)",
        "difficulty_badge": "badge-medium",
        "price": "12만 ~ 25만원",
        "temp": "바스킹존 33°C / 쿨존 25°C",
        "humidity": "40% - 50%",
        "size": "15cm - 22cm",
        "lifespan": "30년 - 50년 이상",
        "diet_type": "초식 (야채 및 건초)",
        "cage_size": "90x60cm 이상",
        "summary": "육지거북 중 비교적 소형으로 자라며 튼튼해서 입문용으로 인기 있습니다. 100% 채식을 합니다.",
        "env_info": """
        - 주행성이므로 **UVB 램프**와 스팟 램프가 필수입니다.
        """,
        "diet_info": """
        - 치커리, 청경채, 치커리 등 신선한 야채에 육지거북 전용 칼슘제를 뿌려 매일 급여합니다.
        """,
        "tips": ["수분 보충과 배변 유도를 위해 주 2~3회 따뜻한 물로 온수욕을 시켜주세요."]
    }
}

# 3. 사이드바 - 파충류 선택 메뉴
with st.sidebar:
    st.title("🦎 파충류 선택 (10종)")
    st.caption("반려 파충류를 선택하여 상세 사육 정보와 분양가를 확인하세요.")
    
    selected_name = st.selectbox(
        "키우고 싶은 파충류 종류:",
        list(REPTILE_DB.keys())
    )
    
    st.divider()
    
    # 초보자 준비물 체크리스트
    st.subheader("🛠️ 필수 입문 준비물")
    c1 = st.checkbox("사육장 (크기/형태 확인)")
    c2 = st.checkbox("온습도계")
    c3 = st.checkbox("열원 (장판 or 램프)")
    c4 = st.checkbox("은신처 & 물그릇")
    c5 = st.checkbox("전용 사료 or 생먹이/쥐")
    c6 = st.checkbox("칼슘제 & 영양제")
    
    checked_count = sum([c1, c2, c3, c4, c5, c6])
    st.progress(checked_count / 6)
    st.caption(f"준비 완료: {checked_count} / 6 항목")

# 선택된 파충류 데이터 가져오기
reptile = REPTILE_DB[selected_name]

# 4. 메인 화면 구성
st.markdown(f"""
<div class="header-card">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <span class="{reptile['difficulty_badge']}">{reptile['difficulty']}</span>
            <span style="background-color: #334155; color: #f8fafc; padding: 4px 12px; border-radius: 20px; font-size: 14px; font-weight: bold; margin-left: 8px;">{reptile['category']}</span>
            <h1 style="margin: 10px 0 5px 0; color: #f8fafc; font-size: 36px;">{reptile['icon']} {selected_name}</h1>
            <p style="color: #94a3b8; font-style: italic; margin: 0;">{reptile['en_name']} ({reptile['scientific_name']})</p>
        </div>
    </div>
    <hr style="border-color: #334155; margin: 15px 0;">
    <p style="font-size: 16px; line-height: 1.6; color: #cbd5e1; margin: 0;">{reptile['summary']}</p>
</div>
""", unsafe_allow_html=True)

# 메인 콘텐츠 컬럼
col1, col2 = st.columns([1, 1.8])

with col1:
    # 비주얼 카드
    st.markdown(f"""
    <div class="icon-box">
        <div style="font-size: 70px; margin-bottom: 5px;">{reptile['icon']}</div>
        <div style="font-size: 20px; font-weight: bold; color: #f8fafc;">{selected_name}</div>
        <div style="font-size: 13px; color: #94a3b8; margin-top: 2px;">{reptile['en_name']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📊 핵심 사육 스펙 & 분양가")
    
    st.markdown(f"""
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
        <div class="stat-card" style="grid-column: span 2; border-left-color: #10b981;">
            <div class="stat-title">🏷️ 평균 분양가</div>
            <div class="stat-value" style="color: #10b981;">{reptile['price']}</div>
        </div>
        <div class="stat-card">
            <div class="stat-title">🌡️ 적정 온도</div>
            <div class="stat-value">{reptile['temp']}</div>
        </div>
        <div class="stat-card">
            <div class="stat-title">💧 적정 습도</div>
            <div class="stat-value">{reptile['humidity']}</div>
        </div>
        <div class="stat-card">
            <div class="stat-title">📏 평균 크기</div>
            <div class="stat-value">{reptile['size']}</div>
        </div>
        <div class="stat-card">
            <div class="stat-title">⏳ 평균 수명</div>
            <div class="stat-value">{reptile['lifespan']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.info(f"**🥩 먹이 유형**: {reptile['diet_type']}\n\n**🏠 권장 사육장**: {reptile['cage_size']}")

with col2:
    tab1, tab2, tab3 = st.tabs(["🏠 사육 환경", "🥗 먹이 & 영양", "💡 핵심 꿀팁"])
    
    with tab1:
        st.subheader("🏠 사육장 세팅 및 환경 관리")
        st.markdown(reptile["env_info"])
        
        st.divider()
        st.subheader("🌡️ 현재 우리집 환경 적합도 테스트")
        room_temp = st.slider("현재 실내 온도 (°C)", 15, 35, 24)
        
        if st.button("환경 체크하기"):
            if "22°C - 26°C" in reptile["temp"] and (20 <= room_temp <= 27):
                st.success("✅ 현재 방 온도가 이 파충류에게 매우 적합합니다!")
            elif room_temp > 28:
                st.warning("⚠️ 실내 온도가 높습니다! 쿨링팬 조절이 필요할 수 있습니다.")
            else:
                st.info("💡 추가적인 열원(장판/램프) 가동이 권장됩니다.")

    with tab2:
        st.subheader("🥗 식단 및 영양 관리")
        st.markdown(reptile["diet_info"])
        st.warning("⚠️ **영양제 안내**: 파충류는 실내 사육 시 칼슘 결핍(MBD)에 걸리기 쉬우므로 적절한 **칼슘 파우더 더스팅**이 필수입니다.")

    with tab3:
        st.subheader("💡 집사를 위한 핵심 꿀팁")
        for i, tip in enumerate(reptile["tips"], 1):
            st.markdown(f"**{i}.** {tip}")

st.divider()
st.caption("Disclaimer: 제시된 분양가는 숍/개인 분양 및 모프(색상/패턴)에 따라 달라질 수 있으며 일반적인 평균 기준입니다.")
