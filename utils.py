from typing import Any
from config.server import JSONKeys

def get_request_method_from_list(*, request_methods: list) -> str:

    """
    This function **returns request method**: GET or POST from list with only one element like ["GET"] or ["POST"]. 
    If length of list is not equal to 1, function **returns empty string**!
    """

    len_of_request_methods_is_not_one: bool = len(request_methods) != 1

    if len_of_request_methods_is_not_one:
        return ""
    else:
        request_method: str = request_methods[0]
        return request_method

def parse_http_status(status: Any) -> tuple:

    """
    This function **returns HTTP status json and status code** from JSON in format ({"status": "status"}, status_code)
    """

    http_status_dict: dict[str, str] = status[0]
    http_status_code: int = status[1]
    return http_status_dict, http_status_code

def parse_sign_up_json(*, request_json: dict) -> dict:

    """
    This function **returns user input data as a dictionary**.
    """

    user_input_data: dict = request_json[JSONKeys.USER_INPUT_DATA.value]
    
    return user_input_data

def parse_log_in_json(*, request_json: dict) -> tuple[dict, str]:
    
    """
    This function **returns endpoint, user input data as a dictionary** and **user's id**.
    """

    user_input_data: dict = request_json[JSONKeys.USER_INPUT_DATA.value]
    input_id: str = user_input_data[JSONKeys.UNIQUE_ID.value]

    return user_input_data, input_id

def parse_update_profile_json(*, request_json: dict) -> tuple:

    """
    This function **returns new user name and password** from profile page
    """

    new_user_name: str = request_json[JSONKeys.NEW_USER_NAME.value]
    new_user_password: str = request_json[JSONKeys.NEW_USER_PASSWORD.value]

    return new_user_name, new_user_password

def get_equality_of_two_dicts(*, first_dict: dict, second_dict: dict, dict_keys: Any) -> bool:
    
    """
    This function **returns equality of two dicts**. This function iterates by keys in argument *dict_keys* and compares values of that keys in two dicts: *first_dict* and *second_dict*. 
    """

    try:
        result: bool = all(first_dict[key] == second_dict[key] for key in dict_keys)
        return result
    except TypeError:
        return False
    
def all_strings_in_list_are_not_empty(*, string_list: list[str]) -> bool:
    
    """
    This function **returns True** if every string in list is not empty or **False** in opposite case
    """

    try:
        result: bool = all(string for string in string_list)
        return result
    except TypeError:
        return False