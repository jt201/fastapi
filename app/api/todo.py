from fastapi import APIRouter, Body, HTTPException

from app.data import data, TodoItem

router = APIRouter(prefix="/todo", tags=["TODO"])


@router.post("/", response_model=bool)
def todo_create_item(content: str = Body(embed=True)) -> bool:
    if not content:
        raise HTTPException(200, detail="내용을 입력해주세요!!")

    if content in [item.content for item in data]:
        raise HTTPException(200, detail="이미 등록된 데이터 입니다!!")

    new_item: TodoItem = TodoItem(content)
    data.append(new_item)

    return new_item in data


@router.put("/{todo_id}", response_model=bool)
def todo_toggle_status_item(todo_id: int) -> bool:
    ids: list[int] = [item.id for item in data]

    if not todo_id in ids:
        raise HTTPException(200, detail="아이템을 찾을 수 없습니다!!")

    idx: int = ids.index(todo_id)

    data[idx].status = not data[idx].status

    return True


@router.delete("/{todo_id}", response_model=bool)
def todo_remove_item(todo_id: int) -> bool:
    ids: list[int] = [item.id for item in data]
    idx: int = ids.index(todo_id)

    data.pop(idx)

    return True
