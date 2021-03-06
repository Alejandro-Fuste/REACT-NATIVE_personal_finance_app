from pytest import fixture
from faker import Faker
from server.entities.option import Option
from server.entities.paper_trade import PaperTrade
from server.entities.db_user import DatabaseUser

fake = Faker()


@fixture
def create_new_user() -> DatabaseUser:
    new_user = DatabaseUser(fake.first_name(), fake.last_name(), fake.ascii_company_email(), fake.domain_word(),
                            fake.sha256(raw_output=False))
    return new_user.make_dictionary()


# new paper trade -----------------------------------------------------------------
@fixture
def create_new_paper_trade() -> Option:
    new_paper_trade = Option("T",
                             20.0,
                             fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                             "3/25",
                             1,
                             "Straddle",
                             fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                             fake.pyfloat(left_digits=2, right_digits=2, positive=True)
                             )

    return new_paper_trade.make_dictionary()


@fixture
def option_update() -> PaperTrade:
    opt_dict = PaperTrade(498040, 1, 0.13, 0.41, 1.01, .01)

    return opt_dict.make_dictionary()


@fixture
def option_update2() -> dict:
    opt_dict = {
        "tradeId": 498040,
        "contracts": 1,
        "callPrice": .13,
        "putPrice": .41,
        "callSellPrice": 1.01,
        "putSellPrice": .01
    }

    return opt_dict


