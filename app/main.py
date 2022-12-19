from datetime import datetime
from typing import List, Dict, Optional

from fastapi import FastAPI, Cookie
from fastapi.staticfiles import StaticFiles

from app.api import router as apiRouter
from app.views import router as viewRouter


app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(viewRouter, include_in_schema=False)
app.include_router(apiRouter)
