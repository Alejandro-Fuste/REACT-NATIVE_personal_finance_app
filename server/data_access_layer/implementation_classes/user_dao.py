from typing import List

from server.data_access_layer.abstract_classes.user_dao import UserDAO
from server.entities.user import User


class UserDAOImp(UserDAO):
    def create_new_user(self, user: User) -> User:
        pass

    def get_user(self, user_id: int) -> User:
        pass

    def get_all_users(self) -> List[User]:
        pass

    def update_user(self, user_id: int, user: User) -> User:
        pass

    def delete_user(self, user_id: int) -> int:
        pass
