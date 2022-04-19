import json
import jsonschema
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


#For the admin module, want to try and separate the data via name, dob, age, etc. Parse information and then make it available/search by specified fields. 

# Standard format for the json file is provided for comparison of received data. 

standard_schema_admin = json.load("schema")

# function for validating the admin data format as specified by the schema.json file.

def validate_admin_format():
    admin_data = json.loads("admin_test")
    jsonschema.validate(admin_data, standard_schema_admin)
    

with open('admin_test') as data:
    admin_data = json.load(data)

client = MongoClient('mongodb://localhost:27022//')

database = client["admin_data"]

admin_client = database["data"]

if isinstance(admin_data, list):
    admin_client.insert_many(admin_data)
else:
    admin_client.insert_one(admin_data) 

