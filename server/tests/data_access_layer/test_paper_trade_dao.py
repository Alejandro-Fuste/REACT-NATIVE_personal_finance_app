from server.data_access_layer.implementation_classes.user_dao import UserDAOImp, UserDAO
from server.data_access_layer.implementation_classes.paper_trade_dao import PaperTradeDAOImp, PaperTradeDAO
from server.entities.paper_trade import PaperTrade

user_dao: UserDAO = UserDAOImp()
paper_trade_dao: PaperTradeDAO = PaperTradeDAOImp()


# Creation Tests -----------------

def test_add_paper_trade_success(create_new_paper_trade):
    users = user_dao.get_all_users()
    first_user_id = users[0]["_id"]
    new_trade: dict = paper_trade_dao.add_paper_trade(first_user_id, create_new_paper_trade)
    assert new_trade.acknowledged


# Read Tests --------------------

def test_get_paper_trades_success():
    users = user_dao.get_all_users()
    first_user_id = users[0]["_id"]
    user_trade = paper_trade_dao.get_paper_trades(first_user_id)
    assert isinstance(user_trade, list)


# Update Tests ------------------

def test_update_paper_trade_success(updated_trade):
    updated_trade: PaperTrade = paper_trade_dao.update_paper_trade(1, updated_trade)
    assert updated_trade.sell_price == 2.00


# Delete Tests -------------------

def test_delete_paper_trade_success():
    deleted_account = paper_trade_dao.delete_paper_trade(2)
    assert deleted_account.deleted_count == 1
