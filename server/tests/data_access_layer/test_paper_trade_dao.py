from server.data_access_layer.implementation_classes.user_dao import UserDAOImp, UserDAO
from server.data_access_layer.implementation_classes.paper_trade_dao import PaperTradeDAOImp, PaperTradeDAO
from server.custom_exceptions.duplicate_trade import DuplicateTrade

user_dao: UserDAO = UserDAOImp()
paper_trade_dao: PaperTradeDAO = PaperTradeDAOImp()

duplicate_trade_message: str = "This trade already exists."


# Creation Tests -----------------

def test_add_paper_trade_success(create_new_paper_trade):
    users = user_dao.get_all_users()
    first_user_id = users[0]["_id"]
    new_trade: dict = paper_trade_dao.add_paper_trade(first_user_id, create_new_paper_trade)
    assert new_trade.acknowledged


def test_add_paper_trade_failure_duplicate():
    users = user_dao.get_all_users()
    first_user_id = users[0]["_id"]
    duplicate_trade = users[0]["paperTrades"][0]

    try:
        paper_trade_dao.add_paper_trade(first_user_id, duplicate_trade)
        assert False
    except DuplicateTrade as e:
        assert str(e) == duplicate_trade_message


# Read Tests --------------------

def test_get_paper_trades_success():
    users = user_dao.get_all_users()
    first_user_id = users[0]["_id"]
    user_trade = paper_trade_dao.get_paper_trades(first_user_id)
    assert isinstance(user_trade, list)


def test_get_paper_trades_failure():
    pass


# Update Tests ------------------

def test_update_paper_trade_success():
    users = user_dao.get_all_users()
    first_user_id = users[0]["_id"]
    updated_trade: bool = paper_trade_dao.update_paper_trade_sell_price(first_user_id, 0, 111.11)
    assert updated_trade


def test_update_paper_trade_failure():
    pass


# Delete Tests -------------------

def test_delete_paper_trade_success():
    users = user_dao.get_all_users()
    first_user_id = users[0]["_id"]
    paper_trade_id = users[0]["paperTrades"][-1]["tradeId"]
    deleted_account = paper_trade_dao.delete_paper_trade(first_user_id, paper_trade_id)
    assert deleted_account


def test_delete_paper_trade_failure():
    pass
