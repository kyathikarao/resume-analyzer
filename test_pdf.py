from app.pdf_parser import extract_text_from_pdf

file_path = "sample_resume.pdf"

with open(file_path, "rb") as f:
    text = extract_text_from_pdf(f)

print(text[:1000])  # Print first 1000 characters