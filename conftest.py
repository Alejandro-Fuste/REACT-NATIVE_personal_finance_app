from pytest import fixture
from faker import Faker
from server.entities.paper_trade import PaperTrade
from server.entities.user import User

fake = Faker()


@fixture
def create_new_user() -> User:
    new_user = User(fake.first_name(), fake.last_name(), fake.ascii_company_email(), fake.domain_word(),
                    fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_user_first_name_number() -> User:
    new_user = User(fake.pyint(max_value=10000), fake.last_name(), fake.ascii_company_email(), fake.domain_word(),
                    fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_user_first_name_blank() -> User:
    new_user = User("", fake.last_name(), fake.ascii_company_email(), fake.domain_word(),
                    fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_paper_trade() -> PaperTrade:
    new_trade = PaperTrade(fake.pyint(max_value=10000), "T", fake.pyfloat(left_digits=2, right_digits=2, positive=True),
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
    return new_trade.make_dictionary()


@fixture
def bad_id() -> str:
    return "623ddc582a8e2cee29b0b62a"


@fixture
def invalid_id() -> int:
    return fake.pyint(max_value=10000)


@fixture
def missing_id() -> str:
    return " "


@fixture
def update_username() -> str:
    return fake.domain_word()


@fixture
def bad_username() -> str:
    return "ekul"


@fixture
def bad_username_number() -> int:
    return fake.pyint(max_value=10000)


@fixture
def username_missing() -> str:
    return ""


@fixture
def username_too_short() -> str:
    return "ab"


@fixture
def username_too_long() -> str:
    return "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567" \
           "89012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234" \
           "56789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901" \
           "2345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567" \
           "89012345678901234567890123456789012345678901234567890123456789012345678901"
