from flask import request, jsonify, session
from blueprint_factory import quantorium_blueprint
from config.server import endpoint_database_router, HTTPStatus, Endpoints, RequestMethods, SessionKeys
from config.database import DatabaseFilePath, DatabaseMethodsNames
from utils import get_request_method_from_list, parse_http_status
from typing import Any

@quantorium_blueprint.route(rule=Endpoints.DELETE_PROFILE.value, methods=RequestMethods.GET.value)
def delete_profile() -> Any:

    current_request_method: str = request.method

    current_request_method_is_POST: bool = current_request_method == get_request_method_from_list(request_methods=RequestMethods.POST.value)
    current_request_method_is_GET: bool = current_request_method == get_request_method_from_list(request_methods=RequestMethods.GET.value)

    if current_request_method_is_GET:

        GET: str = get_request_method_from_list(request_methods=RequestMethods.GET.value)

        user_id: str | None = session.get(SessionKeys.USER_ID.value)
        
        if user_id is None:

            http_status_dict, http_status_code = parse_http_status(status=HTTPStatus.NOT_AUTHORIZED.value)
            return jsonify(http_status_dict), http_status_code
        
        else:

            endpoint_database_router[Endpoints.DELETE_PROFILE.value][GET][DatabaseMethodsNames.DELETE_DATA.value](file_path=DatabaseFilePath.USERS.value, data_id=user_id, delete_confirm=True)

            http_status_dict, http_status_code = parse_http_status(status=HTTPStatus.SUCCESS.value)
            return jsonify(http_status_dict), http_status_code
