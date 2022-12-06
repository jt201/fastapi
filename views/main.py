from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, Response

from . import templates

router = APIRouter()


@dataclass
class TodoItem:
    id: int
    content: str
    author: str
    status: bool
    created: datetime


data: List[TodoItem] = []


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    result: List[TodoItem] = data[::-1]
    return templates.TemplateResponse("index.html", {"request": request, "data": result})


@router.post("/")
async def create_item(content: str = Form(default="")):
    if not content:
        return Response(
            content="""
                <script>
                    alert('내용을 입력해주세요!!');
                    history.back();
                </script>
            """,
            media_type="text/html;charset=utf-8",
        )
    if content in [item.content for item in data]:
        return Response(
            content="""
                <script>
                    alert('이미 등록된 데이터 입니다!!');
                    history.back();
                </script>
            """,
            media_type="text/html;charset=utf-8",
        )

    data.append(
        TodoItem(
            id=(max([item.id for item in data]) + 1 if len(data) > 0 else 0),
            content=content,
            author="201",
            status=False,
            created=datetime.now(),
        )
    )
    return RedirectResponse("/", status_code=302)
