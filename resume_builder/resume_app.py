import streamlit as st
from resume_builder.crew import ResumeBuilder

st.title("🎯 Resume Tailoring Assistant")

resume = st.text_area("📄 Paste your resume here")
job = st.text_area("🧾 Paste the job description here")

if st.button("🚀 Generate Tailored Resume"):
    inputs = {
        "resume": resume,
        "job_description": job
    }
    try:
        result = ResumeBuilder().crew().kickoff(inputs=inputs)
        st.success("✅ Tailored resume generated!")
        st.text_area("🎉 Output", result, height=400)
    except Exception as e:
        st.error(f"❌ Error: {e}")
