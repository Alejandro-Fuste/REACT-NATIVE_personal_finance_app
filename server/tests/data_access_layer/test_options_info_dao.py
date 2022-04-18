from server.data_access_layer.implementation_classes.options_info_dao import OptionsInfoDAO, OptionsInfoImp

options_dao: OptionsInfoDAO = OptionsInfoImp()


# Read Tests ------------------------------------------
def test_get_live_stock_price(ticker):
    pass


def test_get_options(ticker):
    options = options_dao.get_options(ticker)
    assert len(options) > 1 and isinstance(options, dict)
