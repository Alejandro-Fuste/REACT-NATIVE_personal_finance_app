from pymongo import MongoClient
from environment_variables import mongo_url
from server.data_access_layer.abstract_classes.user_dao import UserDAO
from server.entities.user import User
from typing import List

# database connection -------------
connection_string = mongo_url
client = MongoClient(connection_string)
database = client.finance_app
collection = database.users


class UserDAOImp(UserDAO):
    def create_new_user(self, user: User) -> dict:
        return collection.insert_one(user)

    def get_user_by_id(self, user_id: str) -> User:
        pass

    def get_user_by_username(self, username: str) -> User:
        pass

    def get_all_users(self) -> List[User]:
        pass

    def update_user(self, user_id: str, user: User) -> User:
        pass

    def delete_user(self, user_id: str) -> int:
        pass
