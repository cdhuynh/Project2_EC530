import json
from pymongo import MongoClient
from flask import Flask
from flask_restful import Api, Resource

# My goal here is to take one module and create the other modules based on a single implementation rather than reinventing the wheel.
# At that point, we modify each module based on individual needs. 

app = Flask(__name__)
api = Api(app)

if __name__ == "__main__":
    app.run(debug=True)

class user_profile(Resource):
    def get(self):
        return {"data": "This is a test for user data (oximeter, bp, etc."}

api.add_resource(user_profile, "/user")

# based on GFG implementation of storing items into MongoDB. Will proceed to create REstful API successful implementation. 

#For the user module, want to try and separate the data via blood pressure, oximeter, etc. 

with open('user_profile') as data:
    user_data = json.load(data)

client = MongoClient('mongodb://localhost:27022//')

database = client["user_data"]

user_client = database["data"]

if isinstance(user_data, list):
    user_client.insert_many(user_data)
else:
    user_client.insert_one(user_data) 

