from pymongo import MongoClient
from environment_variables import mongo_url
from server.data_access_layer.abstract_classes.user_dao import UserDAO
from server.entities.user import User
from typing import List
from bson.objectid import ObjectId

# database connection -------------
connection_string = mongo_url
client = MongoClient(connection_string)
database = client.finance_app
collection = database.users


class UserDAOImp(UserDAO):
    def create_new_user(self, user: User) -> dict:
        return collection.insert_one(user)

    def get_user_by_id(self, user_id: str) -> dict:
        return collection.find_one({"_id": ObjectId(user_id)})

    def get_all_users(self) -> List[User]:
        return list(collection.find())

    def update_username(self, user_id: str, new_info: str) -> dict:
        return collection.update_one({"_id": ObjectId(user_id)}, {"$set": {"username": new_info}})

    def delete_user(self, user_id: str) -> int:
        return collection.delete_one({"_id": ObjectId(user_id)})


# result = list(collection.find())
# print(result[-1]["_id"])
