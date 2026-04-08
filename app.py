import streamlit as st
from ranking import rank_resumes

st.title("🧠 AI Resume Screening")

job_desc = st.text_area("Paste Job Description")

uploaded_files = st.file_uploader(
    "Upload Resumes", type=["pdf"], accept_multiple_files=True
)

if st.button("Analyze"):
    results = rank_resumes(uploaded_files, job_desc)
    st.write(results)
