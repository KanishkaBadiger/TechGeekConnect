def generate_notes_prompt(notes, mode):
    if mode == "📌 Short Summary":
        return f"Summarize the following notes in simple bullet points:\n{notes}"

    elif mode == "❓ Important Questions":
        return f"From the following notes, generate 5 important exam questions:\n{notes}"

    elif mode == "🧠 Key Concepts":
        return f"Extract key concepts and definitions from these notes:\n{notes}"

    elif mode == "📝 Exam-Oriented Notes":
        return f"""
        Convert the following notes into exam-oriented answers.
        Use headings and points.
        Keep language simple.

        Notes:
        {notes}
        """


def generate_pdf_prompt(pdf_text, question):
    return f"""
You are an AI assistant.
Answer the question strictly using the PDF content below.
If the answer is not present, say "Answer not found in the PDF".

PDF Content:
{pdf_text}

Question:
{question}
"""

PDF_QA_PROMPT = """
You are a PDF Question Answering assistant.

Answer ONLY using the context below.
If the answer is not present, say:
"Not found in the PDF."

Context:
{context}

Question:
{question}
"""



def resume_analysis_prompt(resume, jd):
    return f"""
You are a professional HR and ATS system.

Analyze the resume and job description and provide:

1. ATS Match Score (0-100)
2. Skills Found
3. Missing Skills
4. Education Summary
5. Experience Summary
6. Improvement Suggestions
7. HR Feedback

Resume:
{resume}

Job Description:
{jd}

Give response in structured bullet format.
"""



