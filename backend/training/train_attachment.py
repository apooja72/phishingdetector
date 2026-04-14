import os
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from backend.data_loader import load_attachment_data
from backend.feature_extraction.attachment_features import AttachmentFeatureExtractor
from backend.models.attachment_model import AttachmentModel

DATA_PATH = "backend/data/attachment_dataset.csv"
MODEL_PATH = "backend/models/saved/attachment_model.pkl"

def train_attachment_model():
    filenames, labels = load_attachment_data(DATA_PATH)

    extractor = AttachmentFeatureExtractor()
    X = extractor.extract(filenames)
    y = np.array(labels)

    # split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = AttachmentModel()
    model.train(X_train, y_train)

    preds = model.model.predict(X_test)

    print("\n📊 Attachment Model Accuracy")
    print("Accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

    model.save(MODEL_PATH)

    print("✅ Attachment Model trained and saved")

if __name__ == "__main__":
    train_attachment_model()