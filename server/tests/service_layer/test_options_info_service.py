from server.custom_exceptions.input_not_string import InputNotString

from server.data_access_layer.implementation_classes.options_info_dao import OptionsInfoDAO, OptionsInfoImp
from server.service_layer.implementation_classes.options_info_service import OptionsInfoService, OptionsInfoServiceImp

options_info_dao: OptionsInfoDAO = OptionsInfoImp()
options_info_service: OptionsInfoService = OptionsInfoServiceImp(options_info_dao)

input_must_be_string: str = "The input must be a string."


# Read Tests --------------------------------------------------------------------------------
# Get Stock Price Tests ---------------------------------------------------------------------
def test_get_stock_price_ticker_not_string(int_ticker):
    try:
        options_info_service.get_stock_price(int_ticker)
        assert False
    except InputNotString as e:
        assert str(e) == input_must_be_string


def test_get_stock_price_ticker_empty_string():
    pass


def test_get_stock_price_ticker_blank():
    pass


# Get Calls Tests ---------------------------------------------------------------------
def test_get_calls_ticker_not_string():
    pass


def test_get_calls_ticker_empty_string():
    pass


def test_get_calls_ticker_blank():
    pass


# Get Puts Tests ---------------------------------------------------------------------
def test_get_puts_ticker_not_string():
    pass


def test_get_puts_ticker_empty_string():
    pass


def test_get_puts_ticker_blank():
    pass
