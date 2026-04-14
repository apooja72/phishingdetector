import os
import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from backend.data_loader import load_email_data
from backend.feature_extraction.email_features import EmailFeatureExtractor
from backend.models.email_model import EmailModel

DATA_PATH = "backend/data/email_dataset.csv"
MODEL_PATH = "backend/models/saved/email_model.pkl"
VECT_PATH = "backend/models/saved/email_vectorizer.pkl"

def train_email_model():
    texts, labels = load_email_data(DATA_PATH)

    extractor = EmailFeatureExtractor()
    X = extractor.fit_transform(texts)
    y = np.array(labels)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = EmailModel()
    model.train(X_train, y_train)

    preds = model.model.predict(X_test)

    print("\n📊 Email Model Accuracy")
    print("Accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

    model.save(MODEL_PATH)
    joblib.dump(extractor.vectorizer, VECT_PATH)

    print("✅ Email Model trained and saved")

if __name__ == "__main__":
    train_email_model()