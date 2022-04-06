from pymongo import MongoClient
from .environment_variables import mongo_url

connection_string = mongo_url
client = MongoClient(connection_string)
database = client.finance_app
collection = database.users


def get_all_users() -> list[dict]:
    return list(collection.find({}, {'_id': False}))
