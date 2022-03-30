from unittest.mock import MagicMock, patch, Mock

from server.custom_exceptions.user_id_must_be_string import UserIdMustBeString

from server.data_access_layer.abstract_classes.user_dao import UserDAO
from server.data_access_layer.implementation_classes.user_dao import UserDAOImp

from server.service_layer.implementation_classes.user_service import UserService, UserServiceImp

user_dao: UserDAO = UserDAOImp()
user_service: UserService = UserServiceImp(user_dao)

# Creation Tests --------------------------------------

# Read Tests ------------------------------------------
# ID is integer instead of string

def test_get_user_by_id_not_string():
    try:
        pass
    except 


# Update Tests ----------------------------------------

# Delete Tests ----------------------------------------
