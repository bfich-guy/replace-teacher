from flask import request, jsonify, session
from blueprint_factory import quantorium_blueprint
from config.server import endpoint_database_router, log_in_fields, HTTPStatus, Endpoints, RequestMethods, SessionKeys
from config.database import DatabaseFilePath, DatabaseMethodsNames, User
from utils import parse_http_status, get_request_method_from_list, parse_log_in_json, get_equality_of_two_dicts
from typing import Any

@quantorium_blueprint.route(rule=Endpoints.LOG_IN.value, methods=RequestMethods.POST.value)
def log_in() -> Any:

    current_request_method: str = request.method

    current_request_method_is_POST: bool = current_request_method == get_request_method_from_list(request_methods=RequestMethods.POST.value)
    current_request_method_is_GET: bool = current_request_method == get_request_method_from_list(request_methods=RequestMethods.GET.value)

    if current_request_method_is_POST:

        POST: str = get_request_method_from_list(request_methods=RequestMethods.POST.value)

        request_data: dict = request.get_json()
        user_input_data, input_id = parse_log_in_json(request_json=request_data)

        existing_or_not_user: User = User(**user_input_data)
        actual_user_data_in_database: dict = endpoint_database_router[Endpoints.LOG_IN.value][POST][DatabaseMethodsNames.READ_DATA.value](file_path=DatabaseFilePath.USERS.value, data_id=input_id)
        current_user_is_actually_owner_of_his_account: bool = get_equality_of_two_dicts(first_dict=existing_or_not_user.__dict__, 
                                                                                        second_dict=actual_user_data_in_database, 
                                                                                        dict_keys=log_in_fields,
                                                                                        )
    
        if current_user_is_actually_owner_of_his_account:

            session[SessionKeys.USER_ID.value] = existing_or_not_user.unique_id
                        
            http_status_dict, http_status_code = parse_http_status(status=HTTPStatus.SUCCESS.value)
            return jsonify(http_status_dict), http_status_code
        
        else:

            http_status_dict, http_status_code = parse_http_status(status=HTTPStatus.NOT_AUTHORIZED.value)
            return jsonify(http_status_dict), http_status_code