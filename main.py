from dataclasses import dataclass
from datetime import datetime
from typing import List

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


@dataclass
class TodoItem:
    id: int
    content: str
    author: str
    status: bool
    created: datetime


data: List[TodoItem] = []


from views import router
from api import router as apiRouter

app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(router)
app.include_router(apiRouter)
