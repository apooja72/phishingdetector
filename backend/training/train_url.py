import os
import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from backend.data_loader import load_url_data
from backend.feature_extraction.url_features import URLFeatureExtractor
from backend.models.url_model import URLModel

DATA_PATH = "backend/data/url_dataset.csv"
MODEL_PATH = "backend/models/saved/url_model.pkl"
VECT_PATH = "backend/models/saved/url_vectorizer.pkl"

def train_url_model():
    urls, labels = load_url_data(DATA_PATH)

    extractor = URLFeatureExtractor()
    X = extractor.fit_transform(urls)
    y = np.array(labels)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = URLModel()
    model.train(X_train, y_train)

    preds = model.model.predict(X_test)

    print("\n📊 URL Model Accuracy")
    print("Accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

    model.save(MODEL_PATH)
    joblib.dump(extractor.vectorizer, VECT_PATH)

    print("✅ URL Model trained and saved")

if __name__ == "__main__":
    train_url_model()