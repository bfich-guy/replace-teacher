from flask import Flask
from blueprint_factory import quantorium_blueprint
from routes.Authentication.sign_up import sign_up
from routes.Authentication.log_in import log_in
from routes.Profile.update_profile import update_profile
from routes.Profile.delete_profile import delete_profile
from routes.Templates.about import render_about
from routes.Templates.index import render_index
from routes.Templates.main import render_main
from routes.Templates.profile import render_profile
from routes.Templates.methodologic.industrial_robotics import render_industrial_robotics
from config.server import secret_key, debug

app: Flask = Flask(__name__)
app.register_blueprint(blueprint=quantorium_blueprint)
app.secret_key = secret_key

if __name__ == "__main__":
   app.run(debug=debug)