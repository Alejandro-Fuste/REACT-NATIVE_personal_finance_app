from server.data_access_layer.implementation_classes.user_dao import UserDAOImp, UserDAO
from server.entities.user import User

user_dao: UserDAO = UserDAOImp()


# Creation Tests -----------------

def test_create_user_success(create_new_user):
    new_user: User = user_dao.create_new_user(create_new_user)
    assert new_user.first_name == create_new_user.first_name


# Read Tests ---------------------

def test_get_user_by_id_success():
    result: User = user_dao.get_user_by_id("623cc3f5eb1b73644940438a")
    assert result.first_name == "Luke"


def test_get_user_by_username_success(create_new_user):
    result: User = user_dao.get_user_by_username(create_new_user.username)
    assert result.username == create_new_user.username


def test_get_all_users_success():
    users = user_dao.get_all_users()
    assert len(users) >= 1


# Update Tests -------------------

def test_update_user_success(updated_user):
    updated_user: User = user_dao.update_user("623cc3f5eb1b73644940438a", updated_user)
    assert updated_user.username == "Master Jedi"


# Delete Tests -------------------

def test_delete_user_success(create_new_user):
    get_result: User = user_dao.get_user_by_username(create_new_user.username)
    user_id: str = get_result._id
    deleted_user = user_dao.delete_user(user_id)
    assert deleted_user.deleted_count == 1
