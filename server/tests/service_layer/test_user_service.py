from unittest.mock import MagicMock, patch, Mock

from server.custom_exceptions.user_id_must_be_string import UserIdMustBeString
from server.custom_exceptions.user_id_not_provided import MissingUserId
from server.custom_exceptions.username_not_string import UserNameNotString

from server.data_access_layer.abstract_classes.user_dao import UserDAO
from server.data_access_layer.implementation_classes.user_dao import UserDAOImp

from server.service_layer.implementation_classes.user_service import UserService, UserServiceImp

user_dao: UserDAO = UserDAOImp()
user_service: UserService = UserServiceImp(user_dao)

user_id_must_be_string: str = "The user id must be a string."
user_id_not_provided: str = "A user id must be provided."
username_must_be_string: str = "The username must be a string."


# Creation Tests --------------------------------------

# Read Tests ------------------------------------------

def test_get_user_by_id_not_string(invalid_id):
    try:
        user_service.get_user_by_id(invalid_id)
        assert False
    except UserIdMustBeString as e:
        assert str(e) == user_id_must_be_string


def test_get_user_by_id_no_id(missing_id):
    try:
        user_service.get_user_by_id(missing_id)
        assert False
    except MissingUserId as e:
        assert str(e) == user_id_not_provided


# Update Tests ----------------------------------------

def test_update_username_id_not_string(invalid_id, update_username):
    try:
        user_service.update_username(invalid_id, update_username)
        assert False
    except UserIdMustBeString as e:
        assert str(e) == user_id_must_be_string


def test_update_username_by_id_no_id(missing_id, update_username):
    try:
        user_service.update_username(missing_id, update_username)
        assert False
    except MissingUserId as e:
        assert str(e) == user_id_not_provided


# Username not string
def test_update_username_not_string(bad_id, bad_username_number):
    try:
        user_service.update_username(bad_id, bad_username_number)
        assert False
    except UserNameNotString as e:
        assert str(e) == username_must_be_string


# Username missing
def test_update_username_missing(bad_id, bad_username_number):
    try:
        user_service.update_username(bad_id, bad_username_number)
        assert False
    except UserNameNotString as e:
        assert str(e) == username_must_be_string


# Username too short
# Username too long


# Delete Tests ----------------------------------------

def test_delete_user_by_id_not_string(invalid_id):
    try:
        user_service.delete_user(invalid_id)
        assert False
    except UserIdMustBeString as e:
        assert str(e) == user_id_must_be_string


def test_delete_user_by_id_no_id(missing_id):
    try:
        user_service.delete_user(missing_id)
        assert False
    except MissingUserId as e:
        assert str(e) == user_id_not_provided
