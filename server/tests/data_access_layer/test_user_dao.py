from server.data_access_layer.implementation_classes.user_dao import UserDAOImp, UserDAO
from server.entities.user import User
from pytest import fixture

user_dao: UserDAO = UserDAOImp()


# Creation Tests -----------------

def test_create_user_success():
    pass


# Read Tests ---------------------

def test_get_user_success():
    pass


def test_get_all_users_success():
    pass


# Update Tests -------------------

def test_update_user_success():
    pass


# Delete Tests -------------------

def test_delete_user_success():
    pass
