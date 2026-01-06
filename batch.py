import numpy as np
import pandas as pd
from model import AnomalyModel
from features import extract_features

df = pd.read_csv("data.csv")

features = []
for _, row in df.iterrows():
    record = row.to_dict()
    peer = {
        "avg_salary": df["salary"].mean(),
        "avg_overtime": df["overtime_hours"].mean()
    }
    features.append(extract_features(record, peer))

X = np.array(features)

model = AnomalyModel()
model.train(X)
model.save()
