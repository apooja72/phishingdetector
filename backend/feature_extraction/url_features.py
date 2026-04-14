from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from backend.utils.common import (
    is_ip_address,
    url_length,
    count_special_chars,
    count_digits
)

class URLFeatureExtractor:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3,4),max_features=200)

    def fit_transform(self, urls):
        tfidf = self.vectorizer.fit_transform(urls)
        extra = np.array([self._extra_features(u) for u in urls])
        return np.hstack([tfidf.toarray(), extra])

    def transform(self, urls):
        tfidf = self.vectorizer.transform(urls)
        extra = np.array([self._extra_features(u) for u in urls])
        return np.hstack([tfidf.toarray(), extra])

    def _extra_features(self, url):
        return [
            is_ip_address(url),
            url_length(url),
            count_special_chars(url),
            count_digits(url)
        ]