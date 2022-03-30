from typing import List

from ser

from server.data_access_layer.implementation_classes.user_dao import UserDAOImp
from server.entities.user import User
from server.service_layer.abstract_classes.user_service_abs import UserService


class UserServiceImp(UserService):
    def __init__(self, user_dao):
        self.user_dao: UserDAOImp = user_dao

    def create_new_user(self, user: User) -> dict:
        pass

    def get_user_by_id(self, user_id: str) -> dict:
        pass

    def get_user_by_username(self, username: str) -> dict:
        pass

    def get_all_users(self) -> List[User]:
        pass

    def update_username(self, user_id: str, new_info: str) -> dict:
        pass

    def delete_user(self, user_id: str) -> int:
        pass


