from pytest import fixture

from server.entities.user import User


@fixture
def create_new_user() -> User:
    return User(0, "Luke", "Skywalker", "luke.skywalker@test.com", "Master Luke", "Masterluke1234")