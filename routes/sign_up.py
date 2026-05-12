from flask import request, Response, jsonify, session
from blueprint_factory import quantorium_blueprint
from server_config import Endpoints, endpoint_database_router, User, Path
from utils import parse_sign_up_json
from typing import Any

@quantorium_blueprint.route(rule=Endpoints.SIGN_UP.value, methods=["GET", "POST"])
def sign_up() -> Any:

    current_method: str = request.method

    current_method_is_POST: bool = current_method == "POST"
    current_method_is_GET: bool = current_method == "GET"

    if current_method_is_POST:

        request_data: dict = request.get_json()
        endpoint, file_path, user_input_data = parse_sign_up_json(request_json=request_data)

        user_primary_key: str = str(endpoint_database_router[endpoint]["POST"]["read_primary_key"]())
        user_input_data["unique_id"] = user_primary_key
        new_user: User = User(**user_input_data)
        endpoint_database_router[endpoint]["POST"]["create_data_in_database_file"](file_path=file_path, data=new_user.__dict__)

        session["user_id"] = new_user.unique_id

        return jsonify(new_user.__dict__), 200

    elif current_method_is_GET:
        current_user_id: str | None = session.get("user_id")

        if current_user_id is None:
            return jsonify({"error": "Unauthorized"}), 401

        user_data: dict = endpoint_database_router[Endpoints.SIGN_UP.value]["GET"]["read_data_from_dataase_file"](file_path=Path.USERS.value, data_id=current_user_id)

        return jsonify(user_data), 200