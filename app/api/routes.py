from fastapi import APIRouter
from app.schemas.health import HealthRequest

router = APIRouter()

@router.post("/health")
def health_check(request : HealthRequest):
    return {
        "message" : "Request received Successfully!!",
        "received" : request
    }