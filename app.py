import streamlit as st
from interviewer import generate_question, evaluate_answer
import re

st.set_page_config(page_title="AI Interview Coach", page_icon="🎯")

st.title("🎯 AI Interview Coach")
st.write("Practice interviews with AI")

topic = st.selectbox("Select Topic", ["Java", "Python", "JavaScript"])

if "question" not in st.session_state:
    st.session_state.question = ""

# Generate Question
if st.button("Get Question") or st.button("Next Question"):
    st.session_state.question = generate_question(topic)

# Show Question
if st.session_state.question:
    st.write("### Question:")
    st.write(st.session_state.question)

    answer = st.text_area("Your Answer")

    # Submit Answer
    if st.button("Submit Answer"):
        if answer.strip() != "":
            result = evaluate_answer(st.session_state.question, answer)

            st.write("### Evaluation")

            # Extract score
            score_match = re.search(r'(\d+)/10', result)

            if score_match:
                score = int(score_match.group(1))
                st.progress(score / 10)
                st.write(f"⭐ Score: {score}/10")

            st.markdown(result)
        else:
            st.warning("Please enter your answer")