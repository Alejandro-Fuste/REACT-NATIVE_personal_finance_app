from server.data_access_layer.implementation_classes.user_dao import UserDAOImp, UserDAO
from server.entities.user import User

user_dao: UserDAO = UserDAOImp()


# Creation Tests -----------------

def test_create_user_success(create_new_user):
    new_user: dict = user_dao.create_new_user(create_new_user)
    assert new_user.acknowledged


# Read Tests ---------------------

def test_get_user_by_id_success():
    users = user_dao.get_all_users()
    first_user = users[0]["_id"]
    result = user_dao.get_user_by_id(first_user)
    assert result["firstName"] == "Luke"


def test_get_all_users_success():
    users = user_dao.get_all_users()
    assert len(users) >= 1


# Update Tests -------------------

def test_update_username_success():
    users = user_dao.get_all_users()
    first_user_id = users[0]["_id"]
    updated_user: dict = user_dao.update_username(first_user_id, "Master Jedi")
    assert updated_user.acknowledged


# Delete Tests -------------------

def test_delete_user_success():
    users = user_dao.get_all_users()
    last_user = users[-1]["_id"]
    deleted_user = user_dao.delete_user(last_user)
    assert deleted_user.deleted_count == 1
