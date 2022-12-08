from fastapi import APIRouter

from . import todo

router = APIRouter(prefix="/api")
router.include_router(todo.router)
