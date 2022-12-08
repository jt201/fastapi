from datetime import datetime
from typing import List

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

data: List["TodoItem"] = []


class TodoItem:
    id: int
    content: str
    author: str
    status: bool
    created: datetime

    def __init__(self, content: str = ""):
        self.id = 1 if len(data) == 0 else max([item.id for item in data])
        self.content = content
        self.author = "201"
        self.status = False
        self.created = datetime.now()


from views import router
from api import router as apiRouter

app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(router, include_in_schema=False)
app.include_router(apiRouter)
