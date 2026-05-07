from flask import Flask, render_template, request, jsonify, Response
from config import Endpoints, Templates, DatabaseFileNames, User, auth_registry, Auth
from typing import Callable

app: Flask = Flask(__name__)

@app.route(Endpoints.INDEX.value)
def index() -> str:
    return render_template(Templates.INDEX.value)

@app.route(Endpoints.AUTH.value, methods=["POST"])
def sign_up() -> tuple[Response, int]:

    request_data: dict = request.get_json()
    auth_type: str = request_data[Auth.AUTH_TYPE.value]
    file_path: str = request_data[Auth.FILE_PATH.value]
    user_db_data: dict = request_data[Auth.USER_DB_DATA.value]

    user_id: int = auth_registry[auth_type][0](file_path=file_path, data=user_db_data)
    user_status: str = auth_registry[auth_type][1](file_path=file_path, data_id=user_id)[Auth.STATUS.value]

    responce: dict = {
        "user_id": user_id,
        "user_status": user_status,
    }

    jsonified_responce: Response = jsonify(responce)
    https_status: int = 200
    return jsonified_responce, https_status

@app.route(Endpoints.METHODOLOGIC.value)
def methodologic() -> str:
    return render_template(Templates.METHODOLOGIC.value)

if __name__ == "__main__":
   app.run(debug=True)