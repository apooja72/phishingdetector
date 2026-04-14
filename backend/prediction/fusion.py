from backend.prediction.url_predictor import URLPredictor
from backend.prediction.email_predictor import EmailPredictor
from backend.prediction.attachment_predictor import AttachmentPredictor

class FusionEngine:
    def __init__(self):
        self.url_model = URLPredictor()
        self.email_model = EmailPredictor()
        self.attach_model = AttachmentPredictor()

    def compute(self, url=None, email=None, attachment=None):
        url_score = self.url_model.predict(url) if url else 0.0
        email_score = self.email_model.predict(email) if email else 0.0
        attach_score = self.attach_model.predict(attachment) if attachment else 0.0

        final_score = (
            0.444 * url_score +
            0.222 * email_score +
            0.333 * attach_score
        )

        return {
            "url_score": url_score,
            "email_score": email_score,
            "attachment_score": attach_score,
            "final_score": final_score,
            "prediction": "PHISHING" if final_score > 0.5 else "SAFE"
        }