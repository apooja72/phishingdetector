import numpy as np
from backend.prediction.model_loader import get_models
from backend.feature_extraction.url_features import URLFeatureExtractor

class URLPredictor:
    def __init__(self):
        self.models = get_models()
        self.extractor = URLFeatureExtractor()
        self.extractor.vectorizer = self.models.url_vectorizer

    def predict(self, url: str):
        X = self.extractor.transform([url])

        prob = self.models.url_model.predict_proba(X)[0][1]
        return self._normalize(prob)

    def _normalize(self, prob):
        return float(max(0.0, min(1.0, prob)))