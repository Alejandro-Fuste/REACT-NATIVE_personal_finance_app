from unittest.mock import MagicMock, patch, Mock

from server.custom_exceptions.user_not_found import UserNotFound
from server.custom_exceptions.duplicate_user import DuplicateUser

from server.data_access_layer.abstract_classes.user_dao import UserDAO
from server.data_access_layer.implementation_classes.user_dao import UserDAOImp

from server.service_layer.implementation_classes.user_service import UserService, UserServiceImp

user_dao: UserDAO = UserDAOImp()
user_service: UserService = UserServiceImp(user_dao)


# Creation Tests --------------------------------------

# Read Tests ------------------------------------------

# Update Tests ----------------------------------------

# Delete Tests ----------------------------------------






