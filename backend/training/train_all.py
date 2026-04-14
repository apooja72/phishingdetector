from backend.training.train_url import train_url_model
from backend.training.train_email import train_email_model
from backend.training.train_attachment import train_attachment_model

def train_all():
    print("🚀 Training URL Model...")
    train_url_model()

    print("🚀 Training Email Model...")
    train_email_model()

    print("🚀 Training Attachment Model...")
    train_attachment_model()

    print("🎯 All models trained successfully!")

if __name__ == "__main__":
    train_all()