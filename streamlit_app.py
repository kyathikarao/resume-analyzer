import streamlit as st

from app.pdf_parser import extract_text_from_pdf
from app.text_preprocessor import preprocess_text
from app.analyzer import (
    calculate_ats_score,
    get_keyword_analysis,
    generate_suggestions,
    categorize_skills
)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Resume Analyzer & ATS Predictor",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("📄 Resume Analyzer & ATS Score Predictor")
st.markdown("Upload your resume and compare it with a job description using AI-powered analysis.")

st.markdown("---")

# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📤 Upload Resume (PDF)", type=["pdf"])

with col2:
    job_description = st.text_area("📝 Paste Job Description", height=200)

analyze = st.button("🚀 Analyze Resume")

# ---------------- MAIN LOGIC ----------------
if analyze:

    if not uploaded_file or not job_description.strip():
        st.warning("Please upload a resume AND paste a job description.")
        st.stop()

    # Extract text
    resume_text = extract_text_from_pdf(uploaded_file)

    if not resume_text:
        st.error("Could not extract text from the uploaded PDF.")
        st.stop()

    # Preprocess
    resume_tokens = preprocess_text(resume_text)
    job_tokens = preprocess_text(job_description)

    # ATS Score
    score, similarity = calculate_ats_score(resume_tokens, job_tokens)

    # Keyword Analysis
    matched, missing = get_keyword_analysis(resume_tokens, job_tokens)

    # Suggestions
    suggestions = generate_suggestions(missing)

    # Skill Categorization
    tech_skills, soft_skills = categorize_skills(resume_tokens)

    # ---------------- RESULTS SECTION ----------------
    st.markdown("---")
    st.subheader("📊 ATS Score")

    st.progress(int(min(score, 100)))

    if score >= 75:
        st.success(f"Strong Match 🎯 : {score}%")
    elif score >= 50:
        st.warning(f"Moderate Match ⚠️ : {score}%")
    else:
        st.error(f"Low Match ❌ : {score}%")

    st.caption(f"Similarity Score: {round(similarity, 3)}")

    # ---------------- KEYWORDS ----------------
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Matched Keywords")
        st.write(sorted(matched) if matched else "None")

    with col2:
        st.subheader("❌ Missing Keywords")
        st.write(sorted(missing) if missing else "None")

    # ---------------- SKILL BREAKDOWN ----------------
    st.markdown("---")
    st.subheader("🧠 Skill Breakdown")

    col1, col2 = st.columns(2)

    with col1:
        st.write("💻 Technical Skills")
        st.write(sorted(tech_skills) if tech_skills else "None")

    with col2:
        st.write("🤝 Soft Skills")
        st.write(sorted(soft_skills) if soft_skills else "None")

    # ---------------- SUGGESTIONS ----------------
    st.markdown("---")
    st.subheader("💡 Suggestions to Improve Resume")

    for s in suggestions:
        st.write("👉 " + s)

    st.markdown("---")
    st.success("Analysis Completed Successfully 🚀")
    