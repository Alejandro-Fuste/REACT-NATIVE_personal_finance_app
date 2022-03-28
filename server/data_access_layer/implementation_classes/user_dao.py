from pymongo import MongoClient
from bson.objectid import ObjectId
from environment_variables import mongo_url
from server.data_access_layer.abstract_classes.user_dao import UserDAO
from server.entities.user import User
from server.custom_exceptions.user_not_found import UserNotFound
from server.custom_exceptions.duplicate_user import DuplicateUser
from typing import List

# database connection -------------
connection_string = mongo_url
client = MongoClient(connection_string)
database = client.finance_app
collection = database.users

user_not_found: str = "The user could not be found."
duplicate_user: str = "This user already exists."


class UserDAOImp(UserDAO):
    # Create method -------
    def create_new_user(self, user: User) -> dict:
        result = collection.find_one({"username": user["username"]})

        if result is None:
            return collection.insert_one(user)
        else:
            raise DuplicateUser(duplicate_user)

    # Read methods --------
    def get_user_by_id(self, user_id: str) -> dict:
        result = collection.find_one({"_id": ObjectId(user_id)})

        if result is None:
            raise UserNotFound(user_not_found)
        else:
            return result

    def get_user_by_username(self, username: str) -> dict:
        result = collection.find_one({"username": username})

        if result is None:
            raise UserNotFound(user_not_found)
        else:
            return result

    def get_all_users(self) -> List[User]:
        return list(collection.find())

    # Update methods --------
    def update_username(self, user_id: str, new_info: str) -> dict:
        return collection.update_one({"_id": ObjectId(user_id)}, {"$set": {"username": new_info}})

    # Delete methods --------
    def delete_user(self, user_id: str) -> int:
        return collection.delete_one({"_id": ObjectId(user_id)})

# result = collection.find_one({"_id": ObjectId("623ddc582a8e2cee29b0b62a")})
# print(result)
