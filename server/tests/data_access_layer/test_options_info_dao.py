from server.data_access_layer.implementation_classes.options_info_dao import OptionsInfoDAO, OptionsInfoImp
from server.custom_exceptions.option_not_found import OptionNotFound

options_dao: OptionsInfoDAO = OptionsInfoImp()

stock_not_found = "Your stock was not able to be located."


# Read Tests ------------------------------------------
def test_stock_price_success(ticker):
    price = options_dao.get_stock_price(ticker)
    assert isinstance(price, float)


def test_stock_price_failure(bad_ticker):
    price = options_dao.get_stock_price(bad_ticker)
    assert price == "No data found, symbol may be delisted"


def test_get_calls_success(ticker):
    options = options_dao.get_calls(ticker)
    assert len(options) == 27


def test_get_calls_failure(bad_ticker):
    try:
        options_dao.get_calls(bad_ticker)
        assert False
    except OptionNotFound as e:
        assert str(e) == stock_not_found


def test_get_puts_success(ticker):
    options = options_dao.get_puts(ticker)
    assert len(options) == 27


def test_get_puts_failure(bad_ticker):
    try:
        options_dao.get_puts(bad_ticker)
        assert False
    except OptionNotFound as e:
        assert str(e) == stock_not_found


def test_get_targeted_options_success(ticker):
    options = options_dao.get_targeted_options(ticker, "5/6")
    assert len(options) == 4


def test_get_targeted_options_failure(bad_ticker):
    try:
        options = options_dao.get_targeted_options(bad_ticker, "5/6")
        assert False
    except OptionNotFound as e:
        assert str(e) == stock_not_found
