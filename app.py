import streamlit as st
from ranking import rank_resumes

st.title("AI Resume Screening")

job_desc = st.text_area("Paste Job Description")
