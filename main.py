import os 
from pathlib import Path
from fastapi import FastAPI

app = FastAPI()

NODE_ID = os.getenv("NODE_ID","node-1")
STORAGE_PATH = Path(os.getenv("STORAGE_PATH","/data"))

STORAGE_PATH.mkdir(parents=True,exist_ok=True)

@app.get("/")
def home():
    return {
        "message" : "Storage Node is  running",
        "node_id" : NODE_ID
    }

@app.get("/health")
def health():
    return {
        "node_id" : NODE_ID,
        "stauts" : "healthy"
    }

@app.get("/storage")
def storage_info():
    return {
        "node_id" : NODE_ID,
        "storage_path" : str(STORAGE_PATH),
        "files" : [p.name for p in STORAGE_PATH.iterdir() if p.is_file()]
    }