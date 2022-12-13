from uuid import uuid4
from fastapi import APIRouter, Request, Form, Depends, Cookie
from fastapi.responses import HTMLResponse, RedirectResponse

from . import templates
from main import users, User, sessions, with_auth

router = APIRouter(prefix="/member")


@router.get("/logout")
async def member_logout(todo_session_id: str = Cookie("")):
    if todo_session_id and todo_session_id in sessions.keys():
        del sessions[todo_session_id]

    response = RedirectResponse("/", status_code=303)
    response.delete_cookie(key="todo_session_id")

    return response


@router.get("/login", response_class=HTMLResponse)
async def member_login(request: Request):
    return templates.TemplateResponse("member/login.html", {"request": request})


@router.post("/login", response_class=HTMLResponse | RedirectResponse)
async def member_login_proc(
    email: str = Form(""),
    password: str = Form(""),
    user: User = Depends(with_auth),
):
    if user is not None:
        return RedirectResponse("/", status_code=303)

    find_users = [user for user in users if user.email == email and user.password == password]

    if find_users:
        session_id = str(uuid4())
        user = find_users[0]

        sessions[session_id] = user
        response = RedirectResponse("/", status_code=303)
        response.set_cookie(key="todo_session_id", value=session_id, httponly=True)

        return response

    return HTMLResponse(
        content="""
            <script>
                alert("해당 사용자를 찾을 수 없습니다!!");
                history.back();
            </script>
        """,
    )


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
