from concurrent.futures import thread
import json
from threading import Thread
import jsonschema
import tkinter
from pymongo import MongoClient
from flask import Flask
from flask_restful import Api, Resource
import requests

# For the admin module, want to parse information and then make it available/search by specified fields.


app = Flask(__name__)
api = Api(app)

if __name__ == "__main__":
    app.run(debug=True)


class user_profile(Resource):
    def get(self):
        return {"data": "This is a test for patient data (dob, name, age."}


api.add_resource(user_profile, "/main")


# Define the user or admin selection (via tkinter for simplicity):

admin = 1
user = 2

# Based on selection, call the api module - either user or admin. 


def admin_thread():
    response = requests.get("http://127.0.0.1:5000/admin")
    if(response.status_code == 404):
        return
    return


def user_thread():
    response = requests.get("http://127.0.0.1:5000/user")
    if(response.status_code == 404):
        return
    return


if(admin):
    t_admin = Thread(target=admin_thread)
    t_admin.start()

if(user):
    t_user = Thread(target=user_thread)
    t_user.start()
