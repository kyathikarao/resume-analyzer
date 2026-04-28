from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_ats_score(resume_tokens, job_tokens):

    resume_text = " ".join(resume_tokens)
    job_text = " ".join(job_tokens)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_text])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    # Keyword coverage boost
    resume_set = set(resume_tokens)
    job_set = set(job_tokens)

    if len(job_set) == 0:
        coverage = 0
    else:
        coverage = len(resume_set.intersection(job_set)) / len(job_set)

    # Weighted final score
    final_score = (0.6 * similarity + 0.4 * coverage) * 100

    return round(final_score, 2), similarity
def get_keyword_analysis(resume_tokens, job_tokens):
    """
    Compares resume and job description keywords.

    Returns:
        matched_keywords (set)
        missing_keywords (set)
    """

    resume_set = set(resume_tokens)
    job_set = set(job_tokens)

    matched_keywords = resume_set.intersection(job_set)
    missing_keywords = job_set.difference(resume_set)

    return matched_keywords, missing_keywords
def generate_suggestions(missing_keywords):
    """
    Generate human-readable suggestions based on missing keywords.
    """

    if not missing_keywords:
        return ["Your resume is well aligned with the job description!"]

    suggestions = []

    for word in list(missing_keywords)[:10]:  # limit suggestions
        suggestions.append(f"Consider adding or highlighting '{word}' in your resume.")

    return suggestions
TECH_SKILLS = {
    "python", "java", "c++", "sql", "tensorflow", "pytorch",
    "machine", "learning", "deep", "nlp", "api", "flask"
}

SOFT_SKILLS = {
    "communication", "teamwork", "leadership", "problem", "solving"
}


def categorize_skills(tokens):
    tech = set(tokens).intersection(TECH_SKILLS)
    soft = set(tokens).intersection(SOFT_SKILLS)

    return tech, soft