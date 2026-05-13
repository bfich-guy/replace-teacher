from flask import render_template
from blueprint_factory import quantorium_blueprint
from config.server import Endpoints, Templates

@quantorium_blueprint.route(Endpoints.PROFILE.value)
def render_profile() -> str:
    return render_template(Templates.PROFILE.value)