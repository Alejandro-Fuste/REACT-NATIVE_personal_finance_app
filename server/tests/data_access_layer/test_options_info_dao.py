from server.data_access_layer.implementation_classes.options_info_dao import OptionsInfoDAO, OptionsInfoImp

options_dao: OptionsInfoDAO = OptionsInfoImp()


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
    price = options_dao.get_calls(bad_ticker)
    assert price == "No data found, symbol may be delisted"


def test_get_puts_success(ticker):
    options = options_dao.get_puts(ticker)
    assert len(options) == 27


def test_get_puts_failure(bad_ticker):
    price = options_dao.get_puts(bad_ticker)
    assert price == "No data found, symbol may be delisted"
