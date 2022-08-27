import pymongo
import json
from logging_class import lg

#load Excel dataset attribute_dress as JSON from sql and push to mongodb

try:
    client = pymongo.MongoClient("mongodb+srv://Shriram:loveline123@shriramm.7irhy.mongodb.net/?retryWrites=true&w=majority")
    db = client.test

    with open(r"C:\Users\shriramm\attribute.json") as file:
        data = [(json.load(file))]

    db = client['dress']
    collection = db["attribute_dress"]

    collection.insert_many(data)
    lg.info("data push success")

except Exception as e:

    lg.error(e)