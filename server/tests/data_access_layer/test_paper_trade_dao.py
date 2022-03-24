from server.data_access_layer.implementation_classes.paper_trade_dao import PaperTradeDAOImp, PaperTradeDAO
from server.entities.paper_trade import PaperTrade
from pytest import fixture

paper_trade_dao: PaperTradeDAO = PaperTradeDAOImp()


# Creation Tests -----------------

def test_add_paper_trade_success(create_new_paper_trade):
    new_trade: PaperTrade = paper_trade_dao.add_paper_trade(create_new_paper_trade)
    assert new_trade.ticker == create_new_paper_trade.ticker


# Update Tests -----------------

def test_update_paper_trade_success(updated_trade):
    updated_trade: PaperTrade = paper_trade_dao.update_paper_trade(1, updated_trade)
    assert updated_trade.sell_price == 2.00


# Delete Tests -------------------

def test_delete_paper_trade_success():
    deleted_account = paper_trade_dao.delete_paper_trade(2)
    assert deleted_account.deleted_count == 1
