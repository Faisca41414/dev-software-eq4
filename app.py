from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:8000"],  # Svelte's dev server
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory dictionary
data_store = {}

# Pydantic model for input validation
class KeyValue(BaseModel):
    key: str
    value: str

@app.get("/data")
def get_data():
    return data_store

@app.get("/sendmessage")
def answermessage():
    return 

@app.post("/data")
def add_data(entry: KeyValue):
    if entry.key in data_store:
        raise HTTPException(status_code=400, detail="Key already exists")
    data_store[entry.key] = entry.value
    return {"message": "Entry added successfully"}

@app.delete("/data/{key}")
def delete_data(key: str):
    if key not in data_store:
        raise HTTPException(status_code=404, detail="Key not found")
    del data_store[key]
    return {"message": "Entry deleted successfully"}

from fastapi.staticfiles import StaticFiles

app.mount("/", StaticFiles(directory="./svelte-app/public/", html=True), name="static")
