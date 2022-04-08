from server.custom_exceptions.user_id_must_be_string import UserIdMustBeString
from server.custom_exceptions.user_id_not_provided import MissingUserId
from server.custom_exceptions.paper_trade_exception import PaperTradeException

from server.django_app.api.data_access_layer.implementation_classes.user_dao import UserDAO, UserDAOImp
from server.django_app.api.data_access_layer.abstract_classes.paper_trade_dao import PaperTradeDAO
from server.django_app.api.data_access_layer.implementation_classes.paper_trade_dao import PaperTradeDAOImp

from server.django_app.api.service_layer.implementation_classes.paper_trade_service import PaperTradeService, PaperTradeServiceImp

user_dao: UserDAO = UserDAOImp()
paper_trade_dao: PaperTradeDAO = PaperTradeDAOImp()
paper_trade_service: PaperTradeService = PaperTradeServiceImp(paper_trade_dao)

user_id_must_be_string: str = "The user id must be a string."
user_id_not_provided: str = "A user id must be provided."
paper_trade_id_must_be_int: str = "The paper trade id must be an integer."
paper_trade_id_not_provided: str = "A paper trade id must be provided."
paper_trade_index_must_be_int: str = "The paper trade index must be a integer."
paper_trade_value_must_be_string: str = "The paper trade object value must be a string."
paper_trade_value_must_be_float: str = "The paper trade object value must be a float."
paper_trade_value_not_provided: str = "The paper trade object value must be provided."
paper_trade_index_not_provided: str = "A paper trade index must be provided."
sell_price_must_be_float: str = "The sell price must be a float."
sell_price_index_not_provided: str = "A sell price must be provided."
sell_price_negative: str = "A sell price must be a positive number."


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


# value in new trade is not a number
def test_add_paper_trade_value_not_number(bad_id, trade_value_not_number):
    try:
        paper_trade_service.add_paper_trade(bad_id, trade_value_not_number)
        assert False
    except PaperTradeException as e:
        assert str(e) == paper_trade_value_must_be_float


# value in new trade is missing
def test_add_paper_trade_value_missing(bad_id, trade_value_missing):
    try:
        paper_trade_service.add_paper_trade(bad_id, trade_value_missing)
        assert False
    except PaperTradeException as e:
        assert str(e) == paper_trade_value_not_provided


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


# index not int
def test_update_paper_trade_index_not_int(bad_id, invalid_id):
    try:
        paper_trade_service.update_paper_trade_sell_price(bad_id, '0', 111.11)
        assert False
    except PaperTradeException as e:
        assert str(e) == paper_trade_index_must_be_int


# index missing
def test_update_paper_trade_index_missing(bad_id, missing_paper_trade_id):
    try:
        paper_trade_service.update_paper_trade_sell_price(bad_id, missing_paper_trade_id, 111.11)
        assert False
    except PaperTradeException as e:
        assert str(e) == paper_trade_index_not_provided


# sell price not float
def test_update_paper_trade_sell_price_not_float(bad_id):
    try:
        paper_trade_service.update_paper_trade_sell_price(bad_id, 0, "111.11")
        assert False
    except PaperTradeException as e:
        assert str(e) == sell_price_must_be_float


# sell price missing
def test_update_paper_trade_sell_price_missing(bad_id, missing_paper_trade_id):
    try:
        paper_trade_service.update_paper_trade_sell_price(bad_id, 0, missing_paper_trade_id)
        assert False
    except PaperTradeException as e:
        assert str(e) == sell_price_index_not_provided


# sell price negative number
def test_update_paper_trade_sell_price_negative(bad_id):
    try:
        paper_trade_service.update_paper_trade_sell_price(bad_id, 0, -111.11)
        assert False
    except PaperTradeException as e:
        assert str(e) == sell_price_negative


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


def test_delete_paper_trade_id_not_int(bad_id):
    try:
        paper_trade_service.delete_paper_trade(bad_id, bad_id)
        assert False
    except PaperTradeException as e:
        assert str(e) == paper_trade_id_must_be_int


# id missing
def test_delete_paper_trade_no_user_id(missing_id):
    users: list = user_dao.get_all_users()
    trade_id: int = users[0]["paperTrades"][0]["tradeId"]
    try:
        paper_trade_service.delete_paper_trade(missing_id, trade_id)
        assert False
    except MissingUserId as e:
        assert str(e) == user_id_not_provided


def test_delete_paper_trade_no_id(bad_id, missing_paper_trade_id):
    try:
        paper_trade_service.delete_paper_trade(bad_id, missing_paper_trade_id)
        assert False
    except PaperTradeException as e:
        assert str(e) == paper_trade_id_not_provided
