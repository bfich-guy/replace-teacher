from flask import render_template
from blueprint_factory import quantorium_blueprint
from server_config import Endpoints, Templates

@quantorium_blueprint.route(Endpoints.ABOUT.value)
def about() -> str:
    return render_template(Templates.ABOUT.value)