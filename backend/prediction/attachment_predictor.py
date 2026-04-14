import numpy as np
from backend.prediction.model_loader import get_models
from backend.feature_extraction.attachment_features import AttachmentFeatureExtractor

class AttachmentPredictor:
    def __init__(self):
        self.models = get_models()
        self.extractor = AttachmentFeatureExtractor()

    def predict(self, filename: str):
        X = self.extractor.extract([filename])

        prob = self.models.attachment_model.predict_proba(X)[0][1]
        return self._normalize(prob)

    def _normalize(self, prob):
        return float(max(0.0, min(1.0, prob)))