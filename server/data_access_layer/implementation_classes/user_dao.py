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
        result = collection.find_one({"_id": ObjectId(user_id)})
        return result

    def get_all_users(self) -> List[User]:
        results = collection.find()
        return list(results)

    def update_user(self, user_id: str, user: User) -> User:
        pass

    def delete_user(self, user_id: str) -> int:
        pass

# test_id = "623cdf6f0f58a19156475f78"
# result = collection.find_one({"_id": ObjectId(test_id)})
# print(result)
