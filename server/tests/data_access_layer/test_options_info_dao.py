from server.data_access_layer.implementation_classes.options_info_dao import OptionsInfoDAO, OptionsInfoImp

options_dao: OptionsInfoDAO = OptionsInfoImp()


# Read Tests ------------------------------------------
def test_stock_price_success(ticker):
    price = options_dao.get_stock_price(ticker)
    assert isinstance(price, float)


def test_stock_price_failure(bad_ticker):
    price = options_dao.get_stock_price(bad_ticker)
    assert price == "No data found, symbol may be delisted"


def test_get_calls(ticker):
    options = options_dao.get_calls(ticker)
    assert len(options) == 27


def test_get_puts(ticker):
    options = options_dao.get_puts(ticker)
    assert len(options) == 27
