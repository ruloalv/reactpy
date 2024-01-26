from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure

mats = FastAPI()

@mats.get("/")
async def root():
    return {"message": "Página de Materiales"}