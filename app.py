from flask import Flask
from blueprint_factory import quantorium_blueprint
from routes import index, industrial_robotics, log_in, methodologic, profile, sign_up

app: Flask = Flask(__name__)
app.register_blueprint(blueprint=quantorium_blueprint)

if __name__ == "__main__":
   app.run(debug=True)