from flask import render_template
from blueprint_factory import quantorium_blueprint
from config.server import Endpoints, Templates

@quantorium_blueprint.route(Endpoints.INDUSTRIAL_ROBOTICS.value)
def render_industrial_robotics() -> str:
    return render_template(Templates.INDUSTRIAL_ROBOTICS.value)