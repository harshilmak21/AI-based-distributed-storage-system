import httpx
import psutil
import shutil
import os
from pathlib import Path

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
app = FastAPI()

NODE_ID = os.getenv("NODE_ID", "node-1")
STORAGE_PATH = Path(os.getenv("STORAGE_PATH", "/data"))
STORAGE_CAPACITY_GB = float(os.getenv("STORAGE_CAPACITY_GB","1"))
STORAGE_CAPACITY_BYTES = int(STORAGE_CAPACITY_GB * (1024 **3))
STORAGE_PATH.mkdir(parents=True, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Storage node is running",
        "node_id": NODE_ID
    }


@app.get("/health")
def health():
    return {
        "node_id": NODE_ID,
        "status": "healthy"
    }


@app.get("/storage")
def storage_info():
    return {
        "node_id": NODE_ID,
        "storage_path": str(STORAGE_PATH),
        "files": [
            p.name for p in STORAGE_PATH.iterdir()
            if p.is_file()
        ]
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename or Path(file.filename).name != file.filename:
        raise HTTPException(status_code=400, detail="Invalid filename")

    destination = STORAGE_PATH / file.filename

    if destination.exists():
        raise HTTPException(status_code=409, detail="File already exists")

    try:
        with destination.open("xb") as output:
            while chunk := await file.read(1024 * 1024):
                output.write(chunk)
    except FileExistsError:
        raise HTTPException(status_code=409, detail="File already exists")
    except Exception:
        destination.unlink(missing_ok=True)
        raise HTTPException(status_code=500, detail="Upload failed")
    finally:
        await file.close()

    return {
        "message": "File uploaded successfully",
        "node_id": NODE_ID,
        "filename": file.filename
    }

@app.get("/download/{filename}")
def download_file(filename:str):
    if not filename or Path(filename).name != filename:
        raise HTTPException(status_code = 409 , detail="Invallid filename")

    file_path = STORAGE_PATH/filename

    if not file_path.is_file():
        raise HTTPException(status_code=404 , detail = "file not found")

    return FileResponse(
        path = file_path , 
        filename = filename ,
        media_type = "application/octet-stream"
    )



@app.get("/peer/{peer_id}/health")
async def check_peer(peer_id: int):
    if peer_id not in range(1, 6):
        raise HTTPException(status_code=400, detail="Invalid peer ID")

    if peer_id == int(NODE_ID.split("-")[-1]):
        raise HTTPException(status_code=400, detail="Cannot check self")

    peer_url = f"http://node{peer_id}:8000/health"

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.get(peer_url)
            response.raise_for_status()
            return {
                "requesting_node": NODE_ID,
                "peer": response.json()
            }
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="Peer unavailable")



@app.get("/metrics")
def get_metrics():
    stored_bytes = get_stored_bytes()
    free_bytes = max(0 , STORAGE_CAPACITY_BYTES - stored_bytes)

    cpu_usage = psutil.cpu_percent(interval = 0.2)
    memory_usage = psutil.virtual_memory().percent

    return {
        "node_id": NODE_ID,
        "free_storage": free_bytes / (1024 ** 3),
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "latency": 1.0,
        "bandwidth": 100.0,
        "reliability": 0.99,
        "failure_rate": 0.01,
        "current_load": 0.0,
        "stored_bytes": stored_bytes,
        "capacity_bytes": STORAGE_CAPACITY_BYTES,
    }




def get_stored_bytes():
    return sum(
        path.stat().st_size
        for path in STORAGE_PATH.iterdir()
        if path.is_file()
    )