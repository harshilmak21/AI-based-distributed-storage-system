from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title = "AI Node Selector Service",
    version = "1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {
        "status" : "running",
        "message" : "AI Node Selector Service is Running!"
    }