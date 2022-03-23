from pytest import fixture
from faker import Faker

from server.entities.paper_trade import PaperTrade
from server.entities.user import User

fake = Faker()


# @fixture
def create_new_user() -> User:
    return User(fake.uuid4(), fake.first_name(), fake.last_name(), fake.ascii_company_email(), fake.domain_word(),
                fake.sha256(raw_output=False))


@fixture
def create_new_paper_trade() -> PaperTrade:
    return PaperTrade("T", 23.00, "Call", "3/25", "Straddle", .30, .11, 23.30, 22.89, 0, )


print(create_new_user())
print(create_new_user())
