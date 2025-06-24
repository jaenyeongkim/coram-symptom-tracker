import streamlit as st

# Page config
st.set_page_config(page_title="코람 물리치료: 통증별 스트레칭 가이드", layout="centered")

# Bright UI styling
st.markdown(
    """
    <style>
    body {
        background-color: #f2f9ff;
        font-family: 'Arial', sans-serif;
        color: #222;
    }
    .title {
        color: #0055aa;
        font-size: 36px;
        font-weight: bold;
    }
    .subtitle {
        color: #2266cc;
        font-size: 22px;
        margin-bottom: 10px;
    }
    .stButton>button {
        background-color: #3399ff;
        color: white;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<div class="title">코람 물리치료: 통증별 스트레칭 가이드</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">증상을 선택하시면, 추천 스트레칭과 이미지 안내를 드립니다.</div>', unsafe_allow_html=True)

# Symptoms input
symptoms = st.multiselect(
    "어떤 증상이 있으신가요?",
    [
        "허리 통증",
        "무릎 통증",
        "엉덩이 뻣뻣함",
        "어깨 불편감",
        "균형 문제",
        "근육 약화",
        "관절 통증",
        "움직임 제한",
        "발 저림",
        "수술 후 통증"
    ]
)

# Stretch database
stretch_data = {
    "허리 통증": {
        "title": "무릎 당기기",
        "desc": "등을 대고 누운 상태에서 한쪽 무릎을 가슴 쪽으로 당깁니다.",
        "img": "https://www.spine-health.com/sites/default/files/styles/article_main_image/public/field/image/knee-to-chest-stretch.jpg"
    },
    "무릎 통증": {
        "title": "햄스트링 스트레칭",
        "desc": "다리를 쭉 펴고 앉아 발끝을 향해 상체를 숙입니다.",
        "img": "https://www.verywellfit.com/thmb/sUlvRAwXrsZtxgx3MBzC2Zq4_HA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/hamstring-stretch-56a0100e3df78cafdaa124fd.jpg"
    },
    "엉덩이 뻣뻣함": {
        "title": "비둘기 자세",
        "desc": "한쪽 다리를 앞에 구부리고 다른 다리는 뒤로 뻗습니다.",
        "img": "https://cdn.prod.openfit.com/uploads/2019/02/13104129/pigeon-pose-yoga.jpg"
    },
    "어깨 불편감": {
        "title": "어깨 회전 스트레칭",
        "desc": "팔을 양옆으로 뻗고 원을 그리듯 천천히 돌립니다.",
        "img": "https://www.spotebi.com/wp-content/uploads/2014/10/arm-circles-exercise-illustration.jpg"
    },
    "균형 문제": {
        "title": "한발 서기 연습",
        "desc": "벽을 짚고 한발로 10초간 균형을 잡습니다.",
        "img": "https://www.verywellfit.com/thmb/1M8vK3PgKiB5iv-BjiZsWqAqXAA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/one-leg-stand-56a00cdb3df78cafdaa11fce.jpg"
    },
    "근육 약화": {
        "title": "다리 들어올리기",
        "desc": "등을 대고 누운 상태에서 다리를 번갈아 들어 올립니다.",
        "img": "https://www.physio-pedia.com/images/thumb/2/28/Straight_leg_raise.jpg/600px-Straight_leg_raise.jpg"
    },
    "관절 통증": {
        "title": "가벼운 무릎 굽히기",
        "desc": "벽에 기대어 무릎을 조금만 굽혔다 펴기를 반복합니다.",
        "img": "https://i.pinimg.com/originals/96/88/e0/9688e077519052f9d185a5f4d56deee3.jpg"
    },
    "움직임 제한": {
        "title": "전신 스트레칭",
        "desc": "팔을 위로 올리고 몸통을 좌우로 천천히 움직입니다.",
        "img": "https://www.spotebi.com/wp-content/uploads/2014/10/side-reaches-exercise-illustration.jpg"
    },
    "발 저림": {
        "title": "발목 돌리기",
        "desc": "앉은 상태에서 발끝으로 원을 그리듯 돌립니다.",
        "img": "https://www.summitmedicalgroup.com/media/db/imagelibrary/exercises/ankle-circle-1.jpg"
    },
    "수술 후 통증": {
        "title": "부드러운 관절 움직임",
        "desc": "수술 부위 주변을 천천히 움직이며 통증 없는 범위 내에서 운동합니다.",
        "img": "https://www.verywellhealth.com/thmb/CG7Izv5v1YaMbY8bdz0mIlv48Uw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/knee-extension-exercise-5188803-01-588b66aa3df78caebc2e8b86.jpg"
    }
}

# Show recommendations
if symptoms:
    st.subheader("💡 추천 스트레칭 및 설명")
    for sym in symptoms:
        data = stretch_data.get(sym)
        if data:
            st.markdown(f"### 👉 {data['title']}")
            st.write(data["desc"])
            st.image(data["img"], caption=data["title"], use_column_width=True)
    st.markdown("---")
    st.info("※ 통증이 심하거나 불편함이 지속되면 전문가의 상담을 받으세요.")
else:
    st.info("먼저 증상을 선택해 주세요.")
