import streamlit as st

# Set page config
st.set_page_config(page_title="코람 물리치료 통증 완화 앱", layout="centered")

# Bright UI using custom HTML + Streamlit features
st.markdown(
    """
    <style>
    body {
        background-color: #f2f9ff;
        color: #222;
        font-family: 'Arial', sans-serif;
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
st.markdown('<div class="title">코람 물리치료 통증 완화 앱</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">증상을 선택하시면, 관련된 통증 완화 스트레칭을 안내해 드립니다.</div>', unsafe_allow_html=True)

# Symptoms in Korean
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

# Stretching suggestions
stretching_recommendations = []

if "허리 통증" in symptoms:
    stretching_recommendations.append("👉 **무릎 당기기** – 등을 대고 누운 상태에서 한쪽 무릎을 가슴 쪽으로 당깁니다.")
if "무릎 통증" in symptoms:
    stretching_recommendations.append("👉 **햄스트링 스트레칭** – 다리를 쭉 펴고 앉아 발끝을 향해 상체를 숙입니다.")
if "엉덩이 뻣뻣함" in symptoms:
    stretching_recommendations.append("👉 **비둘기 자세 (요가)** – 한쪽 다리를 구부리고 다른 쪽 다리는 뒤로 뻗습니다.")
if "어깨 불편감" in symptoms:
    stretching_recommendations.append("👉 **어깨 회전 스트레칭** – 팔을 양옆으로 뻗고 원을 그리듯 천천히 돌립니다.")
if "균형 문제" in symptoms:
    stretching_recommendations.append("👉 **한발 서기 연습** – 벽을 짚고 한발로 10초간 균형을 잡습니다.")
if "근육 약화" in symptoms:
    stretching_recommendations.append("👉 **다리 들어올리기** – 등을 대고 누운 상태에서 다리를 번갈아 들어 올립니다.")
if "관절 통증" in symptoms:
    stretching_recommendations.append("👉 **가벼운 무릎 굽히기** – 벽에 기대어 무릎을 조금만 굽혔다 펴기를 반복합니다.")
if "움직임 제한" in symptoms:
    stretching_recommendations.append("👉 **전신 스트레칭** – 팔을 위로 올리고 몸통을 좌우로 천천히 움직입니다.")
if "발 저림" in symptoms:
    stretching_recommendations.append("👉 **발목 돌리기** – 앉은 상태에서 발끝으로 원을 그리듯 돌립니다.")
if "수술 후 통증" in symptoms:
    stretching_recommendations.append("👉 **수술 부위 주변 근육 이완 운동** – 의사의 지시에 따라 부드럽게 움직입니다.")

# Output recommendations
if symptoms:
    st.subheader("💡 추천 스트레칭")
    for rec in stretching_recommendations:
        st.markdown(rec)
    st.markdown("---")
    st.info("※ 모든 운동은 무리하지 않게 진행하시고, 통증이 심할 경우 전문가와 상담하세요.")
else:
    st.info("위 증상 중 하나 이상을 선택해 주세요.")
