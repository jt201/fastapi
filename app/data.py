from fastapi import Cookie
from datetime import datetime
from typing import List, Dict, Optional


class TodoItem:
    id: int
    content: str
    author: str
    status: bool
    created: datetime

    def __init__(self, content: str = ""):
        self.id = 1 if len(data) == 0 else max([item.id for item in data])
        self.content = content
        self.author = "201"
        self.status = False
        self.created = datetime.now()


class User:
    id: int
    name: str
    email: str
    password: str

    def __init__(self, name: str, email: str, password: str):
        self.id = 1 if len(users) == 0 else max([item.id for item in users])
        self.name = name
        self.email = email
        self.password = password


data: List[TodoItem] = []
users: List[User] = []
sessions: Dict[str, User] = {}


def with_auth(todo_session_id: str = Cookie("")) -> Optional[User]:
    if todo_session_id and todo_session_id in sessions.keys():
        return sessions[todo_session_id]
    return None
