from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from math import ceil

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, Response

from main import data, TodoItem
from . import templates

router = APIRouter()


def get_pagination(total: int = 0, current: int = 1, length: int = 5) -> List[int]:
    # 가운데 표시 페이지 갯수 구하기
    calc_length: int = ((length - 1 if length % 2 == 0 else length) if length >= 5 else 5) - 2

    # 전체 페이지
    page: List[int] = [item for item in range(1, total + 1)]

    # 전체 페이지 수가 표시할 페이지수보다 많을 경우
    if total > calc_length + 2:
        separator: int = max(1, (calc_length - 1) / 2)
        start: int = max(1, current - separator)
        end: int = min(total, current + separator)

        # 전체 페이지 수가 계산된 페이지수보다 많을 경우
        if total > calc_length:
            page = [item for item in page if item >= start and item <= end]

        while len(page) < calc_length:
            if max(page) == total:
                page.insert(0, min(page) - 1)
            else:
                page.append(max(page) + 1)

        if min(page) == 1:
            page.append(max(page) + 1)
        elif min(page) == 2:
            page.insert(0, 1)
        elif max(page) == total:
            page.insert(0, min(page) - 1)
        elif max(page) == total - 1:
            page.append(total)

    return page


@router.get("/", response_class=HTMLResponse)
async def index(request: Request, page: int = 1):
    page: int = max(page, 1)
    rpp: int = 5
    start: int = (page - 1) * rpp
    end: int = start + rpp
    result: List[TodoItem] = data[::-1][start:end]
    total: int = len(data)
    total_pages: int = ceil(total / rpp)

    pages: List[int] = get_pagination(total=total_pages, current=page, length=5)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "data": result,
            "total": total,
            "page": page,
            "rpp": rpp,
            "total_pages": total_pages,
            "pages": pages,
        },
    )


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
