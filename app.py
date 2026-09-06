from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import logging

import google.cloud.logging

client = google.cloud.logging.Client()
client.setup_logging()



app = FastAPI()

model = joblib.load("models/model.pkl")

logging.basicConfig(level=logging.INFO)

class HeartInput(BaseModel):
    age: int
    gender: str
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/predict")
def predict(data: HeartInput):

    df = pd.DataFrame([data.model_dump()])

    pred = int(model.predict(df)[0])

    logging.info(
        f"INPUT={data.model_dump()} PREDICTION={pred}"
    )

    return {"prediction": pred}
