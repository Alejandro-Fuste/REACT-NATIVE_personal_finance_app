from server.django_app.api.custom_exceptions.user_id_must_be_string import UserIdMustBeString
from server.django_app.api.custom_exceptions.user_id_not_provided import MissingUserId
from server.django_app.api.custom_exceptions.paper_trade_exception import PaperTradeException
from server.django_app.api.custom_exceptions.input_not_string import InputNotString

from server.django_app.api.data_access_layer.implementation_classes import PaperTradeDAOImp
from server.django_app.api.entities.paper_trade import PaperTrade
from server.django_app.api.service_layer.abstract_classes.paper_trade_service_abs import PaperTradeService

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
sell_price_not_provided: str = "A sell price must be provided."
sell_price_negative: str = "A sell price must be a positive number."


class PaperTradeServiceImp(PaperTradeService):
    def __init__(self, paper_trade_dao):
        self.paper_trade_dao: PaperTradeDAOImp = paper_trade_dao

    def add_paper_trade(self, user_id: str, paper_trade: PaperTrade) -> dict:
        # check user_id is a string
        if isinstance(user_id, str) is False:
            raise UserIdMustBeString(user_id_must_be_string)

        # check user_id not empty
        if len(user_id.strip()) == 0:
            raise MissingUserId(user_id_not_provided)

        # check if value is not empty
        if paper_trade["tradeId"] is None or len(paper_trade["ticker"].strip()) == 0 \
                or paper_trade["strikePrice"] is None \
                or len(paper_trade["tradeType"].strip()) == 0 \
                or len(paper_trade["expirationDate"].strip()) == 0 \
                or len(paper_trade["strategyType"].strip()) == 0 \
                or paper_trade["callPrice"] is None \
                or paper_trade["putPrice"] is None \
                or paper_trade["callBreakevenPoint"] is None \
                or paper_trade["putBreakevenPoint"] is None \
                or paper_trade["straddle_call_breakeven_point"] is None \
                or paper_trade["straddle_put_breakeven_point"] is None \
                or paper_trade["sellPrice"] is None \
                or paper_trade["costPrice"] is None \
                or paper_trade["totalSell"] is None \
                or paper_trade["totalCost"] is None \
                or paper_trade["netProfit"] is None \
                or paper_trade["netProfitPercentage"] is None:
            raise PaperTradeException(paper_trade_value_not_provided)

        # check if value is a string
        if isinstance(paper_trade["ticker"], str) is False or isinstance(paper_trade["tradeType"], str) is False \
                or isinstance(paper_trade["expirationDate"], str) is False \
                or isinstance(paper_trade["strategyType"], str) is False:
            raise InputNotString(paper_trade_value_must_be_string)

        # check if value is a float
        if isinstance(paper_trade["callPrice"], float) is False or isinstance(paper_trade["putPrice"], float) is False \
                or isinstance(paper_trade["callBreakevenPoint"], float) is False \
                or isinstance(paper_trade["putBreakevenPoint"], float) is False \
                or isinstance(paper_trade["straddle_call_breakeven_point"], float) is False \
                or isinstance(paper_trade["straddle_call_breakeven_point"], float) is False \
                or isinstance(paper_trade["sellPrice"], float) is False \
                or isinstance(paper_trade["costPrice"], float) is False \
                or isinstance(paper_trade["totalSell"], float) is False \
                or isinstance(paper_trade["totalCost"], float) is False \
                or isinstance(paper_trade["netProfit"], float) is False \
                or isinstance(paper_trade["strikePrice"], float) is False:
            raise PaperTradeException(paper_trade_value_must_be_float)

        # check if value is an integer
        if isinstance(paper_trade["tradeId"], int) is False \
                or isinstance(paper_trade["netProfitPercentage"], int) is False:
            raise InputNotString(user_id_must_be_string)

        return self.paper_trade_dao.add_paper_trade(user_id, paper_trade)

    def get_paper_trades(self, user_id: str) -> list:
        # check user_id is a string
        if isinstance(user_id, str) is False:
            raise UserIdMustBeString(user_id_must_be_string)

        # check user_id not empty
        if len(user_id.strip()) == 0:
            raise MissingUserId(user_id_not_provided)

        return self.paper_trade_dao.get_paper_trades(user_id)

    def update_paper_trade_sell_price(self, user_id: str, paper_trade_index: int, sell_price: float) -> bool:
        # check user_id is a string
        if isinstance(user_id, str) is False:
            raise UserIdMustBeString(user_id_must_be_string)

        # check user_id not empty
        if len(user_id.strip()) == 0:
            raise MissingUserId(user_id_not_provided)

        # check paper_trade_index is missing
        if paper_trade_index is None:
            raise PaperTradeException(paper_trade_index_not_provided)

        # check paper_trade_index is an int
        if isinstance(paper_trade_index, int) is False:
            raise PaperTradeException(paper_trade_index_must_be_int)

        # check sell_price is missing
        if sell_price is None:
            raise PaperTradeException(sell_price_not_provided)

        # check sell_price is a float
        if isinstance(sell_price, float) is False:
            raise PaperTradeException(sell_price_must_be_float)

        # check if sell_price is a negative number
        if sell_price < 0:
            raise PaperTradeException(sell_price_negative)

        return self.paper_trade_dao.update_paper_trade_sell_price(user_id, paper_trade_index, sell_price)

    def delete_paper_trade(self, user_id: str, paper_trade_id: int) -> int:
        # check user_id is a string
        if isinstance(user_id, str) is False:
            raise UserIdMustBeString(user_id_must_be_string)

        # check user_id not empty
        if len(user_id.strip()) == 0:
            raise MissingUserId(user_id_not_provided)

        # check paper_trade_id is missing
        if paper_trade_id is None:
            raise PaperTradeException(paper_trade_id_not_provided)

        # check paper_trade_id is an int
        if isinstance(paper_trade_id, int) is False:
            raise PaperTradeException(paper_trade_id_must_be_int)

        return self.paper_trade_dao.delete_paper_trade(user_id, paper_trade_id)
