from fastapi import FastAPI

from app.inference.predictor import Predictor
from app.inference.schemas import PredictionRequest,PredictionResponse

app = FastAPI(
    title = "AI Storage Node Predictor",
    version="1.0.0",
)
predictor = Predictor()

@app.get("/")
def home():
    return {
        "message" : "Ai Distributed Storage Prediction API"

    }

@app.post(
    "/predict",
    response_model = PredictionResponse,   
)
def predict(
    request : PredictionRequest
):
    score = predictor.predict(
        request.model_dump()
    )

    return PredictionResponse(
        expert_score = score
    )