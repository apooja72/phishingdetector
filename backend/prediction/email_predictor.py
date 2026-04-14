import numpy as np
from backend.prediction.model_loader import get_models
from backend.feature_extraction.email_features import EmailFeatureExtractor

class EmailPredictor:
    def __init__(self):
        self.models = get_models()
        self.extractor = EmailFeatureExtractor()
        self.extractor.vectorizer = self.models.email_vectorizer

    def predict(self, text: str):
        X = self.extractor.transform([text])

        prob = self.models.email_model.predict_proba(X)[0][1]
        return self._normalize(prob)

    def _normalize(self, prob):
        return float(max(0.0, min(1.0, prob)))