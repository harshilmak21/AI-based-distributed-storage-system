from fastapi import FastAPI
from pathlib import Path
import httpx
from fastapi import UploadFile , File ,HTTPException

from app.inference.predictor import Predictor
from app.inference.schemas import PredictionRequest,PredictionResponse
from app.inference.node_coordinator import NodeCoordinator

coordinator = NodeCoordinator()


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


@app.post("/upload")

async def upload_file(file : UploadFile = File(...)):
    if not file.filename or Path(file.filename).name != file.filename:
        raise HTTPException(status_code=400 , detail = "Invalid filename")

    result = await coordinator.rank_nodes()
    ranked_nodes = result["ranked_nodes"]

    if not ranked_nodes:
        raise HTTPException(
            status_code=503,
            detail = "No Storage nodes are available",

        )

    async with httpx.AsyncClient(timeout = 60.0) as client:
        for node in ranked_nodes:
            node_id = node["node_id"]
            port = 8000 + int(node_id.split("-")[-1])
            url = f"http://localhost:{port}/upload"

            try:
                content = await file.read()
                response = await client.post(
                    url,
                    files={
                        "file": (
                            file.filename,
                            content,
                            file.content_type or "application/octet-stream",
                        )
                    },
                )
                if response.status_code == 409:

                    await file.seek(0)
                    continue

                response.raise_for_status()

                return {
                    "message": "File uploaded successfully",
                    "selected_node": node_id,
                    "expert_score": node["expert_score"],
                    "filename": file.filename,
                }

            except httpx.HTTPError:
                await file.seek(0)
                continue
        raise HTTPException(
        status_code=503,
        detail="Upload failed on all available nodes",
    )