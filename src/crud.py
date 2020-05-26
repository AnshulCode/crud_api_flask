import pymongo
import time
import random


client = pymongo.MongoClient("mongodb://localhost:27017/")
dbs = client["restDB"]
restDB = dbs["db"]
def create(message):
    obj = {"message":message, "_id":random.randrange(1,100)}
    restDB.insert_one(obj)
    return
def retrive(message):
    obj = restDB.find_one({"message":message})
    return obj
def delete(message):
    obj = restDB.find_one({"message": message})
    restDB.delete_one(obj)
    return
def update(id,message):
    obj = restDB.find_one({"_id":id})
    obj["message"] = message
    return obj