from fastapi import FastAPI
from pydantic import BaseModel

import sys
if ("fastapi" not in  sys.argv[0] and "uvicorn" not in sys.argv[0]): 
    print("\n\t🦄🦄🦄🦄🦄🦄🦄🦄\033[1;31m Please run this file with 'fastapi run dev\n\n'")
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}