from flask import Flask, render_template, request, jsonify, Response, session
from config import Endpoints, Templates, User, auth_registry, Auth, Status
from utils import two_dicts_are_equal

app: Flask = Flask(__name__)
app.secret_key = "secret_key"

@app.route(Endpoints.INDEX.value)
def index() -> str:
    return render_template(Templates.INDEX.value)

@app.route(Endpoints.SIGN_UP.value, methods=["POST"])
def sign_up() -> tuple[Response, int]:

    request_data: dict = request.get_json()
    auth_type: str = request_data[Auth.AUTH_TYPE.value]
    file_path: str = request_data[Auth.FILE_PATH.value]
    user_input_data: dict = request_data[Auth.USER_INPUT_DATA.value]

    max_id: str = str(auth_registry[auth_type]["get_max_id"]())
    user_input_data[Auth.UNIQUE_ID.value] = max_id

    new_user: User = User(**user_input_data)
    auth_registry[auth_type]["create_data"](file_path=file_path, data=new_user.__dict__)

    session["user_data"] = new_user.__dict__
    
    return jsonify(Status.SUCCESS.value[0]), Status.SUCCESS.value[1]

@app.route(Endpoints.LOG_IN.value, methods=["POST"])
def log_in() -> tuple[Response, int]:

    request_data: dict = request.get_json()
    auth_type: str = request_data[Auth.AUTH_TYPE.value]
    file_path: str = request_data[Auth.FILE_PATH.value]
    user_input_data: dict = request_data[Auth.USER_INPUT_DATA.value]

    user_id: int = int(user_input_data["unique_id"])
    user_actual_data: dict = auth_registry[auth_type]["read_data"](file_path=file_path, data_id=user_id)
    
    user_input_data_is_equal_to_user_actual_data: bool = two_dicts_are_equal(first_dict=user_input_data,
                                                                             second_dict=user_actual_data,
                                                                             dict_keys=["name", "password", "unique_id"],
                                                                             )

    if user_input_data_is_equal_to_user_actual_data:
        return jsonify(Status.SUCCESS.value[0]), Status.SUCCESS.value[1]
    else:
        return jsonify(Status.FORBIDDEN.value[0]), Status.FORBIDDEN.value[1]
    
@app.route(Endpoints.METHODOLOGIC.value)
def methodologic() -> str:
    return render_template(Templates.METHODOLOGIC.value)

if __name__ == "__main__":
   app.run(debug=True)