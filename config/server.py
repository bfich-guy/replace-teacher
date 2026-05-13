from enum import Enum
from database.database import db
from typing import Any
from dotenv import load_dotenv
from config.database import DatabaseMethodsNames
import os

load_dotenv()

secret_key: str | None = os.getenv("FLASK_SECRET_KEY", "FLASK_SECRET_KEY")
debug: bool = os.getenv("FLASK_DEBUG", "False").strip().lower() in ("true", "1", "t")

log_in_fields: list[str] = ["name", "password", "unique_id"]

class HTTPStatus(Enum):
    SUCCESS = ({"status": "success"}, 200)
    NOT_AUTHORIZED = ({"status": "not_authorized"}, 401)
    FORBIDDEN = ({"status": "forbidden"}, 403)

class Endpoints(Enum):
    INDEX = "/"

    SIGN_UP = "/sign_up"
    LOG_IN = "/log_in"

    MAIN = "/main"
    INDUSTRIAL_ROBOTICS = "/industrial_robotics"

    PROFILE = "/profile"
    UPDATE_PROFILE = "/update_profile"
    DELETE_PROFILE = "/delete_profile"

    ABOUT = "/about"

class RequestMethods(Enum):
    GET = ["GET"]
    POST = ["POST"]
    ALL = ["GET", "POST"]

class Templates(Enum):
    INDEX = "index.html"
    MAIN = "main.html"
    PROFILE = "profile.html"
    
    INDUSTRIAL_ROBOTICS = "methodologic/industrial_robotics.html"

    ABOUT = "about.html"

class JSONKeys(Enum):
    SIGN_UP_ENDPOINT = "sign_up_endpoint"
    LOG_IN_ENDPOINT = "log_in_endpoint"
    UPDATE_PROFILE_ENDPOINT = "update_profile_endpoint"
    USER_INPUT_DATA = "user_input_data"
    NAME = "name"
    NEW_USER_NAME = "new_user_name"
    PASSWORD = "password"
    NEW_USER_PASSWORD = "new_user_password"
    STATUS = "status"
    UNIQUE_ID = "unique_id"

class SessionKeys(Enum):
    USER_ID = "user_id"

endpoint_database_router: dict[str, dict[str, Any]] = {

    Endpoints.SIGN_UP.value: {
        RequestMethods.GET.value[0]: {
            DatabaseMethodsNames.READ_DATA.value: db.read_data_from_database_file,
        },
        RequestMethods.POST.value[0]: {
            DatabaseMethodsNames.READ_PRIMARY_KEY.value: db.read_primary_key,
            DatabaseMethodsNames.CREATE_DATA.value: db.create_data_in_database_file,
        },
    },

    Endpoints.LOG_IN.value: {
        RequestMethods.GET.value[0]: {
            DatabaseMethodsNames.READ_DATA.value: db.read_data_from_database_file,
        },
        RequestMethods.POST.value[0]: {
            DatabaseMethodsNames.READ_DATA.value: db.read_data_from_database_file,
        },
    },

    Endpoints.UPDATE_PROFILE.value: {
        RequestMethods.GET.value[0]: {
            DatabaseMethodsNames.READ_DATA.value: db.read_data_from_database_file,
        },
        RequestMethods.POST.value[0]: {
            DatabaseMethodsNames.READ_DATA.value: db.read_data_from_database_file,
            DatabaseMethodsNames.UPDATE_DATA.value: db.update_data_in_database_file,
        },
    },

    Endpoints.DELETE_PROFILE.value: {
        RequestMethods.GET.value[0]: {
            DatabaseMethodsNames.DELETE_DATA.value: db.delete_data_from_database_file,
        },
        RequestMethods.POST.value[0]: {
            
        },
    },

}