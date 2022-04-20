from server.data_access_layer.implementation_classes.options_info_dao import OptionsInfoDAO, OptionsInfoImp
from server.service_layer.implementation_classes.options_info_service import OptionsInfoService, OptionsInfoServiceImp

options_info_dao: OptionsInfoDAO = OptionsInfoImp()
options_info_service: OptionsInfoService = OptionsInfoServiceImp(options_info_dao)


# Read Tests --------------------------------------------------------------------------------

def test_get_stock_price_ticker_not_string():
    pass


def test_get_stock_price_ticker_missing():
    pass


def test_get_calls_ticker_not_string():
    pass


def test_get_calls_ticker_missing():
    pass


def test_get_puts_ticker_not_string():
    pass


def test_get_puts_ticker_missing():
    pass
