import streamlit as st
from utils.ollama_helper import get_ai_response
from utils.pdf_reader import extract_text_from_pdf
from utils.prompts import generate_notes_prompt
from utils.prompts import generate_pdf_prompt
from utils.pdf_reader import process_pdf, ask_pdf_question
# from utils.resume_analyzer import analyze_resumex
# from utils.resume_analyzer import extract_resume_text


st.set_page_config(page_title = "AI Powered Assistant", layout="wide", page_icon="🤖")
st.title("🤖AI Powered Assistant")

st.sidebar.title("📌 Features")

feature = st.sidebar.radio(
    "Choose a feature:",
    [
        "🤖 AI Chatbot",
        "📝 Notes Summarizer",
        "📄 PDF Q&A",
        "📄 Resume Analyzer"
    ]
)

#AI Chatbot
if feature == "🤖 AI Chatbot":
    st.title("🤖 AI Chatbot")

    user_input = st.text_input("Ask anything: ")

    if st.button("Ask AI"):
        if user_input.strip():
            with st.spinner("AI is thinking..."):
                answer = get_ai_response(user_input)
                st.success(answer)
        else:
            st.warning("Please enter a question")


#Notes Summarizer 
if feature == "📝 Notes Summarizer":
    st.title("🧠 Smart Notes Assistant")

    notes = st.text_area(
        "Paste your study notes here",
        height=250,
        placeholder="Paste your class notes, textbook content, or theory here..."
    )

    mode = st.selectbox(
        "Choose what you want",
        [
            "📌 Short Summary",
            "❓ Important Questions",
            "🧠 Key Concepts",
            "📝 Exam-Oriented Notes"
        ]
    )

    if st.button("Generate"):
        if notes.strip():
            with st.spinner("Processing notes..."):
                prompt = generate_notes_prompt(notes, mode)
                response = get_ai_response(prompt)
                st.success(response)
        else:
            st.warning("Please paste some notes")


#PDF Q&A
if feature == "📄 PDF Q&A":
    st.title("📄 PDF Question Answering")


    uploaded_pdf = st.file_uploader("Upload PDF", type="pdf")

    if uploaded_pdf:
        text = extract_text_from_pdf(uploaded_pdf)
        st.write(text[:1000])
        with st.spinner("Processing PDF..."):
            vectorstore = process_pdf(uploaded_pdf)
            st.success("PDF processed successfully")

    question = st.text_input("Ask a question from this PDF")

    if st.button("Ask") and question:
        with st.spinner("Thinking..."):
            answer = ask_pdf_question(vectorstore, question)
            st.success(answer)


#Resume Analyzer
from utils.pdf_reader import extract_pdf_text
from utils.resume_analyzer import calculate_ats_score, extract_skills, extract_education, extract_experience
from utils.prompts import resume_analysis_prompt
from utils.ollama_helper import ask_ollama
import streamlit as st

if feature == "📄 Resume Analyzer":
    st.title("📄 AI Resume Analyzer")


    resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
    job_desc = st.text_area("Paste Job Description")

    if st.button("Analyze Resume"):

        if resume_file and job_desc:

            resume_text = extract_pdf_text(resume_file)

            ats = calculate_ats_score(resume_text, job_desc)

            skills_list = ["python","java","sql","ml","ai","git","github","streamlit","api","docker"]
            found_skills = extract_skills(resume_text, skills_list)
            missing_skills = list(set(skills_list) - set(found_skills))

            education = extract_education(resume_text)
            experience = extract_experience(resume_text)

            st.subheader("📊 ATS Score")
            st.success(f"{ats}% Match")

            st.subheader("🧠 Skills Found")
            st.write(found_skills)

            st.subheader("❌ Missing Skills")
            st.write(missing_skills)

            st.subheader("🎓 Education")
            st.write(education)

            st.subheader("💼 Experience")
            st.write(experience)

            prompt = resume_analysis_prompt(resume_text, job_desc)
            hr_feedback = ask_ollama(prompt)

            st.subheader("🧑‍💼 HR Feedback")
            st.info(hr_feedback)

            st.subheader("🛠 Suggestions")
            st.write("• Add missing skills")
            st.write("• Improve project descriptions")
            st.write("• Quantify achievements")

        else:
            st.warning("Upload resume and paste job description.")



with open("AI_powered_assistant_BOproject.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>", 
        unsafe_allow_html=True
    )
