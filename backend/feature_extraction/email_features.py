import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer

class EmailFeatureExtractor:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=100, ngram_range=(1,1))

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r'[^a-z\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def fit_transform(self, emails):
        cleaned = [self.clean_text(e) for e in emails]
        return self.vectorizer.fit_transform(cleaned).toarray()

    def transform(self, emails):
        cleaned = [self.clean_text(e) for e in emails]
        return self.vectorizer.transform(cleaned).toarray()