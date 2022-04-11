import json
from pymongo import MongoClient
from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

if __name__ == "__main__":
    app.run(debug=True)

class user_profile(Resource):
    def get(self):
        return {"data": "This is a test for user data (oximeter, bp, etc."}

api.add_resource(user_profile, "/admin")

# based on GFG implementation of storing items into MongoDB. Will proceed to create REstful API successful implementation. 

#For the admin module, want to try and separate the data via name, dob, age, etc. Parse information and then make it available/search by specified fields. 

with open('admin_test') as data:
    admin_data = json.load(data)

client = MongoClient('mongodb://localhost:27022//')

database = client["admin_data"]

admin_client = database["data"]

if isinstance(user_data, list):
    admin_client.insert_many(user_data)
else:
    admin_client.insert_one(user_data) 

