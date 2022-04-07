from server.django_app.api.data_access_layer.implementation_classes import UserDAOImp, UserDAO
from server.django_app.api.custom_exceptions.user_not_found import UserNotFound
from server.django_app.api.custom_exceptions.duplicate_user import DuplicateUser

user_dao: UserDAO = UserDAOImp()

user_not_found_message: str = "The user could not be found."
duplicate_user_message: str = "This user already exists."


# Creation Tests --------------------------------------

def test_create_user_success(create_new_user):
    new_user: dict = user_dao.create_new_user(create_new_user)
    assert new_user.acknowledged


def test_create_user_failure_duplicate():
    users = user_dao.get_all_users()
    duplicate_user = users[0]

    try:
        user_dao.create_new_user(duplicate_user)
        assert False
    except DuplicateUser as e:
        assert str(e) == duplicate_user_message


# Read Tests ------------------------------------------

def test_get_user_by_id_success():
    users = user_dao.get_all_users()
    first_user = users[0]["_id"]
    result = user_dao.get_user_by_id(first_user)
    assert result["firstName"] == "Luke"


def test_get_user_by_id_failure(bad_id):
    try:
        user_dao.get_user_by_id(bad_id)
        assert False
    except UserNotFound as e:
        assert str(e) == user_not_found_message


def test_get_user_by_username_success():
    users = user_dao.get_all_users()
    user_name = users[0]["username"]
    result = user_dao.get_user_by_username(user_name)
    assert result["username"] == user_name


def test_get_user_by_username_failure(bad_username):
    try:
        user_dao.get_user_by_username(bad_username)
        assert False
    except UserNotFound as e:
        assert str(e) == user_not_found_message


def test_get_all_users_success():
    users = user_dao.get_all_users()
    assert len(users) >= 1


# Update Tests ----------------------------------------

def test_update_username_success(update_username):
    users = user_dao.get_all_users()
    first_user_id = users[0]["_id"]
    updated_user: dict = user_dao.update_username(first_user_id, update_username)
    assert updated_user.acknowledged


def test_update_username_failure(bad_id, update_username):
    try:
        user_dao.update_username(bad_id, update_username)
        assert False
    except UserNotFound as e:
        assert str(e) == user_not_found_message


# Delete Tests ----------------------------------------

def test_delete_user_success():
    users = user_dao.get_all_users()
    last_user = users[-1]["_id"]
    deleted_user = user_dao.delete_user(last_user)
    assert deleted_user.deleted_count == 1


def test_delete_user_failure(bad_id):
    try:
        user_dao.delete_user(bad_id)
        assert False
    except UserNotFound as e:
        assert str(e) == user_not_found_message
