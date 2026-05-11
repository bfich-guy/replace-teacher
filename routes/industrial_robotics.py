from flask import render_template
from blueprint_factory import quantorium_blueprint
from server_config import Endpoints, Templates

@quantorium_blueprint.route(Endpoints.INDUSTRIAL_ROBOTICS.value)
def industrial_robotics() -> str:
    return render_template(Templates.INDUSTRIAL_ROBOTICS.value)