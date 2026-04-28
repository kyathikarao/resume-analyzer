from app.text_preprocessor import preprocess_text
from app.analyzer import calculate_ats_score, get_keyword_analysis

resume_text = """
Python developer with experience in machine learning, data analysis, and SQL.
"""

job_description = """
Looking for a Python developer skilled in machine learning, SQL, data analysis,
deep learning, and TensorFlow.
"""

# Preprocess
resume_tokens = preprocess_text(resume_text)
job_tokens = preprocess_text(job_description)

# ATS Score
score, similarity = calculate_ats_score(resume_tokens, job_tokens)

# Keyword Analysis
matched, missing = get_keyword_analysis(resume_tokens, job_tokens)

print(f"ATS Score: {score}%")
print(f"\nMatched Keywords:\n{matched}")
print(f"\nMissing Keywords:\n{missing}")
from app.analyzer import generate_suggestions

suggestions = generate_suggestions(missing)

print("\nSuggestions:")
for s in suggestions:
    print("-", s)