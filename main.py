import streamlit as st

# 1. 페이지 기본 설정 및 디자인 스타일 적용
st.set_page_config(
    page_title="🦎 파충류 사육 대백과사전 (Reptile Encyclopedia)",
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
        font-size: 16px;
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

# 2. 파충류 10종 대용량 백과사전 데이터베이스
REPTILE_DB = {
    "크레스티드 게코": {
        "category": "붙붙이 도마뱀",
        "en_name": "Crested Gecko",
        "scientific_name": "Correlophus ciliatus",
        "icon": "🦎",
        "difficulty": "초급 (입문용 추천)",
        "difficulty_badge": "badge-easy",
        "price": "5만 ~ 25만원 (모프별 수백만원 이상)",
        "temp": "주간 22°C - 26°C / 야간 20°C - 23°C",
        "humidity": "60% - 80% (환기 후 건조 주기 필요)",
        "size": "성체 기준 20cm - 25cm (몸통 10~12cm)",
        "lifespan": "15년 - 20년 이상",
        "diet_type": "잡식성 (슈퍼푸드 사료 및 곤충)",
        "cage_size": "적소 30x30x45cm 이상 (세로형 사육장)",
        "summary": "1994년 재발견된 뉴칼레도니아 원산의 야행성 붙붙이 게코입니다. 속눈썹 모양의 돌기가 특징이며, 살아있는 곤충 없이 인공 사료만으로 육성이 가능하여 입문 파충류 1위로 꼽힙니다.",
        "origin": "뉴칼레도니아 남부 열대 우림 (수목성 생활)",
        "morphs": "노멀, 릴리화이트, 플레임, 헐리퀸, 핀스트라이프, 아잔틱 등",
        "env_detail": """
        #### 🏠 세부 사육장 환경 세팅
        - **사육장 유형**: 세로로 높은 **높이형 사육장**(유리, 아크릴, 적재형 케이지)을 사용합니다.
        - **바닥재**: 청결 관리를 위해 **키친타올**이나 **파충류 매트**를 추천하며, 자연주의 세팅 시 코코피트/에코어스를 활용합니다.
        - **구조물 및 은신처**: 나무를 타는 습성이 강하므로 **코르크 보드, 인조 덩굴, 백스크린, 코코넛 은신처**를 빽빽하게 배치해 활동 공간과 숨을 곳을 만들어줍니다.
        - **온도 관리**: **고온에 매우 취약**합니다. 28°C를 넘어가면 스트레스를 받고 치명적일 수 있으므로 여름철에는 쿨링팬이나 에어컨 조절이 필수입니다. 별도의 고온 열원은 필요하지 않습니다.
        - **습도 및 분무**: 매일 저녁 사육장 벽면에 무지무라/미스트로 분무하여 습도를 높여주고, 낮 동안에는 살짝 마르는 건습 주기를 형성해야 곰팡이를 예방할 수 있습니다.
        """,
        "diet_detail": """
        #### 🥗 식단 및 영양 공급 가이드
        - **주식**: 크레스티드 게코 전용 **슈퍼푸드**(판게아, 레파시, 쿠키스 등)를 케첩 정도의 농도로 물과 1:2 비율로 개어 급여합니다.
        - **급여 주기**: 
          - **베이비/유체**: 주 3~4회 (격일 급여)
          - **성체**: 주 2~3회
        - **특식/생먹이**: 주 1회 칼슘이 첨가된 귀뚜라미나 밀웜을 급여하면 성장 속도와 근육 발달에 도움이 됩니다.
        - **영양제**: 슈퍼푸드에 기본 영양소가 들어있으나, 생먹이 급여 시에는 **비타민 D3 포함 칼슘 파우더**를 더스팅하여 지급합니다.
        """,
        "health_detail": """
        #### 🩺 건강 관리 및 주요 질병
        - **꼬리 자름(Autotomy)**: 위협을 느끼거나 꼬리가 잡히면 자르고 도망칩니다. 자란 꼬리는 재생되지 않고 작은 방울(패브) 모양으로 남으므로 꼬리를 강제로 잡지 마세요.
        - **MBD (대사성 뼈 질환)**: 칼슘과 비타민 D3 결핍 시 뼈가 무르고 척추/턱이 휨. 균형 잡힌 슈퍼푸드 공급이 중요합니다.
        - **탈피 부전**: 습도가 너무 낮으면 손가락이나 꼬리 끝에 탈피 껍질이 남습니다. 온수 부드러운 족욕으로 제거해 주어야 손가락 괴사를 막을 수 있습니다.
        """,
        "behavior_tips": [
            "야행성이므로 낮에는 코르크 보드 뒤나 잎사귀 사이에 숨어 잠을 자고 저녁에 활동합니다.",
            "점프력이 뛰어나므로 핸들링 시 손에서 손으로 이동하도록 '계단 타기' 방식을 활용하세요.",
            "벽면에 매달려 핥아 먹는 습성이 있으므로 물그릇 외에도 벽면 분무가 중요합니다."
        ]
    },
    "레오파드 게코": {
        "category": "지상성 게코",
        "en_name": "Leopard Gecko",
        "scientific_name": "Eublepharis macularius",
        "icon": "🐆",
        "difficulty": "초급 (입문용 추천)",
        "difficulty_badge": "badge-easy",
        "price": "4만 ~ 15만원 (노멀/인기 모프 기준)",
        "temp": "핫존 30°C - 32°C / 쿨존 24°C - 26°C",
        "humidity": "30% - 40% (건조, 습식 은신처 제공)",
        "size": "성체 기준 20cm - 28cm",
        "lifespan": "15년 - 20년 이상",
        "diet_type": "완전 육식성 (생먹이 필수)",
        "cage_size": "45x30x30cm 이상 (가로형 사육장)",
        "summary": "파키스탄, 아프가니스탄의 건조한 지대 원산으로 표범 무늬와 통통한 꼬리가 매력적인 지상성 도마뱀입니다. 순한 성격과 눈꺼풀이 있어 눈을 감는 모습이 귀엽습니다.",
        "origin": "중동 및 아시아 건조 사막/암석지대",
        "morphs": "하이옐로우, 탠저린, 맥스노우, 블레이징 블리자드, 이클립스 등",
        "env_detail": """
        #### 🏠 세부 사육장 환경 세팅
        - **사육장 유형**: 바닥을 넓게 쓰는 **가로형 사육장**(2자 케이지 추천)을 사용합니다.
        - **열원(하부 열원 필수)**: 야행성이며 복부 온열을 통해 소화를 시키므로, 사육장 바닥의 1/3 부분에 **필름 히터/하부 장판**을 설치하여 핫존(30~32°C)을 형성해야 합니다.
        - **은신처 세팅**: 최소 2개의 은신처가 필요합니다. 
          1. 핫존 근처의 **건식 은신처**
          2. 탈피를 돕기 위한 **습식 은신처**(습한 이끼나 젖은 키친타올을 넣은 용기)
        - **바닥재**: 임팩션(장막힘) 위험을 방지하기 위해 **키친타올, 파충류 전용 매트**를 권장하며 소화 불가능한 샌드는 사용을 자제하세요.
        """,
        "diet_detail": """
        #### 🥗 식단 및 영양 공급 가이드
        - **주식**: 살아있는 **귀뚜라미, 밀웜, 듀비아 로치**. (죽은 먹이는 잘 먹지 않음)
        - **급여 방법**: 먹이용 곤충에 반드시 **D3 함유 칼슘 파우더**를 묻혀서(더스팅) 핀셋으로 급여합니다.
        - **급여 주기**:
          - **베이비**: 매일 소형 곤충 3~5마리
          - **아성체/성체**: 2~3일에 1회 곤충 4~6마리
        - **물 공급**: 깨끗한 얕은 물그릇을 쿨존에 항시 비치합니다.
        """,
        "health_detail": """
        #### 🩺 건강 관리 및 주요 질병
        - **꼬리 영양 상태**: 통통하고 두꺼운 꼬리가 건강의 상징입니다. 꼬리가 얇아지면 거식이나 거식성 기생충 감염을 의심해야 합니다.
        - **임팩션 (장막힘)**: 바닥재(모래)나 너무 큰 먹이를 삼켜 장이 막히는 현상. 적절한 바닥재 사용이 예방책입니다.
        - **에그 바인딩 (유란 증후군)**: 무정란을 배란했으나 배출하지 못하는 증상. 산란 환경(습한 흙) 세팅이 요구됩니다.
        """,
        "behavior_tips": [
            "느릿느릿 움직이고 온순하지만 갑자기 놀라 떨어질 수 있으므로 낮게 잡으세요.",
            "배변 장소를 한곳으로 정하는 습성이 있어 청소가 매우 편리합니다.",
            "핸들링은 아이가 안정감을 느끼도록 밑에서 손을 받쳐 들어 올려주세요."
        ]
    },
    "비어디 드래곤": {
        "category": "주행성 도마뱀",
        "en_name": "Bearded Dragon",
        "scientific_name": "Pogona vitticeps",
        "icon": "🐉",
        "difficulty": "중급 (대형 사육장 필요)",
        "difficulty_badge": "badge-medium",
        "price": "10만 ~ 35만원 (하이포, 트랜스 모프 등)",
        "temp": "바스킹존 38°C - 42°C / 쿨존 26°C - 28°C",
        "humidity": "30% - 40% (주간 건조 유지)",
        "size": "성체 기준 45cm - 60cm",
        "lifespan": "10년 - 15년",
        "diet_type": "잡식성 (성장 단계에 따라 비율 변경)",
        "cage_size": "120x60x60cm (4자 대형 원목/포맥스 사육장 필수)",
        "summary": "호주 사막 원산으로 턱 밑의 가시 모양 주름이 마치 용을 닮은 주행성 도마뱀입니다. 주인과의 교감이 매우 뛰어나고 순하지만 대형 사육장과 강력한 조명 세팅이 필요합니다.",
        "origin": "호주 내륙 사막 및 건조한 숲 지대",
        "morphs": "노멀, 하이포, 트랜스, 제로, 위블리, 레더백 등",
        "env_detail": """
        #### 🏠 세부 사육장 환경 세팅
        - **사육장 규격**: 성체 기준 최소 **3자(90cm) ~ 4자(120cm)** 이상의 가로형 대형 사육장이 필수입니다.
        - **조명 세팅 (가장 중요)**: 
          1. **스팟 램프**: 체온 유지를 위해 일광욕장(바스킹존)을 40°C 내외로 유지합니다.
          2. **UVB 램프 (T5 고출력 추천)**: 비타민 D3 합성 및 칼슘 흡수를 위해 매일 10~12시간 조사해야 합니다.
        - **바닥재**: 파충류 매트, 타일, 바크, 혹은 사막 샌드(성체 전용).
        - **구조물**: 바스킹 램프 아래에 오를 수 있는 대형 유목이나 평평한 바위를 놓아줍니다.
        """,
        "diet_detail": """
        #### 🥗 식단 및 영양 공급 가이드
        - **성장 단계별 먹이 비율**:
          - **베이비/유체 (1~6개월)**: 곤충 70% + 야채 30% (매일 곤충 급여)
          - **아성체 (6~12개월)**: 곤충 50% + 야채 50%
          - **성체 (12개월 이상)**: **야채 70% + 곤충 30%** (비만 방지 및 건강을 위해 채식 위주)
        - **추천 야채**: 치커리, 청경채, 단호박, 애호박, 다공채 (시금치/방울토마토는 급여 금지).
        - **영양제**: 생먹이에 D3 포함 칼슘제를 주기적으로 더스팅합니다.
        """,
        "health_detail": """
        #### 🩺 건강 관리 및 주요 질병
        - **MBD**: UVB 조명 부족 시 뼈가 약해지고 다리를 떪. UVB 램프는 6~12개월마다 교체해야 합니다.
        - **황색균 질환 (CANV)**: 피부에 노란 균이 침투하는 전염성 질환으로 사육장 위생 관리가 최우선입니다.
        - **온수욕 (족욕)**: 미지근한 물에 15분 정도 족욕을 시켜주면 수분 보충, 탈피 완화, 배변 유도에 효과적입니다.
        """,
        "behavior_tips": [
            "위협을 느끼거나 기분이 상하면 턱을 검게 부풀리고 입을 벌립니다.",
            "팔을 동그랗게 돌리는 '암 웨이빙(Arm Waving)'은 서복과 인사의 신호입니다.",
            "머리를 위아래로 흔드는 '헤드 뱅잉'은 영역 주장 및 구애의 표시입니다."
        ]
    },
    "콘스네이크": {
        "category": "뱀 (뱀목 뱀과)",
        "en_name": "Corn Snake",
        "scientific_name": "Pantherophis guttatus",
        "icon": "🐍",
        "difficulty": "초급 (뱀 입문 1순위)",
        "difficulty_badge": "badge-easy",
        "price": "8만 ~ 20만원 (일반 모프)",
        "temp": "핫존 28°C - 30°C / 쿨존 24°C - 26°C",
        "humidity": "40% - 50% (탈피 시 60~70%)",
        "size": "성체 기준 120cm - 150cm (몸통이 슬림함)",
        "lifespan": "15년 - 20년",
        "diet_type": "육식성 (해동 냉동 쥐)",
        "cage_size": "90x45x45cm (3자 케이지 권장)",
        "summary": "북미 원산의 독이 없는 옥수수밭 뱀으로, 화려한 색상과 온순한 성격, 강인한 생명력을 가져 애완 뱀 입문으로 가장 많은 사랑을 받고 있습니다.",
        "origin": "미국 동부 및 중부 초원, 숲, 농경지",
        "morphs": "애멜라니스틱, 아네리, 스노우, 팔메토, 테세라, 캔디케인 등",
        "env_detail": """
        #### 🏠 세부 사육장 환경 세팅
        - **탈출 방지 (최우선)**: 뱀은 미세한 틈으로도 몸을 구겨 탈출하므로 **잠금장치가 완벽한 케이지**가 필수입니다.
        - **열원**: 사육장 하부 1/3 영역에 **필름 히터/열선**을 깔아 소화를 돕는 핫존(29°C)을 조성합니다.
        - **바닥재**: 아스펜 쉐이빙(뱀 전용 대팻밥), 파충류 매트, 키친타올.
        - **은신처 및 물그릇**: 몸이 꼭 맞는 은신처 2개와 몸을 완전히 담글 수 있는 넉넉한 무게감 있는 물그릇을 제공합니다.
        """,
        "diet_detail": """
        #### 🥗 식단 및 영양 공급 가이드
        - **주식**: 냉동 쥐(핑키 -> 핑키M -> 핑키L -> 퍼지 -> 호퍼 -> 성체 쥐 순으로 뱀 두께에 맞추어 상향).
        - **급여 가이드**:
          1. 냉동 쥐를 40°C 미지근한 물에 완전히 해동합니다. (속까지 따뜻해야 소화 불량을 방지함)
          2. 핀셋으로 쥐를 잡아 움직이는 것처럼 흔들어 급여합니다.
        - **급여 주기**: 베이비(5~7일에 1회) / 성체(10~14일에 1회).
        """,
        "health_detail": """
        #### 🩺 건강 관리 및 주요 질병
        - **거식 및 토함 (Regurgitation)**: 차가운 상태의 먹이 급여, 온도 미달, 먹은 후 핸들링 시 먹이를 토해냅니다. 토한 후에는 최소 2주간 휴식을 취해야 위장관이 회복됩니다.
        - **블루 현상 (Blue Phase)**: 탈피 직전 눈이 푸르스름하게 변하고 몸이 탁해집니다. 이때는 시야가 가려져 예민하므로 먹이 급여와 핸들링을 중단하고 습도를 높여주세요.
        """,
        "behavior_tips": [
            "먹이를 먹은 후 최소 48시간(2~3일) 동안은 절대로 핸들링하지 마세요.",
            "나무 타는 것도 좋아하므로 유목을 넣어주면 꼬아서 올라가는 모습을 관찰할 수 있습니다."
        ]
    },
    "볼파이톤": {
        "category": "뱀 (보아/비단뱀과)",
        "en_name": "Ball Python",
        "scientific_name": "Python regius",
        "icon": "🐍",
        "difficulty": "초중급",
        "difficulty_badge": "badge-medium",
        "price": "10만 ~ 35만원 (콤보 모프는 수백만원)",
        "temp": "핫존 31°C - 33°C / 쿨존 26°C - 27°C",
        "humidity": "50% - 60% (탈피 시 70% 이상)",
        "size": "성체 기준 120cm - 150cm (몸집이 매우 두껍고 통통함)",
        "lifespan": "20년 - 30년 이상",
        "diet_type": "육식성 (해동 냉동 쥐/라트)",
        "cage_size": "90x45x45cm 이상",
        "summary": "중서부 아프리카 원산의 소형 비단뱀입니다. 위협을 느끼면 머리를 안으로 감싸 공(Ball)처럼 둥글게 몸을 마는 습성에서 이름이 유래했습니다. 대단히 순합니다.",
        "origin": "중서부 아프리카 열대 우림 및 초원",
        "morphs": "파스텔, 스파이더, 피에드, 모하비, 클라운, 바나나 등",
        "env_detail": """
        #### 🏠 세부 사육장 환경 세팅
        - **사육장 환경**: 야행성 습성이 강하고 어두운 공간을 선호하므로, 상단이 열린 유리장보다는 **아크릴/포맥스 렉사육장**에서 안정감을 느낍니다.
        - **온 습도 세팅**: 열대 습윤 환경이 필요하므로 바닥 열원(핫존 32°C)과 함께 바크/코코칩 바닥재를 분무하여 높은 습도를 유지해야 탈피부전을 예방합니다.
        - **은신처**: 입구가 좁고 몸이 꽉 차는 어두운 은신처를 매우 좋아합니다.
        """,
        "diet_detail": """
        #### 🥗 식단 및 영양 공급 가이드
        - **주식**: 냉동 쥐(마우스) 및 라트(소형 쥐).
        - **급여 방법**: 체온 측정기 기준 38~40°C 정도로 따뜻하게 해동한 쥐를 핀셋으로 제공합니다.
        - **거식 주의**: 볼파이톤은 환경 변화, 계절 변화(겨울철), 번식기 등에 **몇 달간 먹이를 거부하는 거식 현상**이 흔하게 발생합니다. 체중 감소가 급격하지 않다면 조급해하지 말고 온습도를 재점검해야 합니다.
        """,
        "health_detail": """
        #### 🩺 건강 관리 및 주요 질병
        - **호흡기 질환 (RI)**: 사육장 온도가 낮고 습도가 과도할 경우 감기에 걸려 거품 침을 흘리거나 쉭쉭 소리를 냅니다. 핫존 온도를 올려주어야 합니다.
        - **스케일 로트 (비늘 부패)**: 바닥재가 축축하게 젖어있으면 배쪽 비늘에 세균 감염이 발생하므로 바닥재 위생이 중요합니다.
        """,
        "behavior_tips": [
            "물 가능성이 파충류 중 가장 낮을 정도로 순하고 겁이 많습니다.",
            "핸들링 시 천천히 몸 전체를 받쳐주면 팔에 부드럽게 감겨 안정을 취합니다."
        ]
    },
    "동부 호스필드 육지거북": {
        "category": "육지거북",
        "en_name": "Russian Tortoise / Horsfield's Tortoise",
        "scientific_name": "Testudo horsfieldii",
        "icon": "🐢",
        "difficulty": "초중급 (육지거북 입문 추천)",
        "difficulty_badge": "badge-medium",
        "price": "12만 ~ 25만원",
        "temp": "바스킹존 32°C - 35°C / 쿨존 24°C - 26°C",
        "humidity": "40% - 50%",
        "size": "성체 기준 15cm - 22cm (소형 육지거북)",
        "lifespan": "30년 - 50년 이상",
        "diet_type": "100% 완전 초식성 (야채 및 건초)",
        "cage_size": "90x60cm 이상 (넓은 원목 사육장)",
        "summary": "중앙아시아의 건조한 지대 출신으로, 육지거북 중 성체 크기가 작아 가정에서 키우기 가장 적합한 종입니다. 활동성이 높고 굴을 파는 습성이 강합니다.",
        "origin": "중앙아시아 건조한 건조 지대, 건조한 건초지",
        "morphs": "노멀, 고스포드 등",
        "env_detail": """
        #### 🏠 세부 사육장 환경 세팅
        - **사육장 구조**: 오픈형 원목 사육장이나 대형 리빙박스를 활용합니다.
        - **조명 세팅**: 주행성 육지거북이므로 **UVB 램프와 스팟 램프**를 필수 배치해야 갑각(껍질)이 형성됩니다.
        - **바닥재**: 버로우(땅파기) 습성을 만족시키기 위해 코코칩, 코코피트, 또는 황토흙을 5~10cm 두께로 두껍게 깔아줍니다.
        """,
        "diet_detail": """
        #### 🥗 식단 및 영양 공급 가이드
        - **주식**: 섬유질이 풍부하고 칼슘 대 인 비율이 높은 야채.
          - **추천 식단**: 치커리, 청경채, 잇몸채, 로메인, 멀베리(뽕잎), 민들레, 몬스테라, 건초 파우더.
          - **금지 식단**: 과일(배탈 유발), 배추/시금치(옥살산 성분으로 칼슘 흡수 방해).
        - **영양제**: 매일 제공하는 야채에 육지거북 전용 **칼슘제 및 종합비타민**을 뿌려줍니다.
        """,
        "health_detail": """
        #### 🩺 건강 관리 및 주요 질병
        - **피라미딩 (등갑 변형)**: 습도 부족, 과도한 단백질 섭취, UVB 부족 시 등갑이 뾰족하게 솟아오르는 현상. 적절한 습도와 초식 식단 유지가 핵심입니다.
        - **온수욕**: 주 2~3회 30°C 정도의 따뜻한 물에 15~20분간 온수욕을 시켜 신진대사를 촉진하고 요산 배출을 돕습니다.
        """,
        "behavior_tips": [
            "구석을 파고 들어가는 습성이 강해 은신처를 단단히 고정해주어야 합니다.",
            "낮 동안 조명 아래에서 일광욕을 즐기는 모습을 자주 관찰할 수 있습니다."
        ]
    },
    "사바나 모니터": {
        "category": "왕도마뱀 (모니터)",
        "en_name": "Savannah Monitor",
        "scientific_name": "Varanus exanthematicus",
        "icon": "🐊",
        "difficulty": "중상급 (대형종, 전문 공간 필요)",
        "difficulty_badge": "badge-hard",
        "price": "8만 ~ 20만원 (개체가는 저렴하나 용품비 높음)",
        "temp": "바스킹존 45°C - 50°C / 쿨존 26°C - 28°C",
        "humidity": "40% - 60%",
        "size": "성체 기준 80cm - 120cm (대형 파충류)",
        "lifespan": "10년 - 15년",
        "diet_type": "완전 육식성 (곤충, 설치류)",
        "cage_size": "150x75x75cm 이상 (대형 초대형 사육장)",
        "summary": "아프리카 초원 지대에 서식하는 소형 공룡 느낌의 왕도마뱀입니다. 분양가는 저렴하지만 대형으로 성장하므로 초대형 사육 환경과 강력한 바스킹 조명이 필요합니다.",
        "origin": "sub-Saharan 아프리카 초원 및 사바나 지대",
        "morphs": "노멀",
        "env_detail": """
        #### 🏠 세부 사육장 환경 세팅
        - **초대형 공간**: 성체가 되면 방 한 칸을 내주거나 주문 제작 대형 케이지가 필요합니다.
        - **고온 바스킹 zone**: 왕도마뱀류는 소화율을 높이기 위해 일광욕 스팟 존을 **45°C 이상**의 고온으로 올려주어야 소화가 가능합니다.
        - **두꺼운 바닥재**: 버로우 습성이 있어 흙/바크 혼합 바닥재를 두껍게 깔아주어야 스트레스를 받지 않습니다.
        """,
        "diet_detail": """
        #### 🥗 식단 및 영양 공급 가이드
        - **유체 식단**: 귀뚜라미, 듀비아 로치, 대형 밀웜 등 곤충 위주.
        - **성체 식단**: 곤충, 냉동 쥐, 메추리, 닭 가슴살.
        - **주의사항 (비만 위험)**: 사육 상태에서는 활동량이 적어 비만에 걸리기 쉽습니다. fatty한 지방 위주 식단(쥐)을 과도하게 주면 간부전으로 사망할 수 있으므로 곤충 비중을 높여주세요.
        """,
        "health_detail": """
        #### 🩺 건강 관리 및 주요 질병
        - **지방간 및 비만**: 모니터 사육의 가장 큰 적입니다. 몸집이 둔해지지 않게 식단 조절과 활동 공간 확보가 필수적입니다.
        - **길들이기 (테이밍)**: 어릴 때부터 오랫동안 꾸준히 핸들링하지 않으면 성체가 되어 날카로운 이빨과 꼬리치기로 공격할 수 있습니다.
        """,
        "behavior_tips": [
            "혀를 길게 낼름거리며 냄새로 주변 사물을 탐색합니다.",
            "주인에게 잘 길들여지면 개처럼 따라다니는 '개마뱀'이 될 수 있습니다."
        ]
    },
    "무어리시 게코": {
        "category": "벽면 부착성 게코",
        "en_name": "Moorish Gecko / Crocodile Gecko",
        "scientific_name": "Tarentola mauritanica",
        "icon": "🦎",
        "difficulty": "초급 (관상용 추천)",
        "difficulty_badge": "badge-easy",
        "price": "3만 ~ 7만원",
        "temp": "주간 26°C - 30°C / 야간 20°C - 22°C",
        "humidity": "40% - 50%",
        "size": "성체 기준 12cm - 15cm (소형)",
        "lifespan": "10년 - 15년",
        "diet_type": "육식성 (소형 곤충)",
        "cage_size": "30x30x30cm (소형 케이지)",
        "summary": "지중해 연안 원산의 소형 게코입니다. 등 비늘이 악어처럼 입체적으로 돋아있어 '크로커다일 게코'라고도 불립니다. 가격이 저렴하고 튼튼하여 입문용 관상 도마뱀으로 좋습니다.",
        "origin": "지중해 연안 국가 (남유럽, 북아프리카)",
        "morphs": "노멀",
        "env_detail": """
        #### 🏠 세부 사육장 환경 세팅
        - **입체적 공간**: 유리 벽면과 바위를 매우 잘 타므로 **코르크 보드 백스크린**이나 입체 구조물을 벽면에 붙여주는 것이 좋습니다.
        - **조명**: 소형 UVB 램프나 소형 스팟 램프를 낮 동안 켜주면 활발하게 움직입니다.
        """,
        "diet_detail": """
        #### 🥗 식단 및 영양 공급 가이드
        - **주식**: 소형 귀뚜라미, 밀웜.
        - **영양제**: 칼슘 파우더를 2회에 1회꼴로 생먹이에 더스팅하여 급여.
        """,
        "health_detail": """
        #### 🩺 건강 관리 및 주요 질병
        - **야생 채집 개체(WC) 주의**: 분양 시 WC 개체일 확률이 있으므로 외부 기생충 유무를 점검해야 합니다.
        """,
        "behavior_tips": [
            "움직임이 매우 빠르고 경계심이 많으므로 손으로 만지는 핸들링보다는 관상 위주 사육을 권장합니다."
        ]
    },
    "베일드 카멜레온": {
        "category": "카멜레온",
        "en_name": "Veiled Chameleon",
        "scientific_name": "Chamaeleo calyptratus",
        "icon": "🦎",
        "difficulty": "상급 (섬세한 사육 필요)",
        "difficulty_badge": "badge-hard",
        "price": "10만 ~ 25만원",
        "temp": "주간 25°C - 28°C (바스킹존 33°C) / 야간 20°C",
        "humidity": "50% - 70% (높은 환기율 필수)",
        "size": "성체 기준 35cm - 55cm",
        "lifespan": "5년 - 8년",
        "diet_type": "육식성 (곤충 및 소량의 잎)",
        "cage_size": "60x60x120cm (망/메쉬 사육장 필수)",
        "summary": "머리 위 높은 투구(Crest)와 신비로운 몸색 변화, 독립적으로 움직이는 두 눈이 특징입니다. 환기가 되지 않으면 안구 질환이나 호흡기 질환에 걸리기 쉬워 난이도가 높습니다.",
        "origin": "예멘 및 사우디아라비아 산악 지대",
        "morphs": "노멀, 트랜스, 피볼드 등",
        "env_detail": """
        #### 🏠 세부 사육장 환경 세팅
        - **망(Mesh) 사육장 필수**: 밀폐된 유리 사육장에서는 공기 순환이 안 되어 치명적입니다. **전면 망 사육장**을 사용해야 합니다.
        - **수분 공급 (드립 시스템)**: 고여있는 물그릇의 물을 인식하지 못합니다. 나뭇잎에 떨어지는 물방울을 인식하므로 **드립 시스템**이나 자동 미스팅기를 설치해야 합니다.
        - **식물 세팅**: 벤자민, 스킨답서스 같은 생화 식물을 넣어주면 습도 유지 및 수분 공급에 도움이 됩니다.
        """,
        "diet_detail": """
        #### 🥗 식단 및 영양 공급 가이드
        - **주식**: 살아있는 귀뚜라미, 왁스웜, 밀웜.
        - **영양제**: 비타민 D3 포함 칼슘 파우더와 종합비타민을 번갈아 더스팅합니다.
        """,
        "health_detail": """
        #### 🩺 건강 관리 및 주요 질병
        - **안구 질환**: 환기 부족이나 수분 결핍 시 눈을 감고 뜨지 못함.
        - **MBD**: 성장 속도가 빨라 칼슘과 UVB 조명이 부족하면 뼈가 쉽게 굽습니다.
        """,
        "behavior_tips": [
            "독립성이 강해 한 사육장에 두 마리 이상을 함께 두면 심각하게 싸웁니다 (1케이지 1개체 필수).",
            "스트레스에 취약하므로 과도한 핸들링을 피해야 합니다."
        ]
    },
    "푸른혀 도마뱀": {
        "category": "지상성 스킨크",
        "en_name": "Blue-tongued Skink",
        "scientific_name": "Tiliqua scincoides",
        "icon": "👅",
        "difficulty": "중급",
        "difficulty_badge": "badge-medium",
        "price": "25만 ~ 50만원 (인도네시아, 세람, 지부티 등)",
        "temp": "바스킹존 35°C - 38°C / 쿨존 24°C - 26°C",
        "humidity": "40% - 70% (아종별 차이 존재)",
        "size": "성체 기준 40cm - 60cm",
        "lifespan": "15년 - 20년 이상",
        "diet_type": "완전 잡식성 (무엇이든 잘 먹음)",
        "cage_size": "120x60x45cm (넓은 가로형)",
        "summary": "호주 및 인도네시아 원산의 대형 스킨크입니다. 천적에게 위협을 줄 때 내미는 선명한 파란색 혀가 가장 큰 특징이며 튼튼하고 잡식성이라 먹이 관리가 재미있습니다.",
        "origin": "호주 및 인도네시아 열대/건조 지대",
        "morphs": "인도네시아, 이리안자야, 세람, 인자이 등",
        "env_detail": """
        #### 🏠 세부 사육장 환경 세팅
        - **가로형 사육장**: 몸이 길고 바닥 생활을 하므로 4자 이상의 가로형 사육장이 필요합니다.
        - **바닥재**: 파고드는 버로우 습성이 있어 바크나 코코칩을 두껍게 깔아주세요.
        - **조명**: UVB 램프와 일광욕용 바스킹 램프 세팅 필수.
        """,
        "diet_detail": """
        #### 🥗 식단 및 영양 공급 가이드
        - **잡식 비율**: **단백질(50%) + 야채(40%) + 과일(10%)**
        - **먹이 종류**: 강아지/고양이 프리미엄 습식 사료, 귀뚜라미, 계란 노른자, 청경채, 사과, 바나나 등.
        """,
        "health_detail": """
        #### 🩺 건강 관리 및 주요 질병
        - **발가락 탈피 부전**: 발가락 비늘 탈피가 잘 안되면 괴사되어 떨어질 수 있으므로 탈피 시 습도를 높이고 확인해야 합니다.
        """,
        "behavior_tips": [
            "사람에게 온순하고 잘 적응하며 먹성을 자랑합니다.",
            "놀라면 몸을 부풀리고 푸른 혀를 내밀어 쉭쉭 소리를 냅니다."
        ]
    }
}

# 3. 사이드바 - 파충류 선택 및 필터
with st.sidebar:
    st.title("📚 파충류 사육 대백과")
    st.caption("희망하는 파충류를 선택하여 전문 사육 서적 수준의 세부 정보를 확인하세요.")
    
    selected_name = st.selectbox(
        "🦎 개체 종류 선택:",
        list(REPTILE_DB.keys())
    )
    
    st.divider()
    
    # 체크리스트
    st.subheader("🛠️ 사육 시작 전 필수 체크리스트")
    c1 = st.checkbox("개체에 맞는 사육장 규격 확보")
    c2 = st.checkbox("온/습도계 및 열원(장판/스팟) 준비")
    c3 = st.checkbox("UVB 및 바스킹 조명 (주행성 한정)")
    c4 = st.checkbox("전용 바닥재 및 은신처 2개 이상")
    c5 = st.checkbox("먹이(슈퍼푸드/곤충/쥐/야채) 및 칼슘제")
    c6 = st.checkbox("인근 파충류 전문 동물병원 위치 파악")
    
    checked_count = sum([c1, c2, c3, c4, c5, c6])
    st.progress(checked_count / 6)
    st.caption(f"준비도: {checked_count} / 6 항목 완료")

reptile = REPTILE_DB[selected_name]

# 4. 메인 화면 - 상단 요약 헤더
st.markdown(f"""
<div class="header-card">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <span class="{reptile['difficulty_badge']}">{reptile['difficulty']}</span>
            <span style="background-color: #334155; color: #f8fafc; padding: 4px 12px; border-radius: 20px; font-size: 14px; font-weight: bold; margin-left: 8px;">{reptile['category']}</span>
            <h1 style="margin: 10px 0 5px 0; color: #f8fafc; font-size: 36px;">{reptile['icon']} {selected_name}</h1>
            <p style="color: #94a3b8; font-style: italic; margin: 0;">{reptile['en_name']} (학명: {reptile['scientific_name']})</p>
        </div>
    </div>
    <hr style="border-color: #334155; margin: 15px 0;">
    <p style="font-size: 16px; line-height: 1.6; color: #cbd5e1; margin: 0;">{reptile['summary']}</p>
</div>
""", unsafe_allow_html=True)

# 메인 콘텐츠 컬럼 분할
col1, col2 = st.columns([1, 2.2])

with col1:
    st.markdown(f"""
    <div class="icon-box">
        <div style="font-size: 80px; margin-bottom: 5px;">{reptile['icon']}</div>
        <div style="font-size: 22px; font-weight: bold; color: #f8fafc;">{selected_name}</div>
        <div style="font-size: 13px; color: #94a3b8; margin-top: 2px;">{reptile['en_name']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📋 핵심 백과 데이터")
    
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
            <div class="stat-title">📏 성체 크기</div>
            <div class="stat-value">{reptile['size']}</div>
        </div>
        <div class="stat-card">
            <div class="stat-title">⏳ 평균 수명</div>
            <div class="stat-value">{reptile['lifespan']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.info(f"**🌍 야생 서식지**: {reptile['origin']}\n\n**🎨 주요 모프**: {reptile['morphs']}")

with col2:
    # 세부 백과사전 탭 구성
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 환경 & 세팅", "🥗 식단 & 영양", "🩺 건강 & 질병", "💡 행동 & 팁", "🌡️ 진단 도구"])
    
    with tab1:
        st.markdown(reptile["env_detail"])
        st.caption(f"**권장 사육장 규격**: {reptile['cage_size']}")

    with tab2:
        st.markdown(reptile["diet_detail"])

    with tab3:
        st.markdown(reptile["health_detail"])

    with tab4:
        st.subheader("💡 개체 행동 특성 및 사육 꿀팁")
        for i, tip in enumerate(reptile["behavior_tips"], 1):
            st.markdown(f"**{i}.** {tip}")

    with tab5:
        st.subheader("🌡️ 우리집 실내 환경 적합도 진단기")
        st.write("현재 거주 중인 방의 온도를 설정하여 이 파충류를 키우기에 적합한지 확인해보세요.")
        
        user_temp = st.slider("현재 실내 온도 (°C)", 15, 38, 24)
        
        if st.button("적합도 진단 실행"):
            if "크레스티드 게코" in selected_name:
                if user_temp > 27:
                    st.error("🚨 위험: 실내 온도가 너무 높습니다! 크레스티드 게코는 28°C 이상 시 고열로 사망 위험이 있습니다. 냉방 장치가 필요합니다.")
                elif 20 <= user_temp <= 26:
                    st.success("✅ 최적: 방 온도가 이 도마뱀에게 매우 완벽합니다.")
                else:
                    st.warning("⚠️ 주의: 온도가 조금 낮습니다. 22°C 이상을 유지해주세요.")
            elif "비어디" in selected_name or "모니터" in selected_name:
                st.info("💡 주행성 도마뱀/모니터는 방 온도 외에도 일광욕 스팟 램프가 필수적입니다.")
            else:
                st.success(f"✅ 현재 설정 온도 {user_temp}°C를 바탕으로 열원(하부 장판 또는 램프) 조절을 통해 환경을 맞춰주실 수 있습니다.")

st.divider()
st.caption("본 정보는 파충류 전문 수의학 자료 및 사육서를 기반으로 제작된 백과사전 가이드입니다.")
