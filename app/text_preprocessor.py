import re
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Load spaCy model
import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Load stopwords
stop_words = set(stopwords.words('english'))


def preprocess_text(text):
    """
    Cleans and preprocesses text using NLP techniques.

    Steps:
    - Lowercasing
    - Remove special characters
    - Tokenization
    - Stopword removal
    - Lemmatization (using spaCy)

    Returns:
        List of cleaned tokens
    """

    # 1. Lowercase
    text = text.lower()

    # 2. Remove special characters & numbers
    text = re.sub(r'[^a-z\s]', ' ', text)

    # 3. Tokenization
    tokens = word_tokenize(text)

    # 4. Remove stopwords & short words
    tokens = [
        word for word in tokens
        if word not in stop_words and len(word) > 2
    ]

    # 5. Lemmatization using spaCy
    doc = nlp(" ".join(tokens))
    lemmatized_tokens = [
        token.lemma_ for token in doc
        if token.lemma_ not in stop_words
    ]

    return lemmatized_tokens