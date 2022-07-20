from server.data_access_layer.implementation_classes.user_dao import UserDAOImp, UserDAO
from server.data_access_layer.implementation_classes.paper_trade_dao import PaperTradeDAOImp, PaperTradeDAO
from server.custom_exceptions.duplicate_trade import DuplicateTrade
from server.custom_exceptions.user_not_found import UserNotFound
from server.custom_exceptions.trade_not_found import TradeNotFound
from server.custom_exceptions.no_trades import NoTrades

user_dao: UserDAO = UserDAOImp()
paper_trade_dao: PaperTradeDAO = PaperTradeDAOImp()

duplicate_trade_message: str = "This trade already exists."
user_not_found_message: str = "The user could not be found."
paper_trade_not_found: str = "This trade could not be found."
user_has_no_trades: str = "Currently, user does not have any trades."


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


def test_get_paper_trades_failure_user_not_found(bad_id):
    try:
        paper_trade_dao.get_paper_trades(bad_id)
        assert False
    except UserNotFound as e:
        assert str(e) == user_not_found_message


def test_get_paper_trades_failure_no_trades_exist():
    users = user_dao.get_all_users()
    user_without_trades = users[2]["_id"]

    try:
        paper_trade_dao.get_paper_trades(user_without_trades)
        assert False
    except NoTrades as e:
        assert str(e) == user_has_no_trades


# Update Tests ------------------

def test_update_paper_trade_success(option_update):
    users = user_dao.get_all_users()
    first_user_id = users[0]["_id"]
    updated_trade: bool = paper_trade_dao.update_paper_trade(first_user_id, 0, option_update)
    assert updated_trade


def test_update_paper_trade_failure_user_not_found(bad_id, option_update):
    try:
        paper_trade_dao.update_paper_trade(bad_id, 0, option_update)
        assert False
    except UserNotFound as e:
        assert str(e) == user_not_found_message


def test_update_paper_trade_failure_paper_trade_not_found():
    users = user_dao.get_all_users()
    first_user_id = users[2]["_id"]
    trades: list = users[2]["paperTrades"]
    bad_trade_index: int = len(trades) + 1

    try:
        paper_trade_dao.update_paper_trade(first_user_id, bad_trade_index, 111.11)
        assert False
    except TradeNotFound as e:
        assert str(e) == paper_trade_not_found


# Delete Tests -------------------

def test_delete_paper_trade_success():
    users = user_dao.get_all_users()
    first_user_id = users[0]["_id"]
    paper_trade_id = users[0]["paperTrades"][-1]["tradeId"]
    deleted_account = paper_trade_dao.delete_paper_trade(first_user_id, paper_trade_id)
    assert deleted_account


def test_delete_paper_trade_failure_user_not_found(bad_id):
    try:
        paper_trade_dao.delete_paper_trade(bad_id, 0)
    except UserNotFound as e:
        assert str(e) == user_not_found_message


def test_delete_paper_trade_failure_paper_trade_not_found():
    users = user_dao.get_all_users()
    first_user_id = users[2]["_id"]
    trades: list = users[2]["paperTrades"]
    bad_trade_index: int = len(trades) + 1

    try:
        paper_trade_dao.delete_paper_trade(first_user_id, bad_trade_index)
        assert False
    except TradeNotFound as e:
        assert str(e) == paper_trade_not_found
