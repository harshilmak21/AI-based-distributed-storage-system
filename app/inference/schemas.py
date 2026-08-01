from pydantic import BaseModel

class PredictionRequest(BaseModel):

    free_storage: float
    cpu_usage: float
    memory_usage: float
    latency: float
    bandwidth: float
    reliability: float
    failure_rate: float
    current_load: float

class PredictionResponse(BaseModel):

    expert_score: float