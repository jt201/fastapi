from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from views import router

app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(router)
