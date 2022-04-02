from server.custom_exceptions.user_id_must_be_string import UserIdMustBeString
from server.custom_exceptions.user_id_not_provided import MissingUserId
from server.custom_exceptions.paper_trade_exception import PaperTradeException
from server.custom_exceptions.input_not_string import InputNotString

from server.data_access_layer.implementation_classes.paper_trade_dao import PaperTradeDAOImp
from server.entities.paper_trade import PaperTrade
from server.service_layer.abstract_classes.paper_trade_service_abs import PaperTradeService

user_id_must_be_string: str = "The user id must be a string."
user_id_not_provided: str = "A user id must be provided."
paper_trade_id_must_be_string: str = "The paper trade id must be a string."
paper_trade_id_not_provided: str = "A paper trade id must be provided."
paper_trade_index_must_be_string: str = "The paper trade index must be a string."
paper_trade_value_must_be_string: str = "The paper trade object value must be a string."
paper_trade_value_must_be_float: str = "The paper trade object value must be a float."
paper_trade_value_not_provided: str = "The paper trade object value must be provided."
paper_trade_index_not_provided: str = "A paper trade index must be provided."
sell_price_must_be_string: str = "The sell price must be a string."
sell_price_index_not_provided: str = "A sell price must be provided."
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

        # check if value is a string
        if isinstance(paper_trade["ticker"], str) is False or isinstance(paper_trade["tradeType"], str) is False \
                or isinstance(paper_trade["expirationDate"], str) is False \
                or isinstance(paper_trade["strategyType"], str) is False:
            raise InputNotString(paper_trade_value_must_be_string)

        # check if value is a float
        if isinstance(paper_trade["callPrice"], float) is False or isinstance(paper_trade["putPrice"], float) is False \
                or isinstance(paper_trade["callBreakevenPoint"], float) is False\
                or isinstance(paper_trade["putBreakevenPoint"], float) is False\
                or isinstance(paper_trade["straddle_call_breakeven_point"], float) is False\
                or isinstance(paper_trade["straddle_call_breakeven_point"], float) is False\
                or isinstance(paper_trade["sellPrice"], float) is False\
                or isinstance(paper_trade["costPrice"], float) is False\
                or isinstance(paper_trade["totalSell"], float) is False\
                or isinstance(paper_trade["totalCost"], float) is False\
                or isinstance(paper_trade["netProfit"], float) is False\
                or isinstance(paper_trade["strikePrice"], float) is False:
            raise PaperTradeException(paper_trade_value_must_be_float)

        # check if value is an integer
        if isinstance(paper_trade["tradeId"], int) is False \
                or isinstance(paper_trade["netProfitPercentage"], int) is False:
            raise InputNotString(user_id_must_be_string)

        # check if value is not empty
        if len(paper_trade["tradeId"].strip()) == 0 or len(paper_trade["ticker"].strip()) == 0\
                or len(paper_trade["strikePrice"].strip()) == 0 \
                or len(paper_trade["tradeType"].strip()) == 0\
                or len(paper_trade["expirationDate"].strip()) == 0\
                or len(paper_trade["strategyType"].strip()) == 0\
                or len(paper_trade["callPrice"].strip()) == 0\
                or len(paper_trade["putPrice"].strip()) == 0\
                or len(paper_trade["callBreakevenPoint"].strip()) == 0\
                or len(paper_trade["putBreakevenPoint"].strip()) == 0\
                or len(paper_trade["straddle_call_breakeven_point"].strip()) == 0\
                or len(paper_trade["straddle_put_breakeven_point"].strip()) == 0\
                or len(paper_trade["sellPrice"].strip()) == 0\
                or len(paper_trade["costPrice"].strip()) == 0\
                or len(paper_trade["totalSell"].strip()) == 0\
                or len(paper_trade["totalCost"].strip()) == 0\
                or len(paper_trade["netProfit"].strip()) == 0\
                or len(paper_trade["netProfitPercentage"].strip()) == 0:
            raise PaperTradeException(paper_trade_value_not_provided)

        return self.paper_trade_dao.add_paper_trade(user_id, paper_trade)

    def get_paper_trades(self, user_id: str) -> list:
        pass

    def update_paper_trade_sell_price(self, user_id: str, paper_trade_index: int, sell_price: float) -> bool:
        pass

    def delete_paper_trade(self, user_id: str, paper_trade_id: int) -> int:
        pass
