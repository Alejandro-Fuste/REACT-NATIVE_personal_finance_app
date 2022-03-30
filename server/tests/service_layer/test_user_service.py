from unittest.mock import MagicMock, patch, Mock

from server.data_access_layer.abstract_classes.user_dao import UserDAO
from server.data_access_layer.implementation_classes.user_dao import UserDAOImp

from server.custom_exceptions.user_not_found import UserNotFound
from server.custom_exceptions.duplicate_user import DuplicateUser