# number errors -----------------------------------------------------------------
@fixture
def create_new_user_first_name_number() -> DatabaseUser:
    new_user = DatabaseUser(fake.pyint(max_value=10000), fake.last_name(), fake.ascii_company_email(),
                            fake.domain_word(),
                            fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_user_last_name_number() -> DatabaseUser:
    new_user = DatabaseUser(fake.first_name(), fake.pyint(max_value=10000), fake.ascii_company_email(),
                            fake.domain_word(),
                            fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_user_username_number() -> DatabaseUser:
    new_user = DatabaseUser(fake.first_name(), fake.last_name(), fake.ascii_company_email(),
                            fake.pyint(max_value=10000),
                            fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_user_password_number() -> DatabaseUser:
    new_user = DatabaseUser(fake.first_name(), fake.last_name(), fake.ascii_company_email(), fake.domain_word(),
                            fake.pyint(max_value=10000))
    return new_user.make_dictionary()


# blank errors -----------------------------------------------------------------
@fixture
def create_new_user_first_name_blank() -> DatabaseUser:
    new_user = DatabaseUser("", fake.last_name(), fake.ascii_company_email(), fake.domain_word(),
                            fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_user_last_name_blank() -> DatabaseUser:
    new_user = DatabaseUser(fake.first_name(), "", fake.ascii_company_email(), fake.domain_word(),
                            fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_user_email_name_blank() -> DatabaseUser:
    new_user = DatabaseUser(fake.first_name(), fake.last_name(), "", fake.domain_word(),
                            fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_user_username_name_blank() -> DatabaseUser:
    new_user = DatabaseUser(fake.first_name(), fake.last_name(), fake.ascii_company_email(), "",
                            fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_user_password_name_blank() -> DatabaseUser:
    new_user = DatabaseUser(fake.first_name(), fake.last_name(), fake.ascii_company_email(), fake.domain_word(),
                            "")
    return new_user.make_dictionary()


# too short errors -----------------------------------------------------------------
@fixture
def create_new_user_first_name_too_short() -> DatabaseUser:
    new_user = DatabaseUser("a", fake.last_name(), fake.ascii_company_email(), fake.domain_word(),
                            fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_user_last_name_too_short() -> DatabaseUser:
    new_user = DatabaseUser(fake.first_name(), "a", fake.ascii_company_email(), fake.domain_word(),
                            fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_user_username_too_short() -> DatabaseUser:
    new_user = DatabaseUser("a", fake.last_name(), fake.ascii_company_email(), "a",
                            fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_user_password_too_short() -> DatabaseUser:
    new_user = DatabaseUser("a", fake.last_name(), fake.ascii_company_email(), fake.domain_word(),
                            "a")
    return new_user.make_dictionary()


# email errors -----------------------------------------------------------------
@fixture
def create_new_user_email_wrong_format() -> DatabaseUser:
    new_user = DatabaseUser(fake.first_name(), fake.last_name(), "a", fake.domain_word(),
                            fake.sha256(raw_output=False))
    return new_user.make_dictionary()


# too long errors -----------------------------------------------------------------
@fixture
def create_new_user_first_name_too_long() -> DatabaseUser:
    new_user = DatabaseUser(
        "1234567890123456789012345678901234557868290345869023486903248068239046089324068923094860982092340"
        "68809", fake.last_name(), fake.ascii_company_email(), fake.domain_word(),
        fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_user_last_name_too_long() -> DatabaseUser:
    new_user = DatabaseUser(fake.first_name(),
                            "123456789012345678901234567890123455786829034586902348690324806823904608932406"
                            "8923094860982092340"
                            "68809", fake.ascii_company_email(), fake.domain_word(),
                            fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_user_username_too_long() -> DatabaseUser:
    new_user = DatabaseUser(fake.first_name(), fake.last_name(), fake.ascii_company_email(),
                            "12345678901234567890123456789012"
                            "345578682903458690234869032480682"
                            "390460893240689230948609820923406"
                            "8809",
                            fake.sha256(raw_output=False))
    return new_user.make_dictionary()


@fixture
def create_new_user_password_too_long() -> DatabaseUser:
    new_user = DatabaseUser(fake.first_name(), fake.last_name(), fake.ascii_company_email(), fake.domain_word(),
                            "12345678901234567890123456789012"
                            "345578682903458690234869032480682"
                            "390460893240689230948609820923406"
                            "8809")
    return new_user.make_dictionary()


@fixture
def trade_value_not_number() -> dict:
    return {
        "ticker": "T",
        "strikePrice": "fake.pyfloat(left_digits=2, right_digits=2, positive=True)",
        "stockPrice": fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        "expirationDate": "3/25",
        "contracts": 1,
        "strategyType": "Straddle",
        "callPrice": fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        "putPrice": fake.pyfloat(left_digits=2, right_digits=2, positive=True)
    }


@fixture
def trade_value_not_int() -> dict:
    return {
        "ticker": "T",
        "strikePrice": fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        "stockPrice": fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        "expirationDate": "3/25",
        "contracts": "1",
        "strategyType": "Straddle",
        "callPrice": fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        "putPrice": fake.pyfloat(left_digits=2, right_digits=2, positive=True)
    }


@fixture
def trade_value_missing() -> dict:
    return {
        "ticker": "T",
        "strikePrice": "fake.pyfloat(left_digits=2, right_digits=2, positive=True)",
        "stockPrice": fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        "expirationDate": "3/25",
        "contracts": None,
        "strategyType": "Straddle",
        "callPrice": fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        "putPrice": fake.pyfloat(left_digits=2, right_digits=2, positive=True)
    }


@fixture
def bad_id() -> str:
    return "623ddc582a8e2cee29b0b62a"


@fixture
def invalid_id() -> int:
    return fake.pyint(max_value=10000)


@fixture
def missing_id() -> str:
    return ""


@fixture
def missing_paper_trade_id() -> None:
    return None


@fixture
def valid_paper_trade_id() -> int:
    return 123456


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
    return "a"


@fixture
def username_too_long() -> str:
    return "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890" \
           "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890" \
           "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890" \
           "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890" \
           "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901"


@fixture
def ticker() -> str:
    return "t"


@fixture
def bad_ticker() -> str:
    return "2t"


@fixture
def int_ticker() -> int:
    return fake.pyint(max_value=10000)


@fixture
def empty_string() -> str:
    return ""


@fixture
def none_ticker() -> None:
    return None


@fixture
def option_dict_ticker_not_string() -> dict:
    opt_dict = {
        "ticker": 1,
        "strikePrice": 19,
        "stockPrice": 19.35,
        "expirationDate": "5/13",
        "contracts": 1,
        "strategyType": "Straddle",
        "callPrice": 0.49,
        "putPrice": 0.13
    }

    return opt_dict


@fixture
def option_dict_missing_exp_date() -> dict:
    opt_dict = {
        "ticker": "T",
        "strikePrice": 19.00,
        "stockPrice": 19.35,
        "expirationDate": "",
        "contracts": 1,
        "strategyType": "Straddle",
        "callPrice": 0.49,
        "putPrice": 0.13
    }

    return opt_dict


@fixture
def option_dict_stock_price_not_float() -> dict:
    opt_dict = {
        "ticker": "T",
        "strikePrice": 19,
        "stockPrice": "19.35",
        "expirationDate": "5/13",
        "contracts": 1,
        "strategyType": "Straddle",
        "callPrice": 0.49,
        "putPrice": 0.13
    }

    return opt_dict


@fixture
def option_dict_contract_not_int() -> dict:
    opt_dict = {
        "ticker": "T",
        "strikePrice": 19.00,
        "stockPrice": 19.35,
        "expirationDate": "5/13",
        "contracts": "1",
        "strategyType": "Straddle",
        "callPrice": 0.49,
        "putPrice": 0.13
    }

    return opt_dict


@fixture
def option_update_sell_price_value_missing() -> dict:
    opt_dict = {
        "tradeId": 123456,
        "contracts": 1,
        "putPrice": 0.13,
        "callPrice": None,
        "callSellPrice": 1.01,
        "putSellPrice": .01
    }

    return opt_dict


@fixture
def option_update_value_not_float() -> dict:
    opt_dict = {
        "tradeId": 123456,
        "contracts": 1,
        "callPrice": ".54",
        "putPrice": 0.13,
        "callSellPrice": 1.01,
        "putSellPrice": .01
    }

    return opt_dict


@fixture
def option_update_sell_price_not_float() -> dict:
    opt_dict = {
        "tradeId": 123456,
        "contracts": "1",
        "callPrice": 0.49,
        "putPrice": 0.13,
        "callSellPrice": "1.01",
        "putSellPrice": .01
    }

    return opt_dict


@fixture
def option_update_sell_price_missing() -> dict:
    opt_dict = {
        "tradeId": 123456,
        "contracts": "1",
        "callPrice": 0.49,
        "putPrice": 0.13,
        "callSellPrice": None,
        "putSellPrice": .01

    }

    return opt_dict


@fixture
def option_update_sell_price_negative_number() -> dict:
    opt_dict = {
        "tradeId": 123456,
        "contracts": 1,
        "callPrice": 0.49,
        "putPrice": 0.13,
        "callSellPrice": -1.01,
        "putSellPrice": .01
    }

    return opt_dict
