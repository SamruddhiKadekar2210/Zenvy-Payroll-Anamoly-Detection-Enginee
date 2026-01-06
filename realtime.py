from fastapi import FastAPI
import numpy as np
from model import AnomalyModel
from features import extract_features
from config import ANOMALY_THRESHOLD

app = FastAPI()

model = AnomalyModel()
model.load()

@app.post("/predict")
def predict(record: dict):
    peer = record["peer_stats"]

    x = extract_features(record, peer).reshape(1, -1)
    score = model.score(x)[0]

    return {
        "anomaly_score": float(score),
        "is_anomaly": bool(score > ANOMALY_THRESHOLD)
    }
