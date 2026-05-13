from flask import render_template
from blueprint_factory import quantorium_blueprint
from config.server import Endpoints, Templates

@quantorium_blueprint.route(Endpoints.INDEX.value)
def render_index() -> str:
    return render_template(Templates.INDEX.value)