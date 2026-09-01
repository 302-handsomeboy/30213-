import streamlit as st

# 1. 페이지 기본 설정 및 디자인 스타일 적용
st.set_page_config(
    page_title="🦎 파충류 백과사전 - 도마뱀 사육 가이드",
    page_icon="🦎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS 스타일링 Injection
st.markdown("""
<style>
    /* 메인 배경 및 폰트 설정 */
    .main {
        background-color: #0f172a;
        color: #f8fafc;
    }
    
    /* 헤더 카드 스타일 */
    .header-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
    }
    
    /* 난이도 배지 */
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

    /* 통계/정보 카드 */
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
        font-size: 20px;
        font-weight: bold;
        color: #f8fafc;
    }

    /* 탭 스타일 조정 */
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

# 2. 도마뱀 데이터베이스 구축
LIZARD_DB = {
    "크레스티드 게코": {
        "en_name": "Crested Gecko",
        "scientific_name": "Correlophus ciliatus",
        "difficulty": "초급 (입문용 추천)",
        "difficulty_badge": "badge-easy",
        "image_url": "https://images.unsplash.com/photo-1596727147705-61a532a659bd?q=80&w=1000&auto=format&fit=crop",
        "temp": "22°C - 26°C (실온 사육 가능)",
        "humidity": "60% - 80% (매일 분무 필수)",
        "size": "20cm - 25cm",
        "lifespan": "15년 - 20년",
        "diet_type": "잡식 (슈퍼푸드 사료 위주 + 귀뚜라미)",
        "cage_size": "30x30x45cm 이상 (높이형 사육장)",
        "summary": "속눈썹 같은 벼슬이 매력적인 뉴칼레도니아 출신 게코입니다. 귀뚜라미 생먹이 없이 전용 슈퍼푸드(가루 사료)만으로도 건강하게 키울 수 있어 파충류 입문자에게 가장 인기 있는 종입니다.",
        "env_info": """
        - **사육장 형태**: 나무를 타는 습성이 있으므로 **세로로 높은 사육장(높이형)**을 준비해야 합니다.
        - **온도 관리**: 고온에 매우 취약합니다. **28°C 이상 올라가지 않도록** 여름철 냉방 관리가 중요합니다.
        - **바닥재**: 키친타올(청결성 추천), 코코피트, 또는 활성탄/에코어스.
        - **구조물**: 덩굴, 유목, 인조 잎사귀 등 은신처와 등반용 구조물을 빽빽하게 채워주세요.
        """,
        "diet_info": """
        - **주식**: 크레스티드 게코 전용 슈퍼푸드 (판게아, 레파시 등)를 물에 개어 격일로 급여.
        - **간식/특식**: 주 1회 기생충 위험이 없는 인공 번식 칼슘 처리 귀뚜라미/밀웜 급여.
        - **영양제**: 슈퍼푸드에 영양소가 포함되어 있으나, 생먹이 급여 시 **칼슘제(D3 포함)** 분말을 묻혀서 급여.
        """,
        "tips": [
            "꼬리가 떨어지면 다시 자라지 않으므로 핸들링 시 꼬리를 세게 잡지 마세요.",
            "야행성이므로 낮에는 어두운 은신처에서 자고 저녁부터 활동합니다.",
            "물그릇 외에도 벽면에 미스트로 분무된 물방울을 핥아 먹는 것을 좋아합니다."
        ]
    },
    "레오파드 게코": {
        "en_name": "Leopard Gecko",
        "scientific_name": "Eublepharis macularius",
        "difficulty": "초급 (입문용 추천)",
        "difficulty_badge": "badge-easy",
        "image_url": "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?q=80&w=1000&auto=format&fit=crop",
        "temp": "핫존 30°C-32°C / 쿨존 24°C-26°C",
        "humidity": "30% - 40% (건조한 환경)",
        "size": "20cm - 28cm",
        "lifespan": "15년 - 20년",
        "diet_type": "육식 (귀뚜라미, 밀웜 등 생먹이)",
        "cage_size": "45x30x30cm 이상 (가로형 사육장)",
        "summary": "표범 무늬와 통통한 꼬리가 매력적인 지상성 게코입니다. 순한 성격과 귀여운 눈망울, 다양한 모프(색상/패턴)로 오랜 기간 사랑받아 온 대표적 입문 파충류입니다.",
        "env_info": """
        - **사육장 형태**: 바닥에서 생활하므로 **가로로 넓은 사육장**이 필요합니다.
        - **열원(필수)**: 사육장 바닥 일부(약 1/3)에 **필름히터/하부장판**을 설치하여 복부 열원을 제공해야 합니다.
        - **은신처**: 건식 은신처와 탈피를 돕기 위한 **습식 은신처(습한 습지/키친타올)**를 함께 제공하세요.
        - **바닥재**: 키친타올, 파충류 전용 매트 (임팩션 방지를 위해 어린 개체는 샌드 금지).
        """,
        "diet_info": """
        - **주식**: 살아있는 귀뚜라미, 밀웜, 두비아 로치.
        - **급여 주기**: 베이비(매일), 성체(2~3일에 1회).
        - **칼슘제 필수**: 칼슘 부족 시 MBD(뼈 질환)가 발생하므로, 생먹이에 **D3 함유 칼슘 가루를 묻혀(더스팅)** 급여하세요.
        """,
        "tips": [
            "영양 상태는 꼬리의 두께로 알 수 있습니다. 통통한 꼬리가 건강의 상징입니다.",
            "눈꺼풀이 있어 눈을 감고 자는 몇 안 되는 게코 중 하나입니다.",
            "핸들링이 매우 쉽지만 느닷없이 이동할 수 있으니 높은 곳에서 떨어지지 않도록 주의하세요."
        ]
    },
    "비어디 드래곤": {
        "en_name": "Bearded Dragon",
        "scientific_name": "Pogona vitticeps",
        "difficulty": "중급 (넓은 공간 필요)",
        "difficulty_badge": "badge-medium",
        "image_url": "https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=1000&auto=format&fit=crop",
        "temp": "바스킹존 38°C-42°C / 쿨존 26°C-28°C",
        "humidity": "30% - 40% (주간 건조)",
        "size": "45cm - 60cm",
        "lifespan": "10년 - 15년",
        "diet_type": "잡식 (성체는 채식 위주 / 어린개체는 육식 위주)",
        "cage_size": "120x60x60cm (3자~4자 이상 대형 사육장)",
        "summary": "턱 밑의 가시 모양 벼슬과 주름이 마치 용을 닮은 주행성 도마뱀입니다. 교감이 잘 되며 주인 알아보는 파충류로 유명하지만, 대형 사육장과 강력한 UVB 조명이 필수적입니다.",
        "env_info": """
        - **사육장**: 성체 기준 최소 3자(90cm) ~ 4자(120cm) 이상의 원목/스팟 사육장이 필요합니다.
        - **조명 필수**: **주행성**이므로 고출력 **UVB 램프**와 일광욕용 **스팟 램프**가 매일 10~12시간 켜져 있어야 합니다.
        - **바닥재**: 바크, 호주 사막 샌드, 타일 또는 키친타올.
        """,
        "diet_info": """
        - **베이비/유체**: 곤충 70% + 야채 30% (귀뚜라미, 듀비아를 매일 먹임).
        - **성체**: 야채 70% + 곤충 30% (치커리, 청경채, 단호박 등 신선한 야채 위주).
        - **주의**: 시금치, 락토스 성분이 있는 음식, 방울토마토 등은 중독 증상을 일으킬 수 있으니 피하세요.
        """,
        "tips": [
            "기분이 좋지 않거나 위협을 느끼면 턱을 검게 부풀려 '비어드(수염)'를 만듭니다.",
            "손을 동그랗게 돌리는 '암 웨이빙(Arm Waving)'은 복종이나 인사의 표현입니다.",
            "주기적인 온수욕(족욕)은 배변 유도와 탈피에 큰 도움이 됩니다."
        ]
    },
    "베일드 카멜레온": {
        "en_name": "Veiled Chameleon",
        "scientific_name": "Chamaeleo calyptratus",
        "difficulty": "상급 (섬세한 환경 관리 필요)",
        "difficulty_badge": "badge-hard",
        "image_url": "https://images.unsplash.com/photo-1596854407944-bf87f6fdd49e?q=80&w=1000&auto=format&fit=crop",
        "temp": "바스킹존 32°C-35°C / 주간 25°C-28°C",
        "humidity": "50% - 70% (통풍 매우 중요)",
        "size": "35cm - 60cm",
        "lifespan": "5년 - 8년",
        "diet_type": "육식 (귀뚜라미, 밀웜 등 움직이는 곤충)",
        "cage_size": "60x60x120cm 이상 (망 사육장 추천)",
        "summary": "머리 위 투구 모양(투구/베일)과 신비로운 색상 변화, 긴 혀로 곤충을 사냥하는 모습이 예술적인 파충류입니다. 통풍 문제와 스트레스에 민감하여 섬세한 사육 환경 구축이 필요합니다.",
        "env_info": """
        - **사육장**: 밀폐된 유리장보다는 **매쉬(망)로 된 통풍이 원활한 높이형 사육장**이 좋습니다.
        - **수분 공급**: 고인 물을 마시지 않습니다. **드립시스템(물방울 떨어지는 장치)**이나 자동 미스팅기로 나뭇잎에 맺힌 물을 마시게 해야 합니다.
        - **조명**: 강한 UVB 램프와 열원이 필수적입니다.
        """,
        "diet_info": """
        - 살아있는 귀뚜라미, 왁스웜, 밀웜 등 다양하고 활동적인 곤충 급여.
        - 비타민과 칼슘 가루를 매주 정기적으로 더스팅하여 영양 결핍 예방.
        """,
        "tips": [
            "스트레스에 매우 약하므로 과도한 핸들링은 피하는 것이 좋습니다.",
            "독립성이 강해 한 사육장에 두 마리 이상 합사하면 서로 공격합니다.",
            "눈이 360도 각각 따로 움직이며 사냥감을 입체적으로 포착합니다."
        ]
    },
    "푸른혀 도마뱀": {
        "en_name": "Blue-tongued Skink",
        "scientific_name": "Tiliqua scincoides",
        "difficulty": "중급 (대형 사육장 및 잡식 식단)",
        "difficulty_badge": "badge-medium",
        "image_url": "https://images.unsplash.com/photo-1533518463841-d62e1fc91373?q=80&w=1000&auto=format&fit=crop",
        "temp": "바스킹존 35°C-38°C / 쿨존 24°C-26°C",
        "humidity": "40% - 80% (아종별 다름)",
        "size": "40cm - 60cm",
        "lifespan": "15년 - 20년 이상",
        "diet_type": "잡식 (고기, 야채, 과일, 곤충 등)",
        "cage_size": "120x60x45cm 이상 (넓은 가로형)",
        "summary": "선명한 파란색 혀와 통통한 소시지 같은 몸매가 특징인 스킨크입니다. 사람에게 순종적이고 온순하며 무엇이든 잘 먹어 인기 있는 대형 게코/스킨크류입니다.",
        "env_info": """
        - **사육장**: 몸이 길고 지상성이므로 넓고 긴 사육장을 준비해야 합니다.
        - **바닥재**: 땅을 파는 습성(Burrowing)이 있으므로 코코칩이나 버크를 두껍게 깔아주세요.
        - **조명**: 주행성이므로 UVB 램프와 바스킹 스팟 램프가 필수입니다.
        """,
        "diet_info": """
        - **식단 비중**: 단백질 50% (습식 강아지/고양이 사료, 곤충) + 야채 40% + 과일 10%.
        - 영양 밸런스가 뛰어나 먹이 관리가 비교적 재미있습니다.
        """,
        "tips": [
            "위협을 느끼면 입을 크게 벌리고 파란 혀를 내밀어 포식자를 놀라게 합니다.",
            "잡식성이어서 고급 습식 사료와 야채 다진 것을 잘 먹습니다.",
            "탈피할 때 손가락, 발가락 끝 탈피껍질이 잘 빠지는지 확인해 주세요."
        ]
    }
}

# 3. 사이드바 - 도마뱀 선택 메뉴
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2826/2826848.png", width=80)
    st.title("🦎 도마뱀 선택")
    st.caption("반려 도마뱀을 선택하여 상세 사육 가이드를 확인하세요.")
    
    selected_lizard_name = st.selectbox(
        "키우고 싶은 도마뱀 종류:",
        list(LIZARD_DB.keys())
    )
    
    st.divider()
    
    # 초보자 준비물 체크리스트
    st.subheader("🛠️ 필수 입문 준비물")
    c1 = st.checkbox("사육장 (크기/형태 확인)")
    c2 = st.checkbox("온습도계")
    c3 = st.checkbox("열원 (장판 or 램프)")
    c4 = st.checkbox("은신처 & 물그릇")
    c5 = st.checkbox("전용 사료 or 생먹이")
    c6 = st.checkbox("칼슘제 (D3 유/무)")
    
    checked_count = sum([c1, c2, c3, c4, c5, c6])
    st.progress(checked_count / 6)
    st.caption(f"준비 완료: {checked_count} / 6 항목")

# 선택된 도마뱀 데이터 가져오기
lizard = LIZARD_DB[selected_lizard_name]

# 4. 메인 화면 구성
# 상단 타이틀 영역
st.markdown(f"""
<div class="header-card">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <span class="{lizard['difficulty_badge']}">{lizard['difficulty']}</span>
            <h1 style="margin: 10px 0 5px 0; color: #f8fafc; font-size: 38px;">{selected_lizard_name}</h1>
            <p style="color: #94a3b8; font-style: italic; margin: 0;">{lizard['en_name']} ({lizard['scientific_name']})</p>
        </div>
    </div>
    <hr style="border-color: #334155; margin: 15px 0;">
    <p style="font-size: 16px; line-height: 1.6; color: #cbd5e1; margin: 0;">{lizard['summary']}</p>
</div>
""", unsafe_allow_html=True)

# 메인 콘텐츠 컬럼 (왼쪽: 사진 및 핵심 스펙, 오른쪽: 상세 정보 탭)
col1, col2 = st.columns([1, 1.8])

with col1:
    # 도마뱀 고화질 사진
    st.image(lizard["image_url"], caption=f"{selected_lizard_name} 대표 이미지", use_container_width=True)
    
    st.subheader("📊 핵심 사육 스펙")
    
    # 4가지 핵심 요약 카드
    st.markdown(f"""
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
        <div class="stat-card">
            <div class="stat-title">🌡️ 적정 온도</div>
            <div class="stat-value" style="font-size: 15px;">{lizard['temp']}</div>
        </div>
        <div class="stat-card">
            <div class="stat-title">💧 적정 습도</div>
            <div class="stat-value" style="font-size: 15px;">{lizard['humidity']}</div>
        </div>
        <div class="stat-card">
            <div class="stat-title">📏 평균 성체 크기</div>
            <div class="stat-value" style="font-size: 15px;">{lizard['size']}</div>
        </div>
        <div class="stat-card">
            <div class="stat-title">⏳ 평균 수명</div>
            <div class="stat-value" style="font-size: 15px;">{lizard['lifespan']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.info(f"**🥩 먹이 유형**: {lizard['diet_type']}\n\n**🏠 권장 사육장**: {lizard['cage_size']}")

with col2:
    # 상세 가이드 탭
    tab1, tab2, tab3, tab4 = st.tabs(["🏠 사육 환경", "🥗 먹이 & 영양", "💡 사육 팁 & 노하우", "🧮 시뮬레이터"])
    
    with tab1:
        st.subheader("🏠 사육장 세팅 및 환경 관리")
        st.markdown(lizard["env_info"])
        
        # 실내 온습도 진단 인터랙티브 툴
        st.divider()
        st.subheader("🌡️ 현재 우리집 환경 적합도 테스트")
        room_temp = st.slider("현재 실내 온도 (°C)", 15, 35, 24)
        room_hum = st.slider("현재 실내 습도 (%)", 20, 90, 50)
        
        if st.button("환경 체크하기"):
            if "22°C - 26°C" in lizard["temp"] and (20 <= room_temp <= 27):
                st.success("✅ 현재 방 온도가 이 도마뱀에게 매우 적합합니다!")
            elif room_temp > 28:
                st.warning("⚠️ 실내 온도가 너무 높습니다! 쿨링팬이나 에어컨 조절이 필요합니다.")
            else:
                st.info("💡 추가적인 열원(하부 장판 또는 스팟 램프) 가동을 추천합니다.")

    with tab2:
        st.subheader("🥗 식단 및 영양 관리")
        st.markdown(lizard["diet_info"])
        
        st.warning("⚠️ **칼슘제 급여 안내**: 실내에서 사육하는 도마뱀은 칼슘 흡수를 위해 **비타민 D3가 포함된 칼슘제**를 주 1~2회 사료/생먹이에 묻혀서 주어야 MBD(대사성 뼈 질환)를 예방할 수 있습니다.")

    with tab3:
        st.subheader("💡 집사를 위한 핵심 꿀팁")
        for i, tip in enumerate(lizard["tips"], 1):
            st.markdown(f"**{i}.** {tip}")
            
    with tab4:
        st.subheader("🧮 개체 맞춤 먹이량 계산기")
        st.write("도마뱀의 성장 단계에 맞는 먹이 급여 주기와 양을 계산합니다.")
        
        age_type = st.radio("성장 단계", ["베이비/유체 (1~6개월)", "아성체/준성체 (6~12개월)", "성체 (12개월 이상)"], horizontal=True)
        
        if selected_lizard_name == "크레스티드 게코":
            if "베이비" in age_type:
                st.success("🍼 **급여 가이드**: 케첩 정도 농도의 슈퍼푸드를 소량 매일 또는 격일로 급여하세요.")
            elif "아성체" in age_type:
                st.success("🦎 **급여 가이드**: 주 3회 슈퍼푸드 급여 + 주 1회 귀뚜라미 2~3마리 특식")
            else:
                st.success("👑 **급여 가이드**: 주 2~3회 슈퍼푸드 급여 (50원 동전 크기 양)")
        elif selected_lizard_name == "레오파드 게코":
            if "베이비" in age_type:
                st.success("🍼 **급여 가이드**: 매일 소형 밀웜/귀뚜라미 3~5마리 (칼슘 더스팅 필수)")
            else:
                st.success("👑 **급여 가이드**: 2~3일에 1회, 중/대형 귀뚜라미나 밀웜 4~6마리")
        else:
            st.info("종별 특성에 맞는 식단표를 참고하여 곤충과 야채 비율을 맞춰주세요.")

# 푸터 영역
st.divider()
st.caption("Disclaimer: 본 사육 가이드는 일반적인 권장 사항이며, 개체별 건강 상태 및 환경에 따라 차이가 있을 수 있습니다. 이상 증세 발생 시 특수동물 전문 병원에 방문하세요.")
