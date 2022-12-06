from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

from . import main, member

router = APIRouter()
router.include_router(main.router)
router.include_router(member.router)
