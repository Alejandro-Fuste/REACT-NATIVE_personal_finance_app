from server.custom_exceptions.user_id_must_be_string import UserIdMustBeString
from server.custom_exceptions.user_id_not_provided import MissingUserId
from server.custom_exceptions.paper_trade_exception import PaperTradeException

from server.data_access_layer.implementation_classes.user_dao import UserDAO, UserDAOImp
from server.data_access_layer.abstract_classes.paper_trade_dao import PaperTradeDAO
from server.data_access_layer.implementation_classes.paper_trade_dao import PaperTradeDAOImp

from server.service_layer.implementation_classes.paper_trade_service import PaperTradeService, PaperTradeServiceImp

user_dao: UserDAO = UserDAOImp()
paper_trade_dao: PaperTradeDAO = PaperTradeDAOImp()
paper_trade_service: PaperTradeService = PaperTradeServiceImp(paper_trade_dao)

user_id_must_be_string: str = "The user id must be a string."
user_id_not_provided: str = "A user id must be provided."
paper_trade_id_must_be_string: str = "The paper trade id must be a string."
paper_trade_id_not_provided: str = "A paper trade id must be provided."


# Creation Tests ----------------------------------------------------------------------------

def test_add_paper_trade_user_id_not_string(invalid_id, create_new_paper_trade):
    try:
        paper_trade_service.add_paper_trade(invalid_id, create_new_paper_trade)
        assert False
    except UserIdMustBeString as e:
        assert str(e) == user_id_must_be_string


# id missing
def test_add_paper_trade_user_id_missing(missing_id, create_new_paper_trade):
    try:
        paper_trade_service.add_paper_trade(missing_id, create_new_paper_trade)
        assert False
    except MissingUserId as e:
        assert str(e) == user_id_not_provided


# Read Tests --------------------------------------------------------------------------------

# id not string
def test_get_paper_trades_user_id_not_string(invalid_id):
    try:
        paper_trade_service.get_paper_trades(invalid_id)
        assert False
    except UserIdMustBeString as e:
        assert str(e) == user_id_must_be_string


# id missing
def test_get_paper_trades_user_id_missing(missing_id):
    try:
        paper_trade_service.get_paper_trades(missing_id)
        assert False
    except MissingUserId as e:
        assert str(e) == user_id_not_provided


# Update Tests ------------------------------------------------------------------------------

# id not string
def test_update_paper_trade_user_id_not_string(invalid_id):
    try:
        paper_trade_service.update_paper_trade_sell_price(invalid_id, 0, 111.11)
        assert False
    except UserIdMustBeString as e:
        assert str(e) == user_id_must_be_string


# id missing
def test_update_paper_trade_user_id_missing(missing_id):
    try:
        paper_trade_service.update_paper_trade_sell_price(missing_id, 0, 111.11)
        assert False
    except MissingUserId as e:
        assert str(e) == user_id_not_provided


# Delete Tests ------------------------------------------------------------------------------
# id not string
def test_delete_paper_trade_user_id_not_string(invalid_id):
    users: list = user_dao.get_all_users()
    trade_id: int = users[0]["paperTrades"][0]["tradeId"]
    try:
        paper_trade_service.delete_paper_trade(invalid_id, trade_id)
        assert False
    except UserIdMustBeString as e:
        assert str(e) == user_id_must_be_string


def test_delete_paper_trade_id_not_string(invalid_id):
    users: list = user_dao.get_all_users()
    user_id: str = users[0]["_id"]
    try:
        paper_trade_service.delete_paper_trade(user_id, invalid_id)
        assert False
    except PaperTradeException as e:
        assert str(e) == paper_trade_id_must_be_string


# id missing
def test_delete_paper_trade_no_user_id(missing_id):
    users: list = user_dao.get_all_users()
    trade_id: int = users[0]["paperTrades"][0]["tradeId"]
    try:
        paper_trade_service.delete_paper_trade(missing_id, trade_id)
        assert False
    except MissingUserId as e:
        assert str(e) == user_id_not_provided


def test_delete_paper_trade_no_id(missing_id):
    users: list = user_dao.get_all_users()
    user_id: str = users[0]["_id"]
    try:
        paper_trade_service.delete_paper_trade(user_id, missing_id)
        assert False
    except PaperTradeException as e:
        assert str(e) == paper_trade_id_not_provided
