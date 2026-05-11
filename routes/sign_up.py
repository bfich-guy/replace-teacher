from flask import request, Response, jsonify
from blueprint_factory import quantorium_blueprint
from server_config import Endpoints, auth_registry, User, HTTPStatus
from utils import parse_sign_up_json, parse_http_status

@quantorium_blueprint.route(rule=Endpoints.SIGN_UP.value, methods=["POST"])
def sign_up() -> tuple[Response, int]:

    request_data: dict = request.get_json()
    auth_type, file_path, user_input_data = parse_sign_up_json(request_json=request_data)

    user_primary_key: str = str(auth_registry[auth_type]["read_primary_key"]())
    user_input_data["unique_id"] = user_primary_key
    new_user: User = User(**user_input_data)
    auth_registry[auth_type]["create_data_in_database_file"](file_path=file_path, data=new_user.__dict__)

    http_status_dict, http_status_code = parse_http_status(status=HTTPStatus.SUCCESS.value)
    jsonified_http_status = jsonify(http_status_dict)

    return jsonified_http_status, http_status_code