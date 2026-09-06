import pandas as pd
import requests

df = pd.read_csv("data.csv")

sample = df.sample(
    n=100,
    replace=True,
    random_state=42
)

sample.to_csv(
    "sample_100.csv",
    index=False
)

URL = "http://34.172.32.91/predict"

for _, row in sample.iterrows():
    if row.isna().any():
        continue

    payload = {
        "age": int(row["age"]),
        "gender": row["gender"],
        "cp": int(row["cp"]),
        "trestbps": float(row["trestbps"]),
        "chol": float(row["chol"]),
        "fbs": int(row["fbs"]),
        "restecg": int(row["restecg"]),
        "thalach": float(row["thalach"]),
        "exang": int(row["exang"]),
        "oldpeak": float(row["oldpeak"]),
        "slope": int(row["slope"]),
        "ca": int(row["ca"]),
        "thal": int(row["thal"])
    }

    r = requests.post(URL, json=payload)

    print(r.json())
