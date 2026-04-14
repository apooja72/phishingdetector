import joblib
import os

BASE_DIR = "backend/models/saved"

class ModelLoader:
    def __init__(self):
        self.url_model = joblib.load(os.path.join(BASE_DIR, "url_model.pkl"))
        self.email_model = joblib.load(os.path.join(BASE_DIR, "email_model.pkl"))
        self.attachment_model = joblib.load(os.path.join(BASE_DIR, "attachment_model.pkl"))

        self.url_vectorizer = joblib.load(os.path.join(BASE_DIR, "url_vectorizer.pkl"))
        self.email_vectorizer = joblib.load(os.path.join(BASE_DIR, "email_vectorizer.pkl"))

_loader = None

def get_models():
    global _loader
    if _loader is None:
        _loader = ModelLoader()
    return _loader