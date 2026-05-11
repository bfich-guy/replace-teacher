from flask import request, Response, jsonify
from blueprint_factory import quantorium_blueprint
from server_config import Endpoints, auth_registry, User, HTTPStatus
from utils import parse_log_in_json, parse_http_status, two_dicts_are_equal

@quantorium_blueprint.route(rule=Endpoints.LOG_IN.value, methods=["POST"])
def log_in() -> tuple[Response, int]:

    request_data: dict = request.get_json()
    auth_type, file_path, user_input_data, input_id = parse_log_in_json(request_json=request_data)

    existing_or_not_user: User = User(**user_input_data)
    actual_data_in_database: dict = auth_registry[auth_type]["read_data_from_database_file"](file_path=file_path, data_id=input_id)
    current_user_is_actually_owner_of_his_account: bool = two_dicts_are_equal(first_dict=existing_or_not_user.__dict__, second_dict=actual_data_in_database, dict_keys=["name", "password", "unique_id"]) #Hardcode
    
    if current_user_is_actually_owner_of_his_account:
        http_status_dict, http_status_code = parse_http_status(status=HTTPStatus.SUCCESS.value)
        jsonified_http_status = jsonify(http_status_dict)

        return jsonified_http_status, http_status_code
    else:
        http_status_dict, http_status_code = parse_http_status(status=HTTPStatus.FORBIDDEN.value)
        jsonified_http_status = jsonify(http_status_dict)

        return jsonified_http_status, http_status_code