import pandas as pd
import joblib
import shap
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

X = df.drop(columns=["target","sno"])

model = joblib.load("models/model.pkl")

X_proc = model.named_steps["preprocessor"].transform(X)

rf = model.named_steps["classifier"]

explainer = shap.TreeExplainer(rf)

sv = explainer.shap_values(X_proc)

print(type(sv))
print(np.array(sv).shape)
