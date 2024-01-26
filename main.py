from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure

from obras.obras import Obras

@component
def App():
    return html.h1("Hola desde reactpy")

app = FastAPI()
configure(app,Obras)

# @app.get("/")
# async def root():
    # return {"message": "Hola"}