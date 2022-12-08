from fastapi import APIRouter

from main import data, TodoItem

router = APIRouter(prefix="/todo")


@router.delete("/{todo_id}", response_model=bool)
def todo_remove_item(todo_id: int) -> bool:
    ids: list[int] = [item.id for item in data]
    idx: int = ids.index(todo_id)

    data.pop(idx)

    return True
