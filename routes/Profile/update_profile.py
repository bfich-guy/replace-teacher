from flask import request, jsonify, session
from blueprint_factory import quantorium_blueprint
from config.server import endpoint_database_router, HTTPStatus, Endpoints, RequestMethods, JSONKeys, SessionKeys
from config.database import DatabaseFilePath, DatabaseMethodsNames, User
from utils import get_request_method_from_list, parse_http_status, parse_update_profile_json, all_strings_in_list_are_not_empty
from typing import Any

@quantorium_blueprint.route(rule=Endpoints.UPDATE_PROFILE.value, methods=RequestMethods.ALL.value)
def update_profile() -> Any:

    current_request_method: str = request.method

    current_request_method_is_POST: bool = current_request_method == get_request_method_from_list(request_methods=RequestMethods.POST.value)
    current_request_method_is_GET: bool = current_request_method == get_request_method_from_list(request_methods=RequestMethods.GET.value)

    if current_request_method_is_POST:

        POST: str = get_request_method_from_list(request_methods=RequestMethods.POST.value)

        request_data: Any = request.get_json()
        new_user_name, new_user_password = parse_update_profile_json(request_json=request_data)

        input_is_not_valid: bool = not all_strings_in_list_are_not_empty(string_list=[new_user_name, new_user_password])

        current_user_id: str | None = session.get(SessionKeys.USER_ID.value)

        if current_user_id is None or input_is_not_valid:

            http_status_dict, http_status_code = parse_http_status(status=HTTPStatus.NOT_AUTHORIZED.value)
            return jsonify(http_status_dict), http_status_code
            
        else:

            user_data: dict | None = endpoint_database_router[Endpoints.UPDATE_PROFILE.value][POST][DatabaseMethodsNames.READ_DATA.value](file_path=DatabaseFilePath.USERS.value, data_id=current_user_id)

            if user_data is None:

                http_status_dict, http_status_code = parse_http_status(status=HTTPStatus.NOT_AUTHORIZED.value)
                return jsonify(http_status_dict), http_status_code
                
            else:

                user_status: str = user_data["status"]

                if user_status is None:

                    http_status_dict, http_status_code = parse_http_status(status=HTTPStatus.NOT_AUTHORIZED.value)
                    return jsonify(http_status_dict), http_status_code
                
                else:

                    updated_user: User = User(name=new_user_name, password=new_user_password, status=user_status, unique_id=current_user_id)
                    endpoint_database_router[Endpoints.UPDATE_PROFILE.value][POST][DatabaseMethodsNames.UPDATE_DATA.value](file_path=DatabaseFilePath.USERS.value, data=updated_user.__dict__, data_id=current_user_id)
                    updated_user.password = None

                    http_status_dict, http_status_code = parse_http_status(status=HTTPStatus.SUCCESS.value)
                    return jsonify(http_status_dict), http_status_code
    
    elif current_request_method_is_GET:

        GET: str = get_request_method_from_list(request_methods=RequestMethods.GET.value)

        user_id: str | None = session[SessionKeys.USER_ID.value]

        if user_id is None:

            http_status_dict, http_status_code = parse_http_status(HTTPStatus.NOT_AUTHORIZED.value)
            return jsonify(http_status_dict), http_status_code
        
        else:

            user_updated_data: dict | None = endpoint_database_router[Endpoints.UPDATE_PROFILE.value][GET][DatabaseMethodsNames.READ_DATA.value](file_path=DatabaseFilePath.USERS.value, data_id=user_id)

            if user_updated_data is None:

                http_status_dict, http_status_code = parse_http_status(status=HTTPStatus.NOT_AUTHORIZED.value)
                return jsonify(http_status_dict), http_status_code
            
            else:

                updated_user: User = User(**user_updated_data)
                updated_user.password = None

                http_status = parse_http_status(HTTPStatus.SUCCESS.value)
                http_status_code: int = http_status[1]
                return jsonify(updated_user.__dict__), http_status_code