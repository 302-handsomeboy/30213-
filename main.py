import streamlit as st

# 1. 페이지 기본 설정 및 깔끔한 화이트 카툰 테마
st.set_page_config(
    page_title="🦎 파충류 사육 대백과 - 화이트 에디션",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS - 흰색 배경 & 검은색 텍스트 (고대비 스타일)
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Jua', 'Noto Sans KR', sans-serif;
    }
    
    /* 앱 전체 배경 - 흰색 */
    .stApp {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    /* 사이드바 배경 - 연한 그레이/흰색 */
    section[data-testid="stSidebar"] {
        background-color: #f8fafc !important;
        border-right: 3px solid #000000 !important;
    }

    /* 만화풍 카드 (흰색 배경 + 검은색 테두리 + 검은색 텍스트) */
    .comic-card {
        background-color: #ffffff;
        border: 3px solid #000000;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 5px 5px 0px #000000;
        color: #000000 !important;
    }

    .comic-card h4, .comic-card h3, .comic-card h2, .comic-card h1 {
        color: #000000 !important;
        font-size: 22px !important;
        font-weight: 900 !important;
        margin-bottom: 12px !important;
        border-bottom: 2px solid #000000;
        padding-bottom: 6px;
    }

    .comic-card p, .comic-card li, .comic-card span, .comic-card div {
        color: #000000 !important;
        font-size: 17px !important;
        line-height: 1.7 !important;
        font-weight: 500;
    }

    .comic-card strong {
        color: #15803d !important;
        font-weight: 900 !important;
    }

    /* 메인 헤더 박스 */
    .comic-header {
        background: #f1f5f9;
        border: 3.5px solid #000000;
        border-radius: 20px;
        padding: 26px;
        margin-bottom: 24px;
        box-shadow: 6px 6px 0px #000000;
        color: #000000 !important;
    }

    /* 말풍선 */
    .speech-bubble {
        position: relative;
        background: #fef08a;
        border: 3px solid #000000;
        border-radius: 16px;
        padding: 18px;
        color: #000000 !important;
        font-weight: 900;
        font-size: 17px;
        box-shadow: 4px 4px 0px #000000;
        margin-bottom: 15px;
        text-align: center;
    }
    .speech-bubble p, .speech-bubble span {
        color: #000000 !important;
    }
    .speech-bubble::after {
        content: '';
        position: absolute;
        bottom: -15px;
        left: 40px;
        border-width: 15px 15px 0;
        border-style: solid;
        border-color: #fef08a transparent;
        display: block;
        width: 0;
    }

    /* 수치 데이터 박스 */
    .comic-stat {
        background-color: #f8fafc;
        border: 2px solid #000000;
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 12px;
    }
    .comic-stat-title {
        font-size: 15px;
        color: #475569;
        font-weight: 900;
    }
    .comic-stat-val {
        font-size: 18px;
        color: #000000;
        font-weight: 900;
        margin-top: 4px;
    }

    /* 난이도 배지 */
    .badge-easy {
        background-color: #86efac;
        color: #000000 !important;
        border: 2px solid #000000;
        padding: 6px 14px;
        border-radius: 12px;
        font-weight: 900;
        font-size: 15px;
    }
    .badge-medium {
        background-color: #fef08a;
        color: #000000 !important;
        border: 2px solid #000000;
        padding: 6px 14px;
        border-radius: 12px;
        font-weight: 900;
        font-size: 15px;
    }
    .badge-hard {
        background-color: #fca5a5;
        color: #000000 !important;
        border: 2px solid #000000;
        padding: 6px 14px;
        border-radius: 12px;
        font-weight: 900;
        font-size: 15px;
    }

    /* 탭 스타일링 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #f1f5f9;
        border: 2px solid #000000 !important;
        border-radius: 12px 12px 0 0 !important;
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 16px !important;
        padding: 10px 18px !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #bbf7d0 !important;
        color: #000000 !important;
        border-color: #000000 !important;
    }

    /* 프로필 아이콘 프레임 */
    .hero-frame {
        background: #fef08a;
        border: 3.5px solid #000000;
        border-radius: 20px;
        text-align: center;
        padding: 22px;
        box-shadow: 5px 5px 0px #000000;
        margin-bottom: 20px;
    }

    /* Streamlit 기본 위젯 글자색 강제 적용 */
    .stSelectbox label, .stCheckbox span, .stSlider label {
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 16px !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

# 2. 파충류 10종 대용량 데이터베이스
REPTILE_DB = {
    "크레스티드 게코": {
        "category": "붙붙이 도마뱀",
        "en_name": "Crested Gecko",
        "scientific_name": "Correlophus ciliatus",
        "icon": "🦎",
        "difficulty": "★☆☆ 입문 쉬움",
        "difficulty_badge": "badge-easy",
        "price": "5만 ~ 25만원 (모프별 수백만원)",
        "setup_cost": "약 8만 ~ 15만원 (적재형/유리케이지, 바닥재, 은신처)",
        "monthly_cost": "약 1만 ~ 2만원 (슈퍼푸드 사료 1봉지로 3~4개월 파충류 사육 가능)",
        "temp": "22°C - 26°C (고온에 취약)",
        "humidity": "60% - 80% (저녁 분무 필수)",
        "size": "20cm - 25cm (소형)",
        "lifespan": "15년 - 20년",
        "diet_type": "잡식성 (슈퍼푸드 가루사료)",
        "cage_size": "30x30x45cm 이상 세로형",
        "motto": "귀뚜라미 필요 없어! 달콤한 슈퍼푸드 사료면 OK!",
        "summary": "1994년 멸종된 줄 알았다가 재발견된 뉴칼레도니아의 전설! 눈 위에 속눈썹 같은 돌기가 있고 발바닥 돌기로 유리벽도 착착 붙어 올라가는 가장 인기 많은 입문용 파충류입니다.",
        "habitat": "뉴칼레도니아 열대 우림 (수목성)",
        "morphs": "노멀, 릴리화이트, 플레임, 헐리퀸, 핀스트라이프, 아잔틱",
        "detail_desc": """
        크레스티드 게코는 살아있는 곤충을 무서워하는 초보 집사에게 최적의 파충류입니다. 과일 기반의 슈퍼푸드 가루를 물에 타서 급여하기 때문에 먹이 관리가 매우 간편합니다. 
        야행성이므로 별도의 강한 조명이 필요 없고, 사람 체온보다 약간 낮은 22~26°C의 서늘한 실내 온도를 선호합니다. 여름철 28°C 이상의 고온 노출만 주의하면 매우 건강하게 오래 함께할 수 있습니다.
        """,
        "env_detail": """
        #### 🏠 정글 세로형 케이지 세팅
        - **세로형 사육장**: 높이가 높은 세로형 아크릴 또는 유리 케이지(30x30x45cm 이상)를 사용합니다.
        - **바닥재**: 청결을 위해 키친타올이나 전용 매트를 깔아주세요.
        - **구조물**: 나무를 타는 습성이 있으므로 코르크 보드, 인조 덩굴, 코코넛 은신처를 풍성하게 배치합니다.
        - **분무**: 저녁에 벽면에 무지무라로 분무하여 습도를 높이고 핥아 먹을 물방울을 만들어줍니다.
        """,
        "diet_detail": """
        #### 🥗 슈퍼푸드 급여 가이드
        - **주식**: 크레스티드 게코 전용 슈퍼푸드(판게아, 레파시 등)를 물과 1:2 비율로 섞어 케첩 농도로 만듭니다.
        - **주기**: 유체는 2일에 1회, 성체는 3일에 1회 급여합니다.
        - **특식**: 일주일에 1회 정도 칼슘제를 더스팅한 소형 귀뚜라미를 주면 성장 속도가 빨라집니다.
        """,
        "health_detail": """
        #### 🩺 건강 및 탈피 관리
        - **꼬리 자름**: 놀라거나 잡히면 꼬리를 자르고 도망칩니다. 자란 꼬리는 재생되지 않으므로 꼬리를 잡지 마세요.
        - **탈피 부전**: 습도가 너무 낮으면 손가락 끝에 탈피 껍질이 남아 괴사할 수 있으므로 탈피기에는 온수 족욕을 시켜줍니다.
        """,
    },
    "레오파드 게코": {
        "category": "지상성 게코",
        "en_name": "Leopard Gecko",
        "scientific_name": "Eublepharis macularius",
        "icon": "🐆",
        "difficulty": "★☆☆ 입문 쉬움",
        "difficulty_badge": "badge-easy",
        "price": "4만 ~ 15만원",
        "setup_cost": "약 7만 ~ 12만원 (사육장, 하부 장판, 건/습식 은신처)",
        "monthly_cost": "약 1만 5천원 ~ 2만 5천원 (밀웜 및 귀뚜라미 구매 비용)",
        "temp": "핫존 30°C - 32°C / 쿨존 24°C - 26°C",
        "humidity": "30% - 40% (건조한 환경)",
        "size": "20cm - 28cm",
        "lifespan": "15년 - 20년",
        "diet_type": "완전 육식성 (생먹이 필수)",
        "cage_size": "45x30x30cm 가로형",
        "motto": "통통한 꼬리에 영양분을 가득 저장한다구!",
        "summary": "표범 무늬 옷을 입은 중동 사막의 귀요미! 다른 게코와 달리 윙크를 할 수 있는 눈꺼풀이 있으며, 통통한 꼬리와 순한 성격이 매력적입니다.",
        "habitat": "아프가니스탄, 파키스탄 건조 암석지대",
        "morphs": "하이옐로우, 탠저린, 맥스노우, 블리자드, 이클립스",
        "detail_desc": """
        레오파드 게코는 사막 지대 출신의 지상성 도마뱀입니다. 주식으로 살아있는 귀뚜라미나 밀웜을 먹으며, 뱃속 온도로 소화를 시키기 때문에 하부 히팅 매트 세팅이 필수적입니다.
        배변 장소를 스스로 정해 한곳에만 변을 누는 청결한 습성이 있어 사육장 관리가 매우 쉽고 온순하여 손 위에서 다루는 핸들링이 수월합니다.
        """,
        "env_detail": """
        #### 🏜️ 사막 하부 온열 세팅
        - **가로형 사육장**: 가로가 넓은 2자 케이지나 적재형 사육장을 준비합니다.
        - **필름 히터**: 사육장 바닥의 1/3 부분 아래에 온열 장판을 깔아 핫존(30~32°C)을 만듭니다.
        - **은신처**: 핫존의 건식 은신처 1개 + 습기를 머금은 습식 은신처 1개를 놓아줍니다.
        """,
        "diet_detail": """
        #### 🦗 생먹이 급여 가이드
        - **주식**: 살아있는 귀뚜라미, 밀웜, 듀비아 로치.
        - **영양제**: 생먹이에 반드시 비타민 D3 포함 칼슘 파우더를 하얗게 묻혀(더스팅) 급여합니다.
        - **주기**: 유체 매일 3~5마리, 성체 2~3일에 1회 4~6마리.
        """,
        "health_detail": """
        #### 🩺 건강 및 꼬리 상태
        - **꼬리 두께**: 꼬리가 머리 두께만큼 통통해야 건강한 상태입니다. 꼬리가 얇아지면 거식이나 기생충 감염을 의심해야 합니다.
        """,
    },
    "비어디 드래곤": {
        "category": "주행성 도마뱀",
        "en_name": "Bearded Dragon",
        "scientific_name": "Pogona vitticeps",
        "icon": "🐉",
        "difficulty": "★★☆ 장비/공간 필요",
        "difficulty_badge": "badge-medium",
        "price": "10만 ~ 35만원",
        "setup_cost": "약 25만 ~ 40만원 (4자 원목사육장, 스팟, 고출력 UVB)",
        "monthly_cost": "약 4만 ~ 6만원 (대량의 곤충, 신선 야채, 전기세)",
        "temp": "바스킹존 38°C - 42°C / 쿨존 26°C - 28°C",
        "humidity": "30% - 40%",
        "size": "45cm - 60cm (대형)",
        "lifespan": "10년 - 15년",
        "diet_type": "잡식성 (성장 단계별 비율 변경)",
        "cage_size": "120x60x60cm (4자 필수)",
        "motto": "고개를 끄덕이며 인사하는 친근한 공룡 친구!",
        "summary": "턱 밑에 멋진 가시 주름을 가진 호주 사막의 도마뱀! 주인과 눈을 맞추고 고개를 끄덕이거나 팔을 돌리는 등 교감 반응이 파충류 중 최고 수준입니다.",
        "habitat": "호주 내륙 사막 및 건조한 숲",
        "morphs": "하이포, 트랜스, 제로, 위블리, 레더백",
        "detail_desc": """
        비어디 드래곤은 강렬한 햇빛을 받고 자라는 주행성 파충류입니다. 따라서 자외선을 제공하는 강력한 UVB 조명과 일광욕용 스팟 램프가 사육의 핵심입니다.
        어릴 때는 귀뚜라미나 듀비아 로치를 왕성하게 먹지만, 성체가 되면서 야채 위주의 식단으로 바뀌므로 주기적인 야채 공급이 필요합니다.
        """,
        "env_detail": """
        #### ☀️ 4자 사육장 & 대형 조명 시스템
        - **사육장**: 성체 기준 최소 가로 120cm(4자) 이상의 대형 원목/포맥스 사육장이 필요합니다.
        - **조명**: 스팟 램프로 바스킹존을 40°C로 만들고, 고출력 T5 UVB 램프를 매일 10시간 이상 켜줍니다.
        """,
        "diet_detail": """
        #### 🥗 성장 단계별 식단
        - **어린이(1~6개월)**: 곤충 70% + 싱싱한 야채 30%
        - **어른(12개월 이상)**: 야채 70%(청경채, 치커리, 단호박) + 곤충 30%
        """,
        "health_detail": """
        #### 🩺 온수 족욕 및 뼈 건강
        - UVB 조명이 부족하면 뼈가 무너지는 MBD 질환에 걸릴 수 있습니다. 주 2회 따뜻한 물에 15분간 온수욕을 시켜 소화를 돕습니다.
        """,
    },
    "콘스네이크": {
        "category": "뱀 (옥수수뱀)",
        "en_name": "Corn Snake",
        "scientific_name": "Pantherophis guttatus",
        "icon": "🐍",
        "difficulty": "★☆☆ 탈출 주의",
        "difficulty_badge": "badge-easy",
        "price": "8만 ~ 20만원",
        "setup_cost": "약 8만 ~ 15만원 (잠금 사육장, 하부 열선, 은신처, 물그릇)",
        "monthly_cost": "약 1만원 ~ 1만 5천원 (주 1회 냉동 쥐 급여)",
        "temp": "핫존 28°C - 30°C / 쿨존 24°C - 26°C",
        "humidity": "40% - 50%",
        "size": "120cm - 150cm (슬림함)",
        "lifespan": "15년 - 20년",
        "diet_type": "육식성 (해동 냉동 쥐)",
        "cage_size": "90x45x45cm (3자 케이지)",
        "motto": "탈출 마술사! 사육장 문은 항상 꼭 잠궈줘!",
        "summary": "화려한 색상과 온순한 성격으로 애완 뱀 입문 1위! 독이 없으며 몸이 날씬하여 다루기 쉽고 쥐 먹이 반응이 아주 우수합니다.",
        "habitat": "북미 대륙의 초원 및 농경지",
        "morphs": "애멜라니스틱, 아네리, 스노우, 팔메토, 테세라",
        "detail_desc": """
        콘스네이크는 뱀 사육을 처음 시작하는 분들에게 가장 적합한 종입니다. 잔병치레가 없고 생명력이 강하며 먹이 반응이 일정합니다.
        일주일에 딱 한 번 미지근한 물에 해동한 냉동 쥐를 급여하면 되므로 바쁜 직장인이나 학생이 키우기에 매우 편리합니다. 단, 몸집이 날씬해 사육장 틈새로 탈출하는 것을 철저히 방지해야 합니다.
        """,
        "env_detail": """
        #### 🔐 탈출 방지 & 하부 히팅
        - **사육장**: 슬라이딩 잠금장치가 완벽한 유리/아크릴 사육장을 마련합니다.
        - **열원**: 사육장 하부 1/3 영역에 필름 히터를 깔아 핫존(29°C)을 형성합니다.
        - **바닥재**: 아스펜 쉐이빙(대팻밥)을 깔아 뱀이 속으로 들어갈 수 있게 해줍니다.
        """,
        "diet_detail": """
        #### 🐁 해동 쥐 급여 방법
        - **주기**: 유체 5~7일에 1회, 성체 10~14일에 1회.
        - **해동**: 냉동 쥐를 40°C 따뜻한 물에 완전히 녹여 핀셋으로 흔들어 줍니다.
        """,
        "health_detail": """
        #### 🩺 소화 및 핸들링 수칙
        - 먹이를 먹은 후 최소 48시간 동안은 핸들링을 하지 마세요. 거칠게 만지면 먹었던 쥐를 토할 수 있습니다.
        """,
    },
    "볼파이톤": {
        "category": "뱀 (비단뱀)",
        "en_name": "Ball Python",
        "scientific_name": "Python regius",
        "icon": "🔮",
        "difficulty": "★★☆ 거식 관리",
        "difficulty_badge": "badge-medium",
        "price": "10만 ~ 35만원 (고급 모프 수백만원)",
        "setup_cost": "약 12만 ~ 25만원 (렉사육장, 온도조절기, 물그릇)",
        "monthly_cost": "약 1만 5천원 ~ 2만 5천원 (냉동 라트/쥐)",
        "temp": "핫존 31°C - 33°C / 쿨존 26°C",
        "humidity": "50% - 60%",
        "size": "120cm - 150cm (통통하고 묵직함)",
        "lifespan": "20년 - 30년 이상",
        "diet_type": "육식성 (해동 쥐/라트)",
        "cage_size": "90x45x45cm 또는 렉사육장",
        "motto": "무서우면 머리를 감싸 동그란 공처럼 변해!",
        "summary": "위협을 느끼면 몸을 둥글게 말아 공(Ball)처럼 만드는 신비로운 소형 비단뱀! 느릿하고 순한 성격과 독특한 모프가 매력적입니다.",
        "habitat": "중서부 아프리카 열대 우림",
        "morphs": "파스텔, 피에드, 모하비, 클라운, 바나나, 스파이더",
        "detail_desc": """
        볼파이톤은 묵직하고 통통한 체형을 가진 아름다운 비단뱀입니다. 순하고 물리칠 가능성이 매우 낮아 사람 손을 타는 데 잘 적응합니다.
        다만 계절 변화나 환경 스트레스에 예민하여 몇 달 동안 먹이를 거부하는 '거식' 현상이 올 수 있으므로 정밀한 온도 및 습도 유지가 필수적입니다.
        """,
        "env_detail": """
        #### 🏠 어둡고 아늑한 은신처
        - **환경**: 상단이 뚫린 장보다는 어둡고 안정감을 주는 렉사육장이나 포맥스 사육장이 좋습니다.
        - **온습도**: 핫존 32°C를 유지하고 바크나 코코칩 바닥재를 사용하여 습도를 55% 이상으로 높여줍니다.
        """,
        "diet_detail": """
        #### 🐁 라트 급여 및 거식 대처
        - **주식**: 체중에 맞는 냉동 마우스 또는 라트(대형 쥐).
        - **거식**: 겨울철 거식이 오더라도 체중 감소가 크지 않다면 온도/습도를 점검하고 기다려줍니다.
        """,
        "health_detail": """
        #### 🩺 호흡기 질환 예방
        - 사육장이 차갑고 축축하면 거품 침을 흘리는 호흡기 질환에 걸리기 쉬우므로 핫존 온도를 일정하게 유지하세요.
        """,
    },
    "동부 호스필드 육지거북": {
        "category": "육지거북",
        "en_name": "Russian Tortoise",
        "scientific_name": "Testudo horsfieldii",
        "icon": "🐢",
        "difficulty": "★★☆ 공간 필요",
        "difficulty_badge": "badge-medium",
        "price": "12만 ~ 25만원",
        "setup_cost": "약 20만 ~ 35만원 (원목 사육장, 스팟, UVB, 바닥재)",
        "monthly_cost": "약 2만원 ~ 3만원 (싱싱한 야채 및 육지거북 사료)",
        "temp": "바스킹존 32°C - 35°C / 쿨존 24°C - 26°C",
        "humidity": "40% - 50%",
        "size": "15cm - 22cm (소형 육지거북)",
        "lifespan": "30년 - 50년 이상",
        "diet_type": "100% 완전 초식성",
        "cage_size": "90x60cm 이상 원목 사육장",
        "motto": "엉금엉금 마이웨이! 땅파기 신동 거북이!",
        "summary": "육지거북 중 성체 크기가 작아 가정에서 키우기 가장 적합한 종! 강력한 앞다리로 땅을 파는 버로우 습성과 활발한 걸음걸이가 귀엽습니다.",
        "habitat": "중앙아시아 건조 초원지대",
        "morphs": "노멀",
        "detail_desc": """
        호스필드 육지거북은 완전 초식성 동물로 과일이나 고기를 절대 급여하면 안 됩니다. 섬유질이 풍부한 치커리, 청경채, 멀베리 잎 등을 주식으로 먹습니다.
        활동량이 많고 구석을 파고드는 습성이 강하므로 두꺼운 코코칩 바닥재와 넓은 오픈형 원목 사육장이 필요합니다.
        """,
        "env_detail": """
        #### 🌿 오픈형 원목 사육장 세팅
        - **조명**: 주행성 거북이이므로 UVB 램프와 스팟 램프를 낮 동안 켜주어야 껍질이 단단해집니다.
        - **바닥재**: 파고들 수 있도록 코코칩이나 흙 바닥재를 5cm 이상 두껍게 깔아줍니다.
        """,
        "diet_detail": """
        #### 🥗 100% 야채 샐러드 식단
        - **추천 야채**: 치커리, 청경채, 로메인, 멀베리 잎, 민들레. (배추/시금치/과일 금지)
        - **영양제**: 야채에 육지거북 전용 칼슘 파우더를 매일 뿌려줍니다.
        """,
        "health_detail": """
        #### 🩺 피라미딩 예방 & 온수욕
        - 등갑이 솟아오르는 피라미딩을 방지하기 위해 적절한 습도와 칼슘을 제공하고, 주 3회 따뜻한 물로 온수욕을 시켜줍니다.
        """,
    },
    "사바나 모니터": {
        "category": "왕도마뱀 (모니터)",
        "en_name": "Savannah Monitor",
        "scientific_name": "Varanus exanthematicus",
        "icon": "🐊",
        "difficulty": "★★★ 전문 공간 필요",
        "difficulty_badge": "badge-hard",
        "price": "8만 ~ 20만원 (분양가는 싸지만 시설비 고가)",
        "setup_cost": "약 40만 ~ 80만원 이상 (대형 초대형 사육장, 고열량 스팟)",
        "monthly_cost": "약 5만원 ~ 10만원 이상 (대량의 곤충, 쥐, 고기)",
        "temp": "바스킹존 45°C - 50°C / 쿨존 26°C - 28°C",
        "humidity": "40% - 60%",
        "size": "80cm - 120cm (대형)",
        "lifespan": "10년 - 15년",
        "diet_type": "완전 육식성 (식탐 왕성)",
        "cage_size": "150x75x75cm 이상 (초대형 사육장)",
        "motto": "사막의 미니 공룡! 먹성은 내가 1등!",
        "summary": "아프리카 초원 출신의 왕도마뱀! 분양가는 저렴하지만 어마어마한 크기로 성장하므로 방 한 칸이나 초대형 사육장이 필요한 상급자용 파충류입니다.",
        "habitat": "아프리카 사바나 초원지대",
        "morphs": "노멀",
        "detail_desc": """
        사바나 모니터는 야생의 모니터 느낌을 그대로 가진 카리스마 넘치는 종입니다. 혀를 내밀어 주변 탐색을 하며 엄청난 먹성을 자랑합니다.
        소화를 위해 45°C 이상의 매우 뜨거운 일광욕존이 필요하며, 어릴 때부터 길들이지 않으면 성체가 되었을 때 다루기 힘들어지므로 꾸준한 핸들링 훈련이 요구됩니다.
        """,
        "env_detail": """
        #### 🏜️ 초고온 바스킹 & 초대형 세팅
        - **공간**: 성체가 되면 길이 1.5m 이상의 초대형 전용 케이지가 필수적입니다.
        - **온도**: 바스킹 존 온도를 45~50°C로 매우 높게 유지해야 소화불량을 막습니다.
        """,
        "diet_detail": """
        #### 🥩 대형 육식 식단
        - **먹이**: 귀뚜라미, 대형 로치, 냉동 쥐, 메추리, 계란.
        - **주의**: 사육 상태에서는 비만에 걸리기 쉬우므로 지방이 많은 쥐보다는 곤충 비중을 높여야 합니다.
        """,
        "health_detail": """
        #### 🩺 비만 및 테이밍 관리
        - 과도한 지방 섭취는 간부전을 유발합니다. 어릴 때부터 손에 익숙해지도록 길들여야(테이밍) 안전합니다.
        """,
    },
    "무어리시 게코": {
        "category": "벽면 부착성 게코",
        "en_name": "Moorish Gecko",
        "scientific_name": "Tarentola mauritanica",
        "icon": "🦎",
        "difficulty": "★☆☆ 관상용 추천",
        "difficulty_badge": "badge-easy",
        "price": "3만 ~ 7만원",
        "setup_cost": "약 6만 ~ 10만원 (소형 사육장, 입체 백스크린, 소형 램프)",
        "monthly_cost": "약 1만원 ~ 1만 5천원 (소형 귀뚜라미, 밀웜)",
        "temp": "주간 26°C - 30°C / 야간 20°C",
        "humidity": "40% - 50%",
        "size": "12cm - 15cm (소형)",
        "lifespan": "10년 - 15년",
        "diet_type": "육식성 (소형 곤충)",
        "cage_size": "30x30x30cm",
        "motto": "악어 같은 피부를 가진 날쌔돌이 게코!",
        "summary": "등에 악어처럼 오돌토돌한 돌기가 솟아있는 지중해 게코! 입문용으로 가격이 부담 없고 매우 튼튼한 관상형 도마뱀입니다.",
        "habitat": "지중해 연안 남유럽 및 북아프리카",
        "morphs": "노멀",
        "detail_desc": """
        무어리시 게코는 '크로커다일 게코'라는 별명이 있을 만큼 멋진 피부 질감을 자랑합니다.
        벽면을 빛의 속도로 이동하므로 손으로 만지기보다는 눈으로 관찰하는 관상용 사육에 적합하며, 생명력이 매우 강해 초보자도 쉽게 키울 수 있습니다.
        """,
        "env_detail": """
        #### 🧗 입체 벽면 구조 세팅
        - **구조**: 벽을 잘 타므로 코르크 보드나 입체 백스크린을 벽면에 붙여줍니다.
        """,
        "diet_detail": """
        #### 🦗 소형 곤충 급여
        - 소형 귀뚜라미와 밀웜에 칼슘제를 뿌려 사육장에 넣어주면 사냥해 먹습니다.
        """,
        "health_detail": """
        #### 🩺 관상 위주 사육
        - 스피드가 매우 빠르므로 잡으려다 놓치면 방 구석으로 탈출할 수 있으니 핸들링 시 주의하세요.
        """,
    },
    "베일드 카멜레온": {
        "category": "카멜레온",
        "en_name": "Veiled Chameleon",
        "scientific_name": "Chamaeleo calyptratus",
        "icon": "🦎",
        "difficulty": "★★★ 환기/환경 섬세함",
        "difficulty_badge": "badge-hard",
        "price": "10만 ~ 25만원",
        "setup_cost": "약 20만 ~ 35만원 (전면 망 사육장, 드립시스템, UVB, 생화)",
        "monthly_cost": "약 3만원 ~ 5만원 (다양한 곤충, 미스팅 장비 유지)",
        "temp": "주간 25°C - 28°C (바스킹존 33°C)",
        "humidity": "50% - 70% (환기 필수)",
        "size": "35cm - 55cm",
        "lifespan": "5년 - 8년",
        "diet_type": "육식성 (살아있는 곤충)",
        "cage_size": "60x60x120cm 메쉬 사육장",
        "motto": "머리 위 멋진 투구와 긴 혀 사냥의 명수!",
        "summary": "머리에 높은 투구(Crest)를 쓴 신비로운 카멜레온! 독립적인 두 눈과 기다란 혀를 발사하여 곤충을 사냥하는 모습이 환상적입니다.",
        "habitat": "예멘 및 사우디아라비아 산악지대",
        "morphs": "노멀, 트랜스, 피볼드",
        "detail_desc": """
        카멜레온은 파충류 집사들의 로망이지만 사육 난이도가 높습니다. 밀폐된 사육장에서는 공기가 순환되지 않아 안구 및 호흡기 질환에 쉽게 걸리므로 전면 망 사육장을 써야 합니다.
        또한 고여있는 물을 마시지 않고 잎사귀에 떨어지는 물방울을 핥아 마시므로 자동 미스팅기나 드립 시스템을 설치해주어야 합니다.
        """,
        "env_detail": """
        #### 🍃 전면 망(Mesh) & 드립 시스템
        - **사육장**: 바람이 잘 통하는 전면 망 케이지에 관엽식물(스킨답서스 등)을 세팅합니다.
        - **수분**: 나뭇잎으로 물방울이 떨어지도록 드립 시스템을 상단에 놓습니다.
        """,
        "diet_detail": """
        #### 👅 긴 혀 발사! 곤충 급여
        - 살아있는 귀뚜라미, 왁스웜을 주며 반드시 비타민 D3 포함 칼슘제를 묻혀줍니다.
        """,
        "health_detail": """
        #### 🩺 스트레스 및 환기 관리
        - 스트레스에 매우 취약하므로 1케이지 1개체 단독 사육을 해야 하며 과도한 스킨십을 피해야 합니다.
        """,
    },
    "푸른혀 도마뱀": {
        "category": "지상성 스킨크",
        "en_name": "Blue-tongued Skink",
        "scientific_name": "Tiliqua scincoides",
        "icon": "👅",
        "difficulty": "★★☆ 중급추천",
        "difficulty_badge": "badge-medium",
        "price": "25만 ~ 50만원",
        "setup_cost": "약 20만 ~ 35만원 (4자 가로 사육장, 스팟, UVB, 대형 물그릇)",
        "monthly_cost": "약 2만원 ~ 4만원 (습식 사료, 야채, 과일)",
        "temp": "바스킹존 35°C - 38°C / 쿨존 25°C",
        "humidity": "40% - 70%",
        "size": "40cm - 60cm",
        "lifespan": "15년 - 20년 이상",
        "diet_type": "완전 잡식성 (무엇이든 잘 먹음)",
        "cage_size": "120x60x45cm 가로형",
        "motto": "파란색 혀를 낼름! 대식가 순둥이!",
        "summary": "파란색 혀가 인상적인 호주 대형 스킨크! 짧은 다리와 뱀 같은 매끈한 비늘, 온순하고 먹성이 좋은 순둥이 파충류입니다.",
        "habitat": "호주 및 인도네시아 열대/건조 지대",
        "morphs": "인도네시아, 세람, 이리안자야, 인자이",
        "detail_desc": """
        푸른혀 도마뱀(블루텅 스킨크)은 무엇이든 잘 먹는 엄청난 먹성을 자랑합니다. 고양이 고급 습식 사료, 야채, 과일, 곤충 등 가리지 않고 식사합니다.
        몸집이 길고 지상에서 생활하므로 가로로 넓은 사육장과 버로우할 수 있는 바크 바닥재를 깔아주면 매우 건강하게 자랍니다.
        """,
        "env_detail": """
        #### 🏠 가로형 사육장 & 파고드는 바닥재
        - 바크나 코코칩 바닥재를 깔아 몸을 파묻을 수 있게 하고 UVB와 스팟 램프를 세팅합니다.
        """,
        "diet_detail": """
        #### 🥩 단백질 + 야채 + 과일 뷔페
        - **비율**: 단백질(50%) + 야채(40%) + 과일(10%)
        - 프리미엄 강아지/고양이 습식 캔 사료나 계란 노른자, 야채를 섞어 급여합니다.
        """,
        "health_detail": """
        #### 🩺 발가락 탈피 관리
        - 발가락 비늘 탈피가 잘 되지 않으면 괴사할 수 있으므로 탈피 시 습도 관리에 신경 써주세요.
        """,
    },
    "레오파드 육지거북": {
        "category": "대형 육지거북",
        "en_name": "Leopard Tortoise",
        "scientific_name": "Stigmochelys pardalis",
        "icon": "🐢",
        "difficulty": "★★★ 대형/습도 주의",
        "difficulty_badge": "badge-hard",
        "price": "20만 ~ 45만원",
        "setup_cost": "약 30만 ~ 60만원 (4자~5자 원목 사육장, 스팟, UVB, 보온 장비)",
        "monthly_cost": "약 3만원 ~ 5만원 (건초, 신선 야채, 칼슘 영양제)",
        "temp": "바스킹존 35°C - 38°C / 쿨존 28°C - 30°C",
        "humidity": "50% - 70% (유체기 높은 습도 필수)",
        "size": "40cm - 60cm (대형)",
        "lifespan": "50년 - 100년 이상",
        "diet_type": "100% 고섬유질 초식성",
        "cage_size": "150x90cm 이상 (성체 시 방 한 칸 구역 필요)",
        "motto": "표범 무늬 등갑을 가진 거대하고 아늑한 귀요미!",
        "summary": "표범 무늬처럼 화려하고 아름다운 등갑 패턴을 가진 대형 육지거북! 온순한 성격과 커다란 덩치로 애호가들에게 사랑받는 장수 파충류입니다.",
        "habitat": "아프리카 동남부 건조 사바나 초원",
        "morphs": "바부키, 소말리아 레오파드",
        "detail_desc": """
        레오파드 육지거북은 웅장하고 아름다운 등갑 무늬를 특징으로 합니다. 성체가 되면 40cm가 넘게 자라므로 성장함에 따라 넓은 공간 확보가 필수적입니다.
        어릴 때(유체)는 건조하면 등갑 모양이 피라미드처럼 기형으로 솟는 피라미딩 현상이나 감기에 걸리기 쉬우므로 high-humidity(높은 습도)와 높은 온도를 섬세하게 유지해 주어야 합니다.
        """,
        "env_detail": """
        #### 🦒 넓은 사육장 & 고온 다습 세팅
        - **온도/조명**: 주간 핫존 35°C 이상, 쿨존도 28°C 이상으로 따뜻하게 유지하며 강력한 UVB 램프를 매일 10~12시간 켜줍니다.
        - **바닥재**: 습도를 머금을 수 있는 코코칩이나 바크를 넉넉히 깔아줍니다.
        """,
        "diet_detail": """
        #### 🌾 고섬유질 건초 & 야채 식단
        - **주식**: 알팔파/티모시 건초 가루, 치커리, 청경채, 로메인, 민들레 잎.
        - **주의**: 수분이 너무 많은 야채나 과일은 설사를 유발할 수 있으므로 건초 비율을 높여 급여합니다.
        """,
        "health_detail": """
        #### 🩺 피라미딩 예방 & 감기 주의
        - 어린 시기에는 온수욕을 매일 15분씩 시켜주어 요산 배출을 돕고 등갑이 예쁘고 평평하게 자라도록 유도합니다.
        """,
    },
}

# 3. 사이드바 - 파충류 선택 및 체크리스트
with st.sidebar:
    st.markdown(
        """
    <div style="background: #ffffff; border: 3px solid #000000; border-radius: 12px; padding: 12px; text-align: center; box-shadow: 4px 4px 0px #000000; margin-bottom: 15px;">
        <h2 style="color: #000000; margin: 0; font-size: 22px; font-weight: 900;">⛺ 정글 탐험 본부</h2>
        <p style="color: #000000; margin: 0; font-size: 13px; font-weight: bold;">파충류 10종 백과사전 선택</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    selected_name = st.selectbox("🦎 탐험할 파충류 선택:", list(REPTILE_DB.keys()))

    reptile = REPTILE_DB[selected_name]

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        f"""
    <div class="speech-bubble">
        💬 "{reptile['motto']}"
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
    <div style="background: #ffffff; border: 2.5px solid #000000; border-radius: 12px; padding: 12px; box-shadow: 3px 3px 0px #000000;">
        <h4 style="color: #000000 !important; margin-top: 0; font-size: 17px !important; border-bottom: 1.5px solid #000000;">🎒 필수 장비 점검 체크리스트</h4>
    </div>
    """,
        unsafe_allow_html=True,
    )

    c1 = st.checkbox("사육장 (케이지)")
    c2 = st.checkbox("온열 장판 / 스팟 램프")
    c3 = st.checkbox("UVB 조명 (주행성 한정)")
    c4 = st.checkbox("전용 바닥재 & 은신처")
    c5 = st.checkbox("먹이 & 칼슘 파우더")
    c6 = st.checkbox("특수동물병원 위치 확인")

    checked_count = sum([c1, c2, c3, c4, c5, c6])
    st.progress(checked_count / 6)

# 4. 메인 화면 - 파충류 상세 정보
st.markdown(
    f"""
<div class="comic-header">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div>
            <span class="{reptile['difficulty_badge']}">{reptile['difficulty']}</span>
            <span style="background-color: #ffffff; color: #000000; border: 2px solid #000000; padding: 6px 14px; border-radius: 12px; font-weight: 900; font-size: 15px; margin-left: 8px;">{reptile['category']}</span>
            <h1 style="margin: 12px 0 5px 0; font-size: 42px; font-weight: 900; color: #000000;">{reptile['icon']} {selected_name}</h1>
            <p style="color: #334155; margin: 0; font-weight: bold; font-size: 18px;">{reptile['en_name']} | 학명: {reptile['scientific_name']}</p>
        </div>
    </div>
    <hr style="border-color: #000000; margin: 18px 0; border-width: 1.5px;">
    <p style="font-size: 18px; line-height: 1.7; color: #000000; margin: 0; font-weight: bold;">{reptile['summary']}</p>
</div>
""",
    unsafe_allow_html=True,
)

# 2열 레이아웃
col1, col2 = st.columns([1.1, 2.0])

with col1:
    st.markdown(
        f"""
    <div class="hero-frame">
        <div style="font-size: 95px; line-height: 1.1;">{reptile['icon']}</div>
        <div style="font-size: 26px; font-weight: 900; color: #000000; margin-top: 5px;">{selected_name}</div>
        <div style="font-size: 15px; font-weight: 900; color: #000000; background: #ffffff; border: 2px solid #000000; border-radius: 8px; padding: 6px; margin-top: 10px;">
            서식지: {reptile['habitat']}
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div style="background: #000000; color: #ffffff; padding: 8px 14px; border-radius: 10px 10px 0 0; font-weight: 900; font-size: 16px; border: 2.5px solid #000000; border-bottom: none;">
        ⚡ 한눈에 보는 수치 데이터
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
    <div class="comic-card" style="border-top-left-radius: 0; margin-top: 0;">
        <div class="comic-stat">
            <div class="comic-stat-title">🏷️ 개체 분양가</div>
            <div class="comic-stat-val">{reptile['price']}</div>
        </div>
        <div class="comic-stat">
            <div class="comic-stat-title">🌡️ 적정 사육 온도</div>
            <div class="comic-stat-val">{reptile['temp']}</div>
        </div>
        <div class="comic-stat">
            <div class="comic-stat-title">💧 적정 습도</div>
            <div class="comic-stat-val">{reptile['humidity']}</div>
        </div>
        <div class="comic-stat">
            <div class="comic-stat-title">📏 다 자랐을 때 크기</div>
            <div class="comic-stat-val">{reptile['size']}</div>
        </div>
        <div class="comic-stat">
            <div class="comic-stat-title">⏳ 기대 수명</div>
            <div class="comic-stat-val">{reptile['lifespan']}</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📖 세부 설명",
            "💵 용품 & 먹이 비용",
            "🏠 사육장 세팅",
            "🥗 먹이 & 영양",
            "🩺 건강 & 관리",
        ]
    )

    with tab1:
        st.markdown(
            f"""
        <div class="comic-card">
            <h4>📖 {selected_name} 세부 특징 및 사육 개요</h4>
            <p>{reptile['detail_desc']}</p>
            <hr style="border-color: #000000; margin: 15px 0;">
            <p><strong>🎨 주요 인기 모프/종류:</strong> {reptile['morphs']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tab2:
        st.markdown(
            f"""
        <div class="comic-card">
            <h4>💵 사육 물품 비용 & 월 유지비 상세 분석</h4>
            <ul style="padding-left: 20px;">
                <li style="margin-bottom: 8px;"><strong>🦎 개체 분양가:</strong> {reptile['price']}</li>
                <li style="margin-bottom: 8px;"><strong>🛠️ 초기 사육 용품 비용:</strong> {reptile['setup_cost']}</li>
                <li style="margin-bottom: 8px;"><strong>🥖 월 먹이 및 유지 비용:</strong> {reptile['monthly_cost']}</li>
            </ul>
            <hr style="border-color: #000000; margin: 15px 0;">
            <p style="font-size: 14px !important; color: #475569 !important;">* 초기 비용에는 사육장, 열원, 조명, 바닥재, 은신처, 물그릇 등이 포함되며 모프 및 사육장 재질(원목/유리/아크릴)에 따라 차이가 있을 수 있습니다.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tab3:
        st.markdown(
            f"""
        <div class="comic-card">
            {reptile['env_detail']}
            <hr style="border-color: #000000; margin: 15px 0;">
            <p><strong>📦 권장 사육장 크기:</strong> {reptile['cage_size']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tab4:
        st.markdown(
            f"""
        <div class="comic-card">
            {reptile['diet_detail']}
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tab5:
        st.markdown(
            f"""
        <div class="comic-card">
            {reptile['health_detail']}
        </div>
        """,
            unsafe_allow_html=True,
        )

# 하단 - 방 온도 진단 및 에티켓
st.markdown("<br>", unsafe_allow_html=True)

c_bot1, c_bot2 = st.columns(2)

with c_bot1:
    st.markdown(
        """
    <div class="comic-card">
        <h4>🌡️ 우리집 실내 온도 적합성 테스트</h4>
        <p>현재 내 방 온도를 설정하고 파충류 적합성을 진단해보세요.</p>
    """,
        unsafe_allow_html=True,
    )

    user_temp = st.slider("현재 내 방 온도 (°C)", 15, 38, 24)

    if st.button("🔥 적합도 테스트 실행"):
        if "크레스티드" in selected_name:
            if user_temp > 27:
                st.error(
                    "🚨 경고! 방 온도가 너무 높습니다! 크레스티드 게코는 28°C 이상 노출 시 치명적입니다."
                )
            elif 20 <= user_temp <= 26:
                st.success(
                    "✅ 최고입니다! 크레스티드 게코가 살기에 가장 완벽한 온도입니다!"
                )
            else:
                st.warning("⚠️ 조금 서늘하네요! 22°C 이상을 유지해주세요.")
        else:
            st.info(
                f"✅ 현재 설정된 온도({user_temp}°C)에 맞추어 온열 장판이나 스팟 램프 조절을 통해 환경을 맞춰주세요."
            )

    st.markdown("</div>", unsafe_allow_html=True)

with c_bot2:
    st.markdown(
        """
    <div class="comic-card">
        <h4>📌 필수 파충류 집사 수칙</h4>
        <ul style="line-height: 1.9; padding-left: 20px;">
            <li>만지기 전후로 반드시 따뜻한 물과 비누로 손을 씻어주세요.</li>
            <li>과도한 스킨십은 스트레스를 유발하므로 적절히 조절해주세요.</li>
            <li>갑자기 먹이를 거부할 때는 사육장 온도와 습도를 최우선으로 점검하세요.</li>
        </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

# 하단 풋터
st.divider()
st.markdown(
    """
<div style="text-align: center; color: #000000; font-weight: bold; font-size: 14px;">
    🐊 Reptile Encyclopedia White Edition | 10종 대용량 파충류 백과사전 가이드 🦎
</div>
""",
    unsafe_allow_html=True,
)
