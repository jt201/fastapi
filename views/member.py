from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from . import templates

router = APIRouter(prefix="/member")


@router.get("/login", response_class=HTMLResponse)
async def member_login(request: Request):
    return templates.TemplateResponse("member/login.html", {"request": request})


@router.get("/register", response_class=HTMLResponse)
async def member_register(request: Request):
    return templates.TemplateResponse("/member/register.html", {"request": request})
