from flask import render_template
from blueprint_factory import quantorium_blueprint
from config.server import Endpoints, Templates

@quantorium_blueprint.route(Endpoints.ABOUT.value)
def render_about() -> str:
    return render_template(Templates.ABOUT.value)