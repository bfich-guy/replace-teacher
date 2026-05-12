from flask import request, jsonify, session
from blueprint_factory import quantorium_blueprint
from server_config import Endpoints, endpoint_database_router, User, Path
from utils import parse_log_in_json, two_dicts_are_equal
from typing import Any

@quantorium_blueprint.route(rule=Endpoints.LOG_IN.value, methods=["GET", "POST"])
def log_in() -> Any:

    current_method: str = request.method

    current_method_is_POST: bool = current_method == "POST"
    current_method_is_GET: bool = current_method == "GET"

    if current_method_is_POST:

        request_data: dict = request.get_json()
        endpoint, file_path, user_input_data, input_id = parse_log_in_json(request_json=request_data)

        existing_or_not_user: User = User(**user_input_data)
        actual_data_in_database: dict = endpoint_database_router[endpoint]["POST"]["read_data_from_database_file"](file_path=file_path, data_id=input_id)
        current_user_is_actually_owner_of_his_account: bool = two_dicts_are_equal(first_dict=existing_or_not_user.__dict__, second_dict=actual_data_in_database, dict_keys=["name", "password", "unique_id"]) #Hardcode
    
        if current_user_is_actually_owner_of_his_account:
            session["user_id"] = existing_or_not_user.unique_id
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"error": "Not Owner"}), 401

    elif current_method_is_GET:
        
        current_user_id: str | None = session.get("user_id")

        if current_user_id is None:
            return jsonify({"error": "Unauthorized"}), 401
        else:
            user_data: dict = endpoint_database_router[Endpoints.LOG_IN.value]["GET"]["read_data_from_database_file"](file_path=Path.USERS.value, data_id=current_user_id)

        return jsonify(user_data), 200



