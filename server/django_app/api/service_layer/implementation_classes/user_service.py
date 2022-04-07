from typing import List

from server.django_app.api.custom_exceptions.input_too_long import InputTooLong
from server.django_app.api.custom_exceptions.input_too_short import InputTooShort
from server.django_app.api.custom_exceptions.input_missing import InputMissing
from server.django_app.api.custom_exceptions.input_not_string import InputNotString
from server.django_app.api.custom_exceptions.user_id_must_be_string import UserIdMustBeString
from server.django_app.api.custom_exceptions.user_id_not_provided import MissingUserId
from server.django_app.api.custom_exceptions.email_wrong_format import EmailWrongFormat

from server.django_app.api.data_access_layer.implementation_classes.user_dao import UserDAOImp
from server.django_app.api.entities.user import User
from server.django_app.api.service_layer.abstract_classes.user_service_abs import UserService

user_id_must_be_string: str = "The user id must be a string."
user_id_not_provided: str = "A user id must be provided."
username_must_be_string: str = "The username must be a string."
username_not_provided: str = "A username must be provided."
input_must_be_string: str = "The input must be a string."
input_not_provided: str = "An input must be provided."
input_too_short: str = "The input is too short."
input_too_long: str = "The input is too long."
email_wrong_format: str = "The email is not in the correct format."


class UserServiceImp(UserService):
    def __init__(self, user_dao):
        self.user_dao: UserDAOImp = user_dao

    # Creation Methods ----------------------------------------------------------------------------
    def create_new_user(self, user: User) -> dict:
        # check if user properties are strings
        if isinstance(user['firstName'], str) is False or isinstance(user["lastName"], str) is False \
                or isinstance(user["email"], str) is False or isinstance(user["username"], str) is False \
                or isinstance(user["password"], str) is False:
            raise InputNotString(input_must_be_string)

        # check if any user properties are empty
        if len(user["firstName"].strip()) == 0 or len(user["lastName"].strip()) == 0 or len(user["email"].strip()) == 0 \
                or len(user["username"].strip()) == 0 or len(user["password"].strip()) == 0:
            raise InputMissing(input_not_provided)

        # check if any user properties are too short
        if len(user["firstName"].strip()) < 2 or len(user["lastName"].strip()) < 2 or len(user["username"].strip()) < 2\
                or len(user["password"].strip()) < 8:
            raise InputTooShort(input_too_short)

        # check if email is too short
        if len(user["email"].strip()) < 5:
            raise EmailWrongFormat(email_wrong_format)

        # check if any user properties are too long
        if len(user["firstName"].strip()) > 100 or len(user["lastName"].strip()) > 100 or len(user["email"].strip()) > 100 \
                or len(user["username"].strip()) > 100 or len(user["password"].strip()) > 100:
            raise InputTooLong(input_too_long)

        return self.user_dao.create_new_user(user)

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
        # check username is a string
        if isinstance(username, str) is False:
            raise InputNotString(username_must_be_string)

        # check user_id not empty
        if len(username.strip()) == 0:
            raise InputMissing(username_not_provided)

        return self.user_dao.get_user_by_username(username)

    def get_all_users(self) -> List[User]:
        return self.user_dao.get_all_users()

    # Update Methods -------------------------------------------------------------------------------
    def update_username(self, user_id: str, new_info: str) -> dict:
        # check user_id is a string
        if isinstance(user_id, str) is False:
            raise UserIdMustBeString(user_id_must_be_string)

        # checks new_info is a string
        if isinstance(new_info, str) is False:
            raise InputNotString(input_must_be_string)

        # check user_id not empty
        if len(user_id.strip()) == 0:
            raise MissingUserId(user_id_not_provided)

        # check new_info not empty
        if len(new_info.strip()) == 0:
            raise InputMissing(input_not_provided)

        # check new_info is too short
        if len(new_info.strip()) < 2:
            raise InputTooShort(input_too_short)

        # check new_info is too long
        if len(new_info.strip()) > 100:
            raise InputTooLong(input_too_long)

        return self.user_dao.update_username(user_id, new_info)

    # Delete Methods -------------------------------------------------------------------------------
    def delete_user(self, user_id: str) -> int:
        # check user_id is a string
        if isinstance(user_id, str) is False:
            raise UserIdMustBeString(user_id_must_be_string)

        # check user_id not empty
        if len(user_id.strip()) == 0:
            raise MissingUserId(user_id_not_provided)

        return self.user_dao.delete_user(user_id)

