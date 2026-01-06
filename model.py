import joblib
from sklearn.ensemble import IsolationForest
from config import CONTAMINATION, MODEL_PATH

class AnomalyModel:
    def __init__(self):
        self.model = IsolationForest(
            n_estimators=200,
            contamination=CONTAMINATION,
            random_state=42
        )

    def train(self, X):
        self.model.fit(X)

    def score(self, X):
        return -self.model.decision_function(X)

    def save(self):
        joblib.dump(self.model, MODEL_PATH)

    def load(self):
        self.model = joblib.load(MODEL_PATH)
