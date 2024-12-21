import streamlit as st

questions = [
    "하루 대부분 기분이 가라앉거나 우울하거나 희망이 없다고 느꼈다.",
    "평소에 즐기던 활동들에 흥미나 즐거움이 줄었다.",
    "잠들기 어렵거나 자주 깨거나 너무 많이 잤다.",
    "피로감이나 에너지가 부족했다.",
    "식욕이 줄었거나 과식했다.",
    "자신이 실패자라고 느꼈거나 자신이나 가족을 실망시켰다고 느꼈다.",
    "집중하는 데 어려움을 겪었다 (예: 신문 읽기나 TV 보기).",
    "다른 사람들이 알아차릴 정도로 너무 느리게 움직이거나 초조하게 움직였다.",
    "자신을 해치거나 죽는 것을 생각했다.",
]

st.title("우울증 자가 진단 설문지")

st.write("지난 2주 동안 각 항목에 대해 얼마나 자주 경험했는지 선택해 주세요.")
scores = []
for i, question in enumerate(questions):
    score = st.radio(
        f"{i+1}. {question}",
        options=["전혀 아님 (0점)", "며칠 있음 (1점)", "절반 이상 (2점)", "거의 매일 (3점)"],
        index=0,
        key=f"q{i}"
    )
    scores.append(int(score.split("(")[1][0]))

if st.button("결과 확인"):
    total_score = sum(scores)
    st.subheader(f"총점: {total_score}/27")

    if total_score <= 4:
        st.write("**결과:** 최소 우울 증상")
    elif 5 <= total_score <= 9:
        st.write("**결과:** 경미한 우울 증상")
    elif 10 <= total_score <= 14:
        st.write("**결과:** 중등도 우울 증상 → 상담 권장")
    elif 15 <= total_score <= 19:
        st.write("**결과:** 중증 우울 증상 → 전문가의 도움 필요")
    else:
        st.write("**결과:** 매우 중증 우울 증상 → 즉각적인 도움 필요")
