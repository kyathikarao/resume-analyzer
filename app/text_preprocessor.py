import re
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# ---------- SAFE NLTK SETUP (NO INFINITE DOWNLOAD) ----------
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Load stopwords safely
stop_words = set(stopwords.words('english'))

# ---------- SAFE SPACY SETUP ----------
try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = spacy.blank("en")   # fallback (NO download)


def preprocess_text(text):
    """
    Cleans and preprocesses text using NLP techniques.
    """

    # 1. Lowercase
    text = text.lower()

    # 2. Remove special characters
    text = re.sub(r'[^a-z\s]', ' ', text)

    # 3. Tokenization
    tokens = word_tokenize(text)

    # 4. Remove stopwords & short words
    tokens = [
        word for word in tokens
        if word not in stop_words and len(word) > 2
    ]

    # 5. Lemmatization
    doc = nlp(" ".join(tokens))
    lemmatized_tokens = [
        token.lemma_ for token in doc
        if token.lemma_ not in stop_words
    ]

    return lemmatized_tokens