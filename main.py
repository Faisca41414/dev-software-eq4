from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import sys

if ("fastapi" not in  sys.argv[0] and "uvicorn" not in sys.argv[0]): 
    print("\n\t🦄🦄🦄🦄🦄🦄🦄🦄\033[1;31m Please run this file with 'fastapi run dev'")


app = FastAPI()

origins = [
    "http://localhost:5173", 
    os.getenv("FRONTEND_URL", "https://production.com") 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    username: str
    message: str


@app.get("/")
async def root():
    return {"message": "Hello World"}

messagesyet=[]
@app.post("/addData")
async def root(msg: Message):
    messagesyet.extend([{'username': 'gpt', 'message': f'Im the backend and you have sent me this message: {msg}'}])
    return messagesyet





if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)