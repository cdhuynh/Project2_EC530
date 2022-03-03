import json
from pymongo import MongoClient
from flask import Flask


# based on GFG implementation of storing items into MongoDB. Will proceed to create REstful API successful implementation. 

with open('chat_message') as message:
    chat_message = json.load(message)

client = MongoClient('mongodb://localhost:27022//')

database = client["chat_client"]

chat_client = database["data"]

if isinstance(chat_message, list):
    chat_client.insert_many(chat_message)
else:
    chat_client.insert_one(chat_message)