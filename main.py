import streamlit as st

# 1. 페이지 기본 설정 및 카툰/만화 스타일 디자인 적용
st.set_page_config(
    page_title="🦎 파충류 사육 대백과 - 카툰 에디션",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - 만화/카툰 & 정글 탐험 테마 (Bold Outline, Hard Shadow, Neon Accent)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Jua', 'Noto Sans KR', sans-serif;
    }
    
    .stApp {
        background-color: #121e17;
        background-image: radial-gradient(#1e3a29 15%, transparent 16%), radial-gradient(#1e3a29 15%, transparent 16%);
        background-size: 30px 30px;
        background-position: 0 0, 15px 15px;
        color: #f0fdf4;
    }

    /* 사이드바 스타일링 */
    section[data-testid="stSidebar"] {
        background-color: #1a2e22 !important;
        border-right: 4px solid #000000;
    }

    /* 만화풍 카드가 들어가는 컨테이너 */
    .comic-card {
        background-color: #1e3a2b;
        border: 4px solid #000000;
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 8px 8px 0px #000000;
        position: relative;
    }

    /* 정글 덩굴 띠 헤더 */
    .comic-header {
        background: linear-gradient(135deg, #22c55e 0%, #15803d 100%);
        border: 4px solid #000000;
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 8px 8px 0px #000000;
        color: #ffffff;
    }

    /* 만화 말풍선 패널 */
    .speech-bubble {
        position: relative;
        background: #fef08a;
        border: 3px solid #000000;
        border-radius: 16px;
        padding: 16px;
        color: #000000;
        font-weight: bold;
        box-shadow: 5px 5px 0px #000000;
        margin-bottom: 15px;
    }
    .speech-bubble::after {
        content: '';
        position: absolute;
        bottom: -15px;
        left: 30px;
        border-width: 15px 15px 0;
        border-style: solid;
        border-color: #fef08a transparent;
        display: block;
        width: 0;
    }
    .speech-bubble::before {
        content: '';
        position: absolute;
        bottom: -20px;
        left: 28px;
        border-width: 17px 17px 0;
        border-style: solid;
        border-color: #000000 transparent;
        display: block;
        width: 0;
    }

    /* 카툰 수치 데이터 박스 */
    .comic-stat {
        background-color: #2e523c;
        border: 3px solid #000000;
        border-radius: 12px;
        padding: 12px;
        box-shadow: 4px 4px 0px #000000;
        margin-bottom: 10px;
    }
    .comic-stat-title {
        font-size: 13px;
        color: #86efac;
        font-weight: bold;
    }
    .comic-stat-val {
        font-size: 17px;
        color: #ffffff;
        font-weight: 900;
    }

    /* 배지 스타일 */
    .badge-easy {
        background-color: #22c55e;
        color: #000;
        border: 2px solid #000;
        padding: 4px 14px;
        border-radius: 12px;
        font-weight: 900;
        box-shadow: 3px 3px 0px #000;
    }
    .badge-medium {
        background-color: #eab308;
        color: #000;
        border: 2px solid #000;
        padding: 4px 14px;
        border-radius: 12px;
        font-weight: 900;
        box-shadow: 3px 3px 0px #000;
    }
    .badge-hard {
        background-color: #ef4444;
        color: #fff;
        border: 2px solid #000;
        padding: 4px 14px;
        border-radius: 12px;
        font-weight: 900;
        box-shadow: 3px 3px 0px #000;
    }

    /* 탭 스타일링 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1a2e22;
        border: 3px solid #000000 !important;
        border-radius: 12px 12px 0 0 !important;
        color: #86efac !important;
        font-weight: bold !important;
        padding: 10px 16px !important;
        box-shadow: 3px 3px 0px #000;
    }
    .stTabs [aria-selected="true"] {
        background-color: #22c55e !important;
        color: #000000 !important;
    }

    /* 만화풍 경고 박스 */
    .comic-alert {
        background-color: #fca5a5;
        border: 3px solid #000;
        color: #000;
        padding: 12px;
        border-radius: 12px;
        font-weight: bold;
        box-shadow: 4px 4px 0px #000;
    }
    
    /* 파충류 일러스트 프레임 */
    .hero-frame {
        background: #fde047;
        border: 5px solid #000;
        border-radius: 20px;
        text-align: center;
        padding: 20px;
        box-shadow: 8px 8px 0px #000;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 2. 파충류 백과사전 데이터베이스
REPTILE_DB = {
    "크레스티드 게코": {
        "category": "붙붙이 도마뱀",
        "en_name": "Crested Gecko",
        "scientific_name": "Correlophus ciliatus",
        "icon": "🦎",
        "difficulty": "★☆☆ 입문 쉬움",
        "difficulty_badge": "badge-easy",
        "price": "5만 ~ 25만원 (인기 모프 수백만원)",
        "temp": "22°C - 26°C (고온 주의!)",
        "humidity": "60% - 80% (저녁 분무 필수)",
        "size": "20cm - 25cm (귀여운 소형)",
        "lifespan": "15년 - 20년",
        "diet_type": "잡식성 (슈퍼푸드 사료)",
        "cage_size": "30x30x45cm 이상 세로형",
        "motto": "귀뚜라미 필요 없어! 과일 맛 사료면 냠냠!",
        "summary": "1994년 멸종된 줄 알았다가 재발견된 뉴칼레도니아의 전설! 속눈썹 같은 멋진 돌기와 앙증맞은 손발가락 패드로 벽을 착착 붙어 타는 인기 1위 게코입니다.",
        "origin": "뉴칼레도니아 우거진 열대 우림",
        "morphs": "노멀, 릴리화이트, 플레임, 헐리퀸, 핀스트라이프",
        "env_detail": """
        #### 🏠 정글 속 세로형 아지트 세팅!
        - **높이가 높은 사육장**: 나무를 타고 노는 습성이 있으므로 **세로형 케이지**가 필수입니다!
        - **바닥재**: 바닥 청소하기 쉬운 **키친타올**이나 **파충류 매트**를 까는 것이 청결 관리에 으뜸입니다.
        - **우림 속 놀이터**: 코르크 보드, 인조 덩굴, 코코넛 은신처를 빽빽하게 넣어 점프 놀이터를 만들어주세요.
        - **여름철 더위 조심!**: 28°C가 넘어가면 뻗어버릴 수 있어요! 에어컨이나 쿨링팬으로 선선하게 만들어주세요.
        """,
        "diet_detail": """
        #### 🥗 인공 사료(슈퍼푸드) 맛있게 주기
        - **주식**: 크레스티드 게코 전용 **슈퍼푸드 가루**를 물과 1:2 비율로 개어 케첩 농도로 줍니다.
        - **식사 주기**: 
          - **아기(유체)**: 2일에 1회 (격일)
          - **어른(성체)**: 3일에 1회
        - **칼슘 보충**: 가끔 칼슘 파우더를 묻힌 곤충을 특식으로 주면 살이 포동포동 차오릅니다!
        """,
        "health_detail": """
        #### 🩺 응급 상황! 건강 지키기
        - **꼬리 자르기 연출!**: 깜짝 놀라거나 꼬리를 잡히면 스르륵 자르고 도망칩니다! (다시 안 자라나니 꼬리는 만지지 마세요)
        - **탈피 부전 방지**: 손가락 끝에 껍질이 남아 괴사하지 않게 물 분무를 촉촉하게 해주세요!
        """
    },
    "레오파드 게코": {
        "category": "지상성 게코",
        "en_name": "Leopard Gecko",
        "scientific_name": "Eublepharis macularius",
        "icon": "🐆",
        "difficulty": "★☆☆ 입문 쉬움",
        "difficulty_badge": "badge-easy",
        "price": "4만 ~ 15만원",
        "temp": "핫존 30°C - 32°C / 쿨존 24°C",
        "humidity": "30% - 40% (건조한 사막)",
        "size": "20cm - 28cm",
        "lifespan": "15년 - 20년",
        "diet_type": "완전 육식성 (생먹이)",
        "cage_size": "45x30x30cm 이상 가로형",
        "motto": "통통한 꼬리가 내 에너지 저장소라구!",
        "summary": "표범 무늬 옷을 입은 사막의 귀요미! 다른 게코와 달리 윙크를 할 수 있는 눈꺼풀이 있고, 꼬리에 영양분을 저장해 통통한 꼬리가 매력 포인트입니다.",
        "origin": "중동 및 아시아 건조 암석 사막",
        "morphs": "하이옐로우, 탠저린, 맥스노우, 블리자드",
        "env_detail": """
        #### 🏜️ 따끈따끈 사막 은신처 세팅
        - **하부 온열 장판 필수!**: 뱃속에서 음식을 소화시키기 때문에 바닥 1/3에 **필름 히터**를 꼭 깔아주어야 합니다.
        - **두 개의 집**: 핫존의 바싹 마른 **건식 은신처** + 쿨존의 촉촉한 **습식 은신처**(탈피 보조용)를 준비합니다.
        """,
        "diet_detail": """
        #### 🦗 꿀꺽! 살아있는 곤충 뷔페
        - **주식**: 살아있는 **귀뚜라미, 밀웜**.
        - **칼슘 더스팅**: 먹이 곤충에 뼈 건강을 위한 **칼슘 파우더**를 하얗게 묻혀서 핀셋으로 챙겨주세요!
        """,
        "health_detail": """
        #### 🩺 통통한 꼬리 건강 체크
        - 꼬리가 마르고 얇아지면 거식이나 배탈의 신호입니다! 바로 사육 온도를 점검해보세요.
        """
    },
    "비어디 드래곤": {
        "category": "주행성 도마뱀",
        "en_name": "Bearded Dragon",
        "scientific_name": "Pogona vitticeps",
        "icon": "🐉",
        "difficulty": "★★☆ 공간 필요",
        "difficulty_badge": "badge-medium",
        "price": "10만 ~ 35만원",
        "temp": "일광욕존 40°C / 쿨존 27°C",
        "humidity": "30% - 40%",
        "size": "45cm - 60cm (멋진 대형)",
        "lifespan": "10년 - 15년",
        "diet_type": "잡식성 (야채+곤충)",
        "cage_size": "120x60x60cm (4자 대형)",
        "motto": "머리를 끄덕이며 인사하는 유쾌한 친구!",
        "summary": "턱 밑에 가시 주름이 있는 사막의 소형 공룡! 사람을 잘 알아보고 팔을 돌려 인사하는 등 주인과의 스킨십 반응이 가장 우수한 멋쟁이 파충류입니다.",
        "origin": "호주 내륙 대사막 지대",
        "morphs": "하이포, 트랜스, 제로, 레더백",
        "env_detail": """
        #### ☀️ 강렬한 태양광 조명 시스템
        - **스팟 램프 & UVB 램프**: 태양빛 대신 **고출력 UVB 램프**를 매일 10시간 이상 켜주어야 갑옷 같은 뼈가 단단해집니다!
        - **넓은 대형 사육장**: 어른이 되면 몸집이 커지므로 최소 3자~4자의 으리으리한 원목 집이 필요해요.
        """,
        "diet_detail": """
        #### 🥗 야채 편식은 안 돼요!
        - **어릴 때**: 곤충 70% + 싱싱한 야채 30%
        - **어른이 될 때**: **야채 70%** (청경채, 치커리, 애호박 등) + 곤충 30%
        """,
        "health_detail": """
        #### 🩺 따뜻한 족욕 타임
        - 미지근한 물에 주 2회 15분간 온수 족욕을 시켜주면 시원하게 똥을 싸고 탈피도 잘 됩니다!
        """
    },
    "콘스네이크": {
        "category": "뱀 (옥수수뱀)",
        "en_name": "Corn Snake",
        "scientific_name": "Pantherophis guttatus",
        "icon": "🐍",
        "difficulty": "★☆☆ 탈출 주의",
        "difficulty_badge": "badge-easy",
        "price": "8만 ~ 20만원",
        "temp": "핫존 29°C / 쿨존 25°C",
        "humidity": "40% - 50%",
        "size": "120cm - 150cm (날씬함)",
        "lifespan": "15년 - 20년",
        "diet_type": "육식성 (해동 냉동 쥐)",
        "cage_size": "90x45x45cm",
        "motto": "탈출 마술사! 뚜껑은 꼭 닫아줘!",
        "summary": "배 바닥의 무늬가 옥수수 알갱이를 닮은 아름답고 순한 뱀! 잔병치레가 없고 온순하여 애완 뱀 세상을 입문하는 집사들에게 사랑받는 1순위 후보입니다.",
        "origin": "북미 대륙의 넓은 초원과 숲",
        "morphs": "아네리, 스노우, 팔메토, 테세라",
        "env_detail": """
        #### 🔐 탈출 불가능한 철통 보안!
        - **슬림한 몸매의 탈출왕**: 바늘구멍 같은 틈새도 뚫고 나갑니다. **잠금장치가 확실한 사육장**을 만드세요!
        """,
        "diet_detail": """
        #### 🐁 따뜻하게 녹인 맛있는 식사
        - **냉동 쥐 급여**: 냉동 쥐를 따뜻한 물(40°C)에 속까지 푹 해동해서 핀셋으로 건네줍니다.
        - **주기**: 일주일에 딱 1번만 먹이면 끝!
        """,
        "health_detail": """
        #### 🩺 식사 후 핸들링 금지
        - 먹이를 먹고 2일 동안 건드리면 토할 수 있어요! 48시간은 소화할 수 있게 가만히 두세요.
        """
    },
    "볼파이톤": {
        "category": "뱀 (비단뱀)",
        "en_name": "Ball Python",
        "scientific_name": "Python regius",
        "icon": "🔮",
        "difficulty": "★★☆ 거식 관리",
        "difficulty_badge": "badge-medium",
        "price": "10만 ~ 35만원",
        "temp": "핫존 32°C / 쿨존 26°C",
        "humidity": "50% - 60%",
        "size": "120cm - 150cm (통통함)",
        "lifespan": "20년 - 30년",
        "diet_type": "육식성 (해동 쥐/라트)",
        "cage_size": "90x45x45cm",
        "motto": "무서우면 동그란 공처럼 몸을 말아!",
        "summary": "겁을 먹으면 머리를 안으로 감싸 탱탱한 공(Ball) 모양이 되는 귀여운 비단뱀! 느릿느릿한 걸음걸이와 묵직하고 둥글둥글한 외모가 아주 순합니다.",
        "origin": "중서부 아프리카 열대 우림",
        "morphs": "파스텔, 피에드, 모하비, 클라운, 바나나",
        "env_detail": "어둡고 아늑한 렉사육장 환경과 높은 습도를 유지해주면 안도감을 느낍니다.",
        "diet_detail": "체온 수준으로 따뜻한 해동 쥐를 제공하며, 계절에 따라 단식을 하더라도 당황하지 마세요.",
        "health_detail": "습도가 낮으면 비늘에 무리가 가므로 촉촉한 바닥재를 세팅해주세요."
    },
    "동부 호스필드 육지거북": {
        "category": "육지거북",
        "en_name": "Russian Tortoise",
        "scientific_name": "Testudo horsfieldii",
        "icon": "🐢",
        "difficulty": "★★☆ 공간 필요",
        "difficulty_badge": "badge-medium",
        "price": "12만 ~ 25만원",
        "temp": "일광욕존 34°C / 쿨존 25°C",
        "humidity": "40% - 50%",
        "size": "15cm - 22cm (아담함)",
        "lifespan": "30년 - 50년 이상",
        "diet_type": "100% 완전 초식성",
        "cage_size": "90x60cm 원목 케이지",
        "motto": "엉금엉금 마이웨이! 땅파기 대장!",
        "summary": "땅을 파는 강력한 앞다리를 가진 씩씩한 육지거북! 과일이나 고기는 절대로 먹지 않고, 신선한 야채 샐러드만 먹는 미식가 엉금입니다.",
        "origin": "중앙아시아의 건조한 초원",
        "morphs": "노멀",
        "env_detail": "코코칩 바닥재를 두껍게 깔아 땅을 파고 들어갈 수 있게 해주는 것이 스트레스 해소에 좋습니다.",
        "diet_detail": "치커리, 청경채, 멀베리 잎 등 칼슘이 풍부하고 섬유질이 많은 신선 야채를 매일 줍니다.",
        "health_detail": "UVB 램프가 없으면 껍질이 울퉁불퉁해지는 피라미딩 현상이 일어나니 조명 관리가 필수입니다."
    }
}

# 3. 사이드바 - 만화 캐릭터 스타일의 메뉴 & 체크리스트
with st.sidebar:
    st.markdown("""
    <div style="background: #22c55e; border: 3px solid #000; border-radius: 16px; padding: 15px; text-align: center; box-shadow: 4px 4px 0px #000; margin-bottom: 20px;">
        <h2 style="color: #000; margin: 0; font-size: 24px;">⛺ 정글 탐험 본부</h2>
        <p style="color: #000; margin: 0; font-size: 13px; font-weight: bold;">파충류 사육 파트너를 선택하세요!</p>
    </div>
    """, unsafe_allow_html=True)
    
    selected_name = st.selectbox(
        "🦎 탐험할 파충류 선택:",
        list(REPTILE_DB.keys())
    )
    
    reptile = REPTILE_DB[selected_name]
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 사이드바 말풍선 팁
    st.markdown(f"""
    <div class="speech-bubble">
        💬 "{reptile['motto']}"
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 사육 장비 장착 체크리스트 (빈 곳 채우기)
    st.markdown("""
    <div style="background: #1e3a2b; border: 3px solid #000; border-radius: 12px; padding: 12px; box-shadow: 4px 4px 0px #000;">
        <h4 style="color: #86efac; margin-top: 0;">🎒 사육장 장비 장착!</h4>
    </div>
    """, unsafe_allow_html=True)
    
    c1 = st.checkbox("안전 사육장 케이지")
    c2 = st.checkbox("온/습도 측정기 & 열원")
    c3 = st.checkbox("UVB & 바스킹 스팟 조명")
    c4 = st.checkbox("전용 바닥재 & 은신처")
    c5 = st.checkbox("맛있는 사료 및 칼슘 파우더")
    c6 = st.checkbox("특수동물병원 연락처 확보")
    
    checked_count = sum([c1, c2, c3, c4, c5, c6])
    st.progress(checked_count / 6)
    
    # 사이드바 하단 만화풍 장식 박스
    st.markdown("""
    <div style="background: #000; color: #fde047; padding: 10px; border-radius: 10px; text-align: center; font-weight: bold; font-size: 12px; margin-top: 20px;">
        💥 WARNING: 파충류의 매력에 빠지면 헤어나올 수 없음!
    </div>
    """, unsafe_allow_html=True)

# 4. 메인 화면 - 만화 타이틀 & 파충류 대문
st.markdown(f"""
<div class="comic-header">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div>
            <span class="{reptile['difficulty_badge']}">{reptile['difficulty']}</span>
            <span style="background-color: #000; color: #86efac; border: 2px solid #000; padding: 4px 12px; border-radius: 12px; font-weight: bold; margin-left: 8px;">{reptile['category']}</span>
            <h1 style="margin: 12px 0 5px 0; font-size: 40px; text-shadow: 2px 2px 0px #000;">{reptile['icon']} {selected_name}</h1>
            <p style="color: #dcfce7; margin: 0; font-weight: bold;">{reptile['en_name']} | 学名: {reptile['scientific_name']}</p>
        </div>
        <div style="font-size: 50px; text-shadow: 4px 4px 0px #000;">
            🌵🌴
        </div>
    </div>
    <hr style="border-color: #000; margin: 15px 0; border-width: 2px;">
    <p style="font-size: 17px; line-height: 1.6; color: #ffffff; margin: 0; font-weight: bold;">{reptile['summary']}</p>
</div>
""", unsafe_allow_html=True)

# 메인 콘텐츠 레이아웃
col1, col2 = st.columns([1.1, 2.0])

with col1:
    # 파충류 캐리커처 프레임 Box
    st.markdown(f"""
    <div class="hero-frame">
        <div style="font-size: 100px; line-height: 1.1;">{reptile['icon']}</div>
        <div style="font-size: 26px; font-weight: 900; color: #000;">{selected_name}</div>
        <div style="font-size: 14px; font-weight: bold; color: #166534; background: #bbf7d0; border: 2px solid #000; border-radius: 10px; padding: 4px; margin-top: 6px;">
            원산지: {reptile['origin']}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 만화 스탯 보드 Box
    st.markdown("""
    <div style="background: #000; color: #fff; padding: 6px 12px; border-radius: 8px 8px 0 0; font-weight: bold; font-size: 14px; display: inline-block;">
        ⚡ 파충류 능력치 스펙
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="comic-card" style="border-top-left-radius: 0;">
        <div class="comic-stat" style="border-color: #22c55e;">
            <div class="comic-stat-title">💰 예상 분양 가격대</div>
            <div class="comic-stat-val" style="color: #4ade80;">{reptile['price']}</div>
        </div>
        <div class="comic-stat">
            <div class="comic-stat-title">🌡️ 추천 적정 온도</div>
            <div class="comic-stat-val">{reptile['temp']}</div>
        </div>
        <div class="comic-stat">
            <div class="comic-stat-title">💧 습도 환경</div>
            <div class="comic-stat-val">{reptile['humidity']}</div>
        </div>
        <div class="comic-stat">
            <div class="comic-stat-title">📏 다 자랐을 때 크기</div>
            <div class="comic-stat-val">{reptile['size']}</div>
        </div>
        <div class="comic-stat">
            <div class="comic-stat-title">⏳ 평균 수명</div>
            <div class="comic-stat-val">{reptile['lifespan']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 빈곳 채우기용 - 파충류 사육 상식 만화 컷
    st.markdown(f"""
    <div style="background: #fde047; border: 3px solid #000; border-radius: 16px; padding: 16px; color: #000; box-shadow: 5px 5px 0px #000;">
        <h4 style="margin: 0 0 8px 0; font-size: 16px;">🎨 모프(Color Pattern) 갤러리</h4>
        <p style="margin: 0; font-size: 13px; font-weight: bold;">{reptile['morphs']}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # 세부 백과사전 탭
    tab1, tab2, tab3, tab4 = st.tabs(["🏠 집 세팅 가이드", "🥗 냠냠 급여법", "🩺 건강 & 병원", "🌡️ 온도 진단기"])
    
    with tab1:
        st.markdown(f"""
        <div class="comic-card">
            {reptile['env_detail']}
            <hr style="border-color: #000;">
            <p style="font-weight: bold; color: #fde047; margin: 0;">📦 추천 사육장 사이즈: {reptile['cage_size']}</p>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown(f"""
        <div class="comic-card">
            {reptile['diet_detail']}
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown(f"""
        <div class="comic-card">
            {reptile['health_detail']}
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.markdown("""
        <div class="comic-card">
            <h3 style="color: #fde047; margin-top: 0;">🌡️ 우리집 방 온도 파충류 적합성 테스트!</h3>
            <p style="font-weight: bold;">스파크가 튀는 탐험가 온습도 진단 시스템입니다.</p>
        """, unsafe_allow_html=True)
        
        user_temp = st.slider("현재 내 방 온도 (°C)", 15, 38, 24)
        
        if st.button("🔥 적합도 테스트 실행!"):
            if "크레스티드" in selected_name:
                if user_temp > 27:
                    st.markdown("""
                    <div class="comic-alert">
                        🚨 경고! 방 온도가 너무 높습니다! 크레스티드 게코는 28°C 이상에서 위험해집니다. 에어컨을 켜주세요!
                    </div>
                    """, unsafe_allow_html=True)
                elif 20 <= user_temp <= 26:
                    st.success("✅ 최고입니다! 크레스티드 게코가 신나게 점프할 수 있는 아주 쾌적한 온도입니다!")
                else:
                    st.warning("⚠️ 조금 쌀쌀하네요! 22°C 이상으로 올려주시는 것을 권장합니다.")
            else:
                st.success(f"✅ 설정된 온도({user_temp}°C)를 바탕으로 스팟 램프나 온열 장판을 세팅해주시면 적합합니다!")
        
        st.markdown("</div>", unsafe_allow_html=True)

    # 오른쪽 빈공간 채우기 - 파충류 사육 에티켓 카툰 가이드
    st.markdown("""
    <div style="background: #1e293b; border: 3px solid #000; border-radius: 16px; padding: 20px; box-shadow: 6px 6px 0px #000; margin-top: 20px;">
        <h4 style="color: #38bdf8; margin-top: 0;">📌 집사의 3대 에티켓 수칙!</h4>
        <ul style="line-height: 1.8; font-weight: bold; color: #f8fafc; margin-bottom: 0;">
            <li>1. 만지기 전후로 반드시 손을 깨끗이 씻어주세요! 🧼</li>
            <li>2. 자고 있는 친구를 갑자기 분무기로 칙칙 쏘지 마세요! 💦</li>
            <li>3. 거식(먹이 거부)이 찾아오면 온도부터 차근차근 점검해보세요! 🌡️</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# 하단 풋터
st.divider()
st.markdown("""
<div style="text-align: center; color: #86efac; font-weight: bold; font-size: 14px;">
    🐊 Reptile Encyclopedia Cartoon Edition | 파충류 집사를 위한 만화풍 대백과사전 🦎
</div>
""", unsafe_allow_html=True)
