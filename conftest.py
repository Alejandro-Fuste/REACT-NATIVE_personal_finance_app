from pytest import fixture
from faker import Faker
from server.entities.paper_trade import PaperTrade
from server.entities.user import User

fake = Faker()


@fixture
def create_new_user() -> User:
    return User(fake.first_name(), fake.last_name(), fake.ascii_company_email(), fake.domain_word(),
                fake.sha256(raw_output=False))


@fixture
def create_new_paper_trade() -> PaperTrade:
    return PaperTrade(fake.pyint(max_value=10000), "T", fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                      "Call", "3/25", "Straddle",
                      fake.pyfloat(left_digits=0, right_digits=2, positive=True),
                      fake.pyfloat(left_digits=0, right_digits=2, positive=True),
                      fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                      fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                      fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                      fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                      fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                      fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                      fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                      fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                      fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                      fake.pyint(max_value=100)
                      )
