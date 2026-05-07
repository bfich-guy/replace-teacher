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
    data: dict = request_data[Auth.USER_DATA.value]

    auth_registry[auth_type](file_path=file_path, data=data)

    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
   app.run(debug=True)