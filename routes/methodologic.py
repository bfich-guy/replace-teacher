from flask import render_template
from blueprint_factory import quantorium_blueprint
from server_config import Endpoints, Templates

@quantorium_blueprint.route(Endpoints.METHODOLOGIC.value)
def methodologic() -> str:
    return render_template(Templates.METHODOLOGIC.value)