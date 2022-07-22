from server.custom_exceptions.input_missing import InputMissing
from server.custom_exceptions.input_not_int import InputNotInteger
from server.custom_exceptions.paper_trade_id_missing import PaperTradeIdMissing
from server.custom_exceptions.paper_trade_id_not_int import PaperTradeIdNotInt
from server.custom_exceptions.sell_price_negative import SellPriceNegative
from server.custom_exceptions.sell_price_not_float import SellPriceNotFloat
from server.custom_exceptions.user_id_must_be_string import UserIdMustBeString
from server.custom_exceptions.user_id_not_provided import MissingUserId
from server.custom_exceptions.paper_trade_exception import PaperTradeException
from server.custom_exceptions.input_not_string import InputNotString
from server.custom_exceptions.value_not_float_in_option import ValueNotFloat
from server.custom_exceptions.value_missing_from_option import ValueMissing

from server.data_access_layer.implementation_classes.paper_trade_dao import PaperTradeDAOImp
from server.service_layer.abstract_classes.paper_trade_service_abs import PaperTradeService

from server.entities.option import Option
from server.entities.paper_trade import PaperTrade

user_id_must_be_string: str = "The user id must be a string."
user_id_not_provided: str = "A user id must be provided."
paper_trade_id_must_be_int: str = "The paper trade id must be an integer."
paper_trade_id_not_provided: str = "A paper trade id must be provided."
paper_trade_index_must_be_int: str = "The paper trade index must be a integer."
paper_trade_value_must_be_string: str = "The paper trade object value must be a string."
paper_trade_value_must_be_float: str = "The paper trade object value must be a float."
paper_trade_value_must_be_int: str = "The paper trade object value must be an integer."
paper_trade_value_not_provided: str = "The paper trade object value must be provided."
paper_trade_index_not_provided: str = "A paper trade index must be provided."
sell_price_must_be_float: str = "The sell price must be a float."
sell_price_not_provided: str = "A sell price must be provided."
sell_price_negative: str = "A sell price must be a positive number."
value_not_float_in_object: str = "The object has a value that is not a float."
value_not_int_in_object: str = "The object has a value that is not an integer."
value_missing_from_object: str = "The object has a missing value."


class PaperTradeServiceImp(PaperTradeService):
    def __init__(self, paper_trade_dao):
        self.paper_trade_dao: PaperTradeDAOImp = paper_trade_dao

    def add_paper_trade(self, user_id: str, pending_option: dict) -> dict:
        # check user_id is a string
        if isinstance(user_id, str) is False:
            raise UserIdMustBeString(user_id_must_be_string)

        # check user_id not empty
        if len(user_id.strip()) == 0:
            raise MissingUserId(user_id_not_provided)

        # check if value is a string
        if isinstance(pending_option["ticker"], str) is False \
                or isinstance(pending_option["expirationDate"], str) is False \
                or isinstance(pending_option["strategyType"], str) is False:
            raise InputNotString(paper_trade_value_must_be_string)

        # check if value is not empty
        if len(pending_option["ticker"].strip()) == 0 \
                or pending_option["strikePrice"] is None \
                or pending_option["stockPrice"] is None \
                or len(pending_option["expirationDate"].strip()) == 0 \
                or len(pending_option["strategyType"].strip()) == 0 \
                or pending_option["contracts"] is None \
                or pending_option["callPrice"] is None \
                or pending_option["putPrice"] is None:
            raise PaperTradeException(paper_trade_value_not_provided)

        # check if value is a float
        if isinstance(pending_option["callPrice"], float) is False \
                or isinstance(pending_option["putPrice"], float) is False \
                or isinstance(pending_option["stockPrice"], float) is False \
                or isinstance(pending_option["strikePrice"], float) is False:
            raise PaperTradeException(paper_trade_value_must_be_float)

        # check if value is an integer
        if isinstance(pending_option["contracts"], int) is False:
            raise InputNotInteger(paper_trade_value_must_be_int)

        paper_trade = Option(pending_option["ticker"], pending_option["strikePrice"], pending_option["stockPrice"],
                             pending_option["expirationDate"], pending_option["contracts"],
                             pending_option["strategyType"], pending_option["callPrice"],
                             pending_option["putPrice"])

        return self.paper_trade_dao.add_paper_trade(user_id, paper_trade.make_dictionary())

    def get_paper_trades(self, user_id: str) -> list:
        # check user_id is a string
        if isinstance(user_id, str) is False:
            raise UserIdMustBeString(user_id_must_be_string)

        # check user_id not empty
        if len(user_id.strip()) == 0:
            raise MissingUserId(user_id_not_provided)

        return self.paper_trade_dao.get_paper_trades(user_id)

    def update_paper_trade(self, user_id: str, paper_trade_index: int, option_update: dict) -> bool:
        # check user_id is a string
        if isinstance(user_id, str) is False:
            raise UserIdMustBeString(user_id_must_be_string)

        # check user_id not empty
        if len(user_id.strip()) == 0:
            raise MissingUserId(user_id_not_provided)

        # check paper_trade_index is missing
        if paper_trade_index is None:
            raise InputMissing(paper_trade_index_not_provided)

        # check paper_trade_index is an int
        if isinstance(paper_trade_index, int) is False:
            raise InputNotInteger(paper_trade_index_must_be_int)

        # check if values are missing
        if option_update["tradeId"] is None \
                or option_update["contracts"] is None \
                or option_update["callPrice"] is None \
                or option_update["putPrice"] is None \
                or option_update["callSellPrice"] is None \
                or option_update["putSellPrice"] is None:
            raise ValueMissing(value_missing_from_object)

        # check sell_price is a float
        if isinstance(option_update["callSellPrice"], float) is False \
                or isinstance(option_update["putSellPrice"], float) is False:
            raise SellPriceNotFloat(sell_price_must_be_float)

        # check if value is a float
        if isinstance(option_update["callPrice"], float) is False \
                or isinstance(option_update["putPrice"], float) is False:
            raise ValueNotFloat(value_not_float_in_object)

        # check if value is an integer
        if isinstance(option_update["contracts"], int) is False \
                or isinstance(option_update["tradeId"], int) is False:
            raise InputNotInteger(value_not_int_in_object)

        # check if sell prices are a negative number
        if option_update["callSellPrice"] < 0 \
                or option_update["putSellPrice"] < 0:
            raise SellPriceNegative(sell_price_negative)

        paper_trade = PaperTrade(option_update["tradeId"], option_update["contracts"], option_update["callPrice"],
                                 option_update["putPrice"], option_update["callSellPrice"],
                                 option_update["putSellPrice"])

        return self.paper_trade_dao.update_paper_trade(user_id, paper_trade_index, paper_trade.make_dictionary())

    def delete_paper_trade(self, user_id: str, paper_trade_id: int) -> int:
        # check user_id is a string
        if isinstance(user_id, str) is False:
            raise UserIdMustBeString(user_id_must_be_string)

        # check user_id not empty
        if len(user_id.strip()) == 0:
            raise MissingUserId(user_id_not_provided)

        # check paper_trade_id is missing
        if paper_trade_id is None:
            raise PaperTradeIdMissing(paper_trade_id_not_provided)

        # check paper_trade_id is an int
        if isinstance(paper_trade_id, int) is False:
            raise PaperTradeIdNotInt(paper_trade_id_must_be_int)

        return self.paper_trade_dao.delete_paper_trade(user_id, paper_trade_id)
