from fastapi import FastAPI, Request
from src.anomaly_detector import detect_anomaly
import pandas as pd

app = FastAPI()

@app.post("/detect")
async def detect(request: Request):
    data = await request.json()
    df = pd.DataFrame([data])
    result = detect_anomaly(df)
    return {"is_anomaly": result}
