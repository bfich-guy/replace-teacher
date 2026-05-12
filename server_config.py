from enum import Enum
from database.database import db
from typing import Any

endpoint_database_router: dict[str, dict[str, Any]] = {
    "/sign_up": {
        "GET": {
            "read_data_from_dataase_file": db.read_data_from_database_file,
        },
        "POST": {
            "read_primary_key": db.read_primary_key,
            "create_data_in_database_file": db.create_data_in_database_file,
        },
    },

    "/log_in": {
        "GET": {
            "read_data_from_database_file": db.read_data_from_database_file,
        },
        "POST": {
            "read_data_from_database_file": db.read_data_from_database_file,
        },
    },
}

class HTTPStatus(Enum):
    SUCCESS = ({"status": "success"}, 200)
    FORBIDDEN = ({"status": "forbidden"}, 403)

class Endpoints(Enum):
    INDEX = "/"

    SIGN_UP = "/sign_up"
    LOG_IN = "/log_in"

    METHODOLOGIC = "/methodologic"
    INDUSTRIAL_ROBOTICS = "/industrial_robotics"

    PROFILE = "/profile"
    UPDATE_PROFILE = "/update_profile"
    DELETE_PROFILE = "/delete_profile"

    ABOUT = "/about"

class Templates(Enum):
    INDEX = "index.html"
    METHODOLOGIC = "methodologic.html"
    PROFILE = "profile.html"
    
    INDUSTRIAL_ROBOTICS = "methodologic/industrial_robotics.html"

    ABOUT = "about.html"

class Path(Enum):
    USERS = "database/users.json"

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