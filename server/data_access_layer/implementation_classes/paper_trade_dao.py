from pymongo import MongoClient
from server.environment_variables import mongo_url
from bson.objectid import ObjectId
from server.data_access_layer.abstract_classes.paper_trade_dao import PaperTradeDAO
from server.entities.paper_trade import PaperTrade
from server.entities.option import Option
from server.custom_exceptions.duplicate_trade import DuplicateTrade
from server.custom_exceptions.trade_not_found import TradeNotFound
from server.custom_exceptions.user_not_found import UserNotFound
from server.custom_exceptions.no_trades import NoTrades

# database connection -------------
connection_string = mongo_url
client = MongoClient(connection_string)
database = client.finance_app
collection = database.users

duplicate_trade_message: str = "This trade already exists."
user_not_found: str = "The user could not be found."
user_has_no_trades: str = "Currently, user does not have any trades."
paper_trade_not_found: str = "This trade could not be found."


class PaperTradeDAOImp(PaperTradeDAO):
    # Create method -------
    def add_paper_trade(self, user_id: str, paper_trade: Option) -> dict:
        trade_id: int = paper_trade["tradeId"]
        result = collection.find_one({"paperTrades": {"$elemMatch": {"tradeId": trade_id}}})

        if result is None:
            return collection.update_one({"_id": ObjectId(user_id)}, {"$push": {"paperTrades": paper_trade}})
        else:
            raise DuplicateTrade(duplicate_trade_message)

    # Read methods --------
    def get_paper_trades(self, user_id: str) -> list:
        trades = collection.find_one({"_id": ObjectId(user_id)})

        if trades is None:
            raise UserNotFound(user_not_found)
        elif len(trades["paperTrades"]) == 0:
            raise NoTrades(user_has_no_trades)
        else:
            return trades["paperTrades"]

    # Update method -------
    def update_paper_trade(self, user_id: str, paper_trade_index: int, paper_trade: PaperTrade) -> bool:
        user = collection.find_one({"_id": ObjectId(user_id)})

        if user is None:
            raise UserNotFound(user_not_found)
        elif len(user["paperTrades"]) == 0:
            raise TradeNotFound(paper_trade_not_found)
        else:
            result = collection.update_one({"_id": ObjectId(user_id)},
                                           {"$set": {f"paperTrades.{paper_trade_index}.callSellPrice":
                                            paper_trade["callSellPrice"],
                                                     f"paperTrades.{paper_trade_index}.putSellPrice":
                                                         paper_trade["putSellPrice"],
                                                     f"paperTrades.{paper_trade_index}.status": "closed",
                                                     f"paperTrades.{paper_trade_index}.costPrice":
                                                         paper_trade["costPrice"],
                                                     f"paperTrades.{paper_trade_index}.totalSell":
                                                         paper_trade["totalSell"],
                                                     f"paperTrades.{paper_trade_index}.totalCost":
                                                         paper_trade["totalCost"],
                                                     f"paperTrades.{paper_trade_index}.netProfit":
                                                         paper_trade["netProfit"],
                                                     f"paperTrades.{paper_trade_index}.netProfitPercentage":
                                                         paper_trade["netProfitPercentage"],
                                                     }})
            return result.acknowledged

    # Delete method -------
    def delete_paper_trade(self, user_id: str, paper_trade_id: int) -> int:
        user = collection.find_one({"_id": ObjectId(user_id)})

        if user is None:
            raise UserNotFound(user_not_found)
        elif len(user["paperTrades"]) == 0:
            raise TradeNotFound(paper_trade_not_found)
        else:
            deleted = collection.update_one({"_id": ObjectId(user_id)},
                                            {"$pull": {"paperTrades": {"tradeId": paper_trade_id}}})
            return deleted.acknowledged
