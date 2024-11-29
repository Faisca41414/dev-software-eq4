from fastapi import FastAPI
from pydantic import BaseModel

import sys
if ("fastapi" not in  sys.argv[0]): 
    raise Exception("\n\t🦄🦄🦄🦄🦄🦄🦄🦄\033[1;31m Please run this file with 'fastapi run dev'")
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}