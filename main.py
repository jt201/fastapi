from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/member/login", response_class=HTMLResponse)
async def member_login(request: Request):
    return templates.TemplateResponse("member/login.html", {"request": request})


@app.get("/member/register", response_class=HTMLResponse)
async def member_register(request: Request):
    return templates.TemplateResponse("/member/register.html", {"request": request})
