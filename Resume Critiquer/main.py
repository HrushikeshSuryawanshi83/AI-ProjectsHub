import streamlit as st
import PyPDF2
import io
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="AI Resume Critiquer", page_icon="📄", layout="centered")
st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback on how to improve it.")

# Get API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# File uploader
uploaded_file = st.file_uploader("Upload Your Resume (PDF or TXT)", type=["pdf", "txt"])

# Job role input
job_role = st.text_input("Enter the job role you are applying for (optional):")

# Analyze button
analyze = st.button("Analyze Resume")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to handle PDF or TXT
def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

# Main analysis block
if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content...")
            st.stop()

        # Prompt for AI
        prompt = f"""
        You are an expert career advisor and recruiter. You will review the following resume text and give detailed, constructive feedback to improve it.

        Resume:
        {file_content}

        Job Role (if provided): {job_role if job_role.strip() else "Not specified"}

        Please provide your feedback in the following format:
        1. **Overall Impression**
        2. **Strengths**
        3. **Weaknesses / Gaps**
        4. **ATS (Applicant Tracking System) Optimization Tips**
        5. **Role-specific Suggestions** (if job role is given)
        6. **Grammar & Formatting Issues**
        7. **Suggested Next Steps**
        8.**Summary**
        """

        # Initialize Gemini client
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GEMINI_API_KEY)

        # Get AI feedback
        with st.spinner("Analyzing your resume..."):
            response = llm.invoke(prompt)

        # Show results
        st.markdown("### Analysis Results")
        st.markdown(response.content)

    except Exception as e:
        st.error(f"Error occurred: {str(e)}")
