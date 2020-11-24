import flask
import json
from config import host, port
from flask import Response, request
from api.controller import homeController

app = flask.Flask(__name__)

# Uncomment the following line to turn off the
# debugging mode
# app.config["DEBUG"] = False

# The route is defined below which call its respective controller function.
# After receiving data response from the controller, they return the response with appropriate response code.


@app.route("/", methods=["GET"])
def home():
    data = homeController(URL=request.args["src"])
    return Response(json.dumps(data["message"]), status=data["code"])


app.run(host=host, port=port)
