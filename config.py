from enum import Enum
from database.db_crud import db
from typing import Any

auth_registry: dict[str, Any] = {
    "sign_up": db.create_data, 
}

class Auth(Enum):
    AUTH_TYPE = "auth_type"
    FILE_PATH = "file_path"
    USER_DATA = "user_data"

class Endpoints(Enum):
    INDEX = "/"
    AUTH = "/auth"

class Templates(Enum):
    INDEX = "index.html"

class DatabaseFileNames(Enum):
    LESSONS = "database/lessons.json"
    USERS = "database/users.json"

class User:
    def __init__(self, *,
                 name: str | None,
                 password: str | None,
                 status: str | None,
                 ) -> None:
        
        self.name: str | None = name
        self.password: str | None = password
        self.status: str | None = status
        self.unique_id: str | None = "0"

class Lesson:
    def __init__(self, *,
                 topic: str | None,
                 info: str | None,
                 ) -> None:
        
        self.topic: str | None = topic
        self.info: str | None = info