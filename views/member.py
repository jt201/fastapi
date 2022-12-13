from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse

from . import templates
from main import users, User

router = APIRouter(prefix="/member")


@router.get("/login", response_class=HTMLResponse)
async def member_login(request: Request):
    return templates.TemplateResponse("member/login.html", {"request": request})


@router.get("/register", response_class=HTMLResponse)
async def member_register(request: Request):
    return templates.TemplateResponse("/member/register.html", {"request": request})


@router.post("/register", response_class=HTMLResponse)
async def member_register_proc(
    email: str = Form(""),
    name: str = Form(""),
    password: str = Form(""),
    password_chk: str = Form(""),
):
    if len([item.email for item in users if item.email == email]) > 0:
        return HTMLResponse(
            content="""
                <script>
                    alert("이미 등록된 이메일 입니다!!");
                    history.back();
                </script>
            """,
        )

    if password != password_chk:
        return HTMLResponse(
            content="""
                <script>
                    alert("비밀번호가 맞지 않습니다!!");
                    history.back();
                </script>
            """,
        )

    new_user = User(name=name, email=email, password=password)

    users.append(new_user)

    return HTMLResponse(
        content="""
            <script>
                alert("가입되었습니다!!");
                location.href = "/member/login";
            </script>
        """,
    )
