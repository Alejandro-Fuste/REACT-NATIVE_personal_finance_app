from server.data_access_layer.implementation_classes.options_info_dao import OptionsInfoDAO, OptionsInfoImp

options_dao: OptionsInfoDAO = OptionsInfoImp()


# Read Tests ------------------------------------------
def test_get_live_stock_price(ticker):
    price = options_dao.get_live_stock_price(ticker)
    assert isinstance(price, float)



