from typing import List

from server.data_access_layer.abstract_classes.user_dao import UserDAO
from server.entities.user import User


class UserDAOImp(UserDAO):
    def create_new_user(self, user: User) -> User:
        pass

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
