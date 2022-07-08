from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
import json
app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def hello_world():
    print("berkant malı")
    return "<p>Hello, World!</p>"


@app.route("/berkant")
def berkant():
    return "<p>Berkant</p>"


@app.route("/api", methods=["POST"])
def api():
    crn = json.loads(request.data)["crn"]
    token = json.loads(request.data)["token"]
    crn_list = crn.split(",")
    print(crn_list)
    print(token)
    return "<p>API</p>"


if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
