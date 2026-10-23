
import os
from pathlib import Path

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
app = FastAPI()

NODE_ID = os.getenv("NODE_ID", "node-1")
STORAGE_PATH = Path(os.getenv("STORAGE_PATH", "/data"))
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