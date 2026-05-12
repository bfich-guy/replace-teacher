from typing import Any

def parse_http_status(status: tuple[dict[str, str], int]) -> tuple:

    """
    **Returns HTTP status json and status code** from JSON like ({"status": "status"}, status_code)
    """

    http_status_dict: dict[str, str] = status[0]
    http_status_code: int = status[1]
    return http_status_dict, http_status_code

def parse_sign_up_json(*, request_json: dict) -> tuple:

    """
    **Returns authentication type, name of file in database and user data**.
    """

    endpoint: str = request_json["endpoint"]
    file_path: str = request_json["file_path"]
    user_input_data: dict = request_json["user_input_data"]
    
    return endpoint, file_path, user_input_data

def parse_log_in_json(*, request_json: dict) -> Any:
    
    """
    **Returns authentication type, name of file in database, user data and his id**.
    """

    endpoint: str = request_json["endpoint"]
    file_path: str = request_json["file_path"]
    user_input_data: dict = request_json["user_input_data"]
    input_id: str = user_input_data["unique_id"]

    return endpoint, file_path, user_input_data, input_id

def two_dicts_are_equal(*, first_dict: dict, second_dict: dict, dict_keys: Any) -> bool:
    
    """
    **Returns equality of two dicts**. This function iterates by keys in argument *dict_keys* and compares values of that keys in two dicts: *first_dict* and *second_dict*. 
    """

    result_list: list = []

    try:
        for key in dict_keys:
            keys_in_dicts_are_equal: bool = first_dict[key] == second_dict[key]
            result_list.append(keys_in_dicts_are_equal)

        result: bool = all(result_list)
        return result
    except TypeError:
        return False