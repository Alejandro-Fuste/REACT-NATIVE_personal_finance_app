from typing import List

from server.custom_exceptions.user_id_must_be_string import UserIdMustBeString

from server.data_access_layer.implementation_classes.user_dao import UserDAOImp
from server.entities.user import User
from server.service_layer.abstract_classes.user_service_abs import UserService

user_id_must_be_string: str = "The user id must be a string."


class UserServiceImp(UserService):
    def __init__(self, user_dao):
        self.user_dao: UserDAOImp = user_dao

    def create_new_user(self, user: User) -> dict:
        pass

    def get_user_by_id(self, user_id: str) -> dict:
        if isinstance(user_id, str) is True:
            return self.user_dao.get_user_by_id(user_id)
        else:
            raise UserIdMustBeString(user_id_must_be_string)

    def get_user_by_username(self, username: str) -> dict:
        pass

    def get_all_users(self) -> List[User]:
        pass

    def update_username(self, user_id: str, new_info: str) -> dict:
        pass

    def delete_user(self, user_id: str) -> int:
        pass


test_input = 1
print(isinstance(test_input, str))
