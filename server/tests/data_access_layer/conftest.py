from pytest import fixture

from server.entities.paper_trade import PaperTrade
from server.entities.user import User


@fixture
def create_new_user() -> User:
    return User(0, "Luke", "Skywalker", "luke.skywalker@test.com", "Master Luke", "Masterluke1234")

@fixture
def create_new_paper_trade() -> PaperTrade:
    return PaperTrade("T", 23.00, "Call", "3/25", "Straddle", .30, .11, 23.30, 22.89, 0, )