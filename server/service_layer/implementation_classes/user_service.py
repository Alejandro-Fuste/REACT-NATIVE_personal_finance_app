from typing import List

from server.custom_exceptions.user_id_must_be_string import UserIdMustBeString
from server.custom_exceptions.user_id_not_provided import MissingUserId

from server.data_access_layer.implementation_classes.user_dao import UserDAOImp
from server.entities.user import User
from server.service_layer.abstract_classes.user_service_abs import UserService

user_id_must_be_string: str = "The user id must be a string."
user_id_not_provided: str = "A user id must be provided."


class UserServiceImp(UserService):
    def __init__(self, user_dao):
        self.user_dao: UserDAOImp = user_dao

    # Creation Methods ----------------------------------------------------------------------------
    def create_new_user(self, user: User) -> dict:
        pass

    # Read Methods --------------------------------------------------------------------------------
    def get_user_by_id(self, user_id: str) -> dict:
        # check user_id is a string
        if isinstance(user_id, str) is False:
            raise UserIdMustBeString(user_id_must_be_string)

        # check user_id not empty
        if len(user_id.strip()) == 0:
            raise MissingUserId(user_id_not_provided)

        return self.user_dao.get_user_by_id(user_id)

    def get_user_by_username(self, username: str) -> dict:
        pass

    def get_all_users(self) -> List[User]:
        return self.user_dao.get_all_users()

    # Update Methods -------------------------------------------------------------------------------
    def update_username(self, user_id: str, new_info: str) -> dict:
        pass

    # Delete Methods -------------------------------------------------------------------------------
    def delete_user(self, user_id: str) -> int:
        pass


