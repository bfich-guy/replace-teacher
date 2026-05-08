def two_dicts_are_equal(*, first_dict: dict, second_dict: dict, dict_keys: list[str]) -> bool:

    result_list: list = []

    for key in dict_keys:
        keys_in_dicts_are_equal: bool = first_dict[key] == second_dict[key]
        result_list.append(keys_in_dicts_are_equal)

    result: bool = all(result_list)
    return result