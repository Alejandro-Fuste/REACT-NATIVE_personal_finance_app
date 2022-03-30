from unittest.mock import MagicMock, patch, Mock

from server.custom_exceptions.user_id_must_be_string import UserIdMustBeString
from server.custom_exceptions.user_id_not_provided import MissingUserId

from server.data_access_layer.abstract_classes.user_dao import UserDAO
from server.data_access_layer.implementation_classes.user_dao import UserDAOImp

from server.service_layer.implementation_classes.user_service import UserService, UserServiceImp

user_dao: UserDAO = UserDAOImp()
user_service: UserService = UserServiceImp(user_dao)

user_id_must_be_string: str = "The user id must be a string."
user_id_not_provided: str = "A user id must be provided."


# Creation Tests --------------------------------------

# Read Tests ------------------------------------------

# ID is integer instead of string
def test_get_user_by_id_not_string(invalid_id):
    try:
        user_service.get_user_by_id = Mock(side_effect=Exception(user_id_must_be_string))
        assert False
    except UserIdMustBeString as e:
        assert str(e) == user_id_must_be_string


# def test_get_user_by_id_not_string(invalid_id):
#     try:
#         user_service.get_user_by_id(invalid_id)
#         assert False
#     except UserIdMustBeString as e:
#         assert str(e) == user_id_must_be_string


# ID was not provided
def test_get_user_by_id_no_id(missing_id):
    try:
        user_service.get_user_by_id(missing_id)
        assert False
    except MissingUserId as e:
        assert str(e) == user_id_not_provided

# Update Tests ----------------------------------------

# Delete Tests ----------------------------------------
