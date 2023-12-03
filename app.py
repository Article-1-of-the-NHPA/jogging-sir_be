from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import json

conn = sqlite3.connect('joggingsir.db', check_same_thread=False)
c = conn.cursor()

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return JSONResponse(content={"Hello하이": "World"})

@app.get("/images/{filename}")
async def get_image(filename: str):
    # Serve the uploaded image
    return FileResponse(f"images/{filename}", media_type="image/jpeg")

@app.get("/courses")
def get_courses():
    data = []
    try:
        results = c.execute('select * from course').fetchall()
        for result in results:
            data.append(result)
    except Exception as e:
        raise e
    finally:
        conn.commit()
    content = data
    headers = {'Content-Type': 'application/json', 'charset':'utf-8'}
    return JSONResponse(content=content, headers=headers)

@app.get("/records")
def get_records():
    data = []
    try:
        results = c.execute('select * from record').fetchall()
        for result in results:
            data.append(result)
    except Exception as e:
        raise e
    finally:
        conn.commit()
    content = data
    headers = {'Content-Type': 'application/json', 'charset':'utf-8'}
    return JSONResponse(content=content, headers=headers)

@app.post("/records")
def post_record():
    try:
        c.execute('insert into record values (for, test)')
        return 'true'
    except Exception as e:
        raise e
    finally:
        conn.commit()

