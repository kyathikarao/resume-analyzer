import pdfplumber

def extract_text_from_pdf(file):
    """
    Extracts text from an uploaded PDF file.

    Args:
        file: Uploaded file object (from Streamlit)

    Returns:
        text (str): Extracted text from PDF
    """
    text = ""

    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

    return text.strip()