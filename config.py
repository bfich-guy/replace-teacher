from enum import Enum
from database.db_crud import db
from typing import Any

auth_registry: dict[str, dict[str, Any]] = {
    "sign_up": {
        "get_max_id": db.get_max_id,
        "create_data": db.create_data,
    },

    "log_in": {
        "read_data": db.read_data,
    },
}

class Status(Enum):
    SUCCESS = ({"status": "success"}, 200)
    FORBIDDEN = ({"status": "forbidden"}, 403)

class Auth(Enum):
    AUTH_TYPE = "auth_type"
    FILE_PATH = "file_path"
    USER_INPUT_DATA = "user_input_data"
    UNIQUE_ID = "unique_id"
    STATUS = "status"

class Endpoints(Enum):
    INDEX = "/"
    SIGN_UP = "/sign_up"
    LOG_IN = "/log_in"
    METHODOLOGIC = "/methodologic"

class Templates(Enum):
    INDEX = "index.html"
    METHODOLOGIC = "methodologic.html"

class User:
    def __init__(self, *,
                 name: str | None,
                 password: str | None,
                 status: str | None,
                 unique_id: str | None,
                 ) -> None:
        
        self.name: str | None = name
        self.password: str | None = password
        self.status: str | None = status
        self.unique_id: str | None = unique_id

class Lesson:
    def __init__(self, *,
                 topic: str | None,
                 info: str | None,
                 ) -> None:
        
        self.topic: str | None = topic
        self.info: str | None = info