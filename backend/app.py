import json, pymongo
from re import A 
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
from pymongo import MongoClient
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/berkant")
def berkant():
    return "<p>Berkant</p>"

@app.route("/api", methods=["POST"])
@cross_origin(supports_credentials=True)
def api():
    crn = json.loads(request.data)["crn"]
    token = json.loads(request.data)["token"]
    crn_list = crn.split(",")
    print("Requested CRN: ", crn_list)
    print("Token: ",token)

    cluster = MongoClient("mongodb+srv://berrkantt:Beko.mongo.3998@requests.5l5puag.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["CRNKapar"]
    collection = db["CRNKapar_Requests"]
    post = {"CRN" : crn, "Token" : token, "Date" : dt_string}
    collection.insert_one(post)
    return "<p>API</p>"

if __name__ == '__main__':
    app.run()
