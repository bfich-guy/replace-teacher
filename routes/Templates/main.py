from flask import render_template
from blueprint_factory import quantorium_blueprint
from config.server import Endpoints, Templates

@quantorium_blueprint.route(Endpoints.MAIN.value)
def render_main() -> str:
    return render_template(Templates.MAIN.value)