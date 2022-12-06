from dataclasses import dataclass
from datetime import datetime
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from typing import List

from . import templates

router = APIRouter()


@dataclass
class TodoItem:
    id: int
    content: str
    author: str
    status: bool
    created: datetime


data: List[TodoItem] = [
    TodoItem(
        id=1,
        content="Todo List Item",
        author="201",
        status=False,
        created=datetime.fromisoformat("2022-01-01 00:00:00"),
    ),
    TodoItem(
        id=1,
        content="OLD Todo List Item",
        author="201",
        status=True,
        created=datetime.fromisoformat("2021-12-31 13:50:00"),
    ),
]


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": data})
