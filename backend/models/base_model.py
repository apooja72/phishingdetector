import xgboost as xgb
import joblib

class BaseXGBModel:
    def __init__(self):
        self.model = xgb.XGBClassifier(
            n_estimators=15,
            max_depth=1,
            learning_rate=0.5,
            subsample=0.5,
            colsample_bytree=0.5,
            eval_metric='logloss',
            use_label_encoder=False,
            n_jobs=-1
        )

    def train(self, X, y):
        self.model.fit(X, y)

    def predict_proba(self, X):
        return self.model.predict_proba(X)[:, 1]

    def save(self, path):
        joblib.dump(self.model, path)

    def load(self, path):
        self.model = joblib.load(path)