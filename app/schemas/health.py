from pydantic import BaseModel

class HealthRequest(BaseModel):
    service_name : str
    status: str