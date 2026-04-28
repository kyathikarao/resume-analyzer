from app.text_preprocessor import preprocess_text

sample_text = """
Experienced Python Developer with strong skills in Machine Learning,
Data Analysis, and SQL databases.
"""

tokens = preprocess_text(sample_text)

print(tokens)