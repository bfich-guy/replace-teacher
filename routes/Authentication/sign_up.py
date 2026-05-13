from flask import request, jsonify, session
from blueprint_factory import quantorium_blueprint
from config.server import endpoint_database_router, HTTPStatus, Endpoints, RequestMethods, JSONKeys, SessionKeys
from config.database import DatabaseFilePath, DatabaseMethodsNames, User
from utils import get_request_method_from_list, parse_http_status, parse_sign_up_json
from typing import Any

@quantorium_blueprint.route(rule=Endpoints.SIGN_UP.value, methods=RequestMethods.POST.value)
def sign_up() -> Any:

    current_method: str = request.method

    current_method_is_POST: bool = current_method == get_request_method_from_list(request_methods=RequestMethods.POST.value)
    current_method_is_GET: bool = current_method == get_request_method_from_list(request_methods=RequestMethods.GET.value)

    if current_method_is_POST:

        POST: str = get_request_method_from_list(request_methods=RequestMethods.POST.value)

        request_data: dict = request.get_json()
        user_input_data: dict = parse_sign_up_json(request_json=request_data)

        user_primary_key: str = str(endpoint_database_router[Endpoints.SIGN_UP.value][POST][DatabaseMethodsNames.READ_PRIMARY_KEY.value]())
        user_input_data[JSONKeys.UNIQUE_ID.value] = user_primary_key
        new_user: User = User(**user_input_data)
        endpoint_database_router[Endpoints.SIGN_UP.value][POST][DatabaseMethodsNames.CREATE_DATA.value](file_path=DatabaseFilePath.USERS.value, data=new_user.__dict__)

        session[SessionKeys.USER_ID.value] = new_user.unique_id

        http_status_dict, http_status_code = parse_http_status(status=HTTPStatus.SUCCESS.value)
        return jsonify(http_status_dict), http_status_code