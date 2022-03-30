from pprint import pprint

from pymongo import MongoClient
from environment_variables import mongo_url
from bson.objectid import ObjectId
from server.data_access_layer.abstract_classes.paper_trade_dao import PaperTradeDAO
from server.entities.paper_trade import PaperTrade
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


class PaperTradeDAOImp(PaperTradeDAO):
    # Create method -------
    def add_paper_trade(self, user_id: str, paper_trade: PaperTrade) -> dict:
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
    def update_paper_trade_sell_price(self, user_id: str, paper_trade_index: int, sell_price: float) -> bool:
        result = collection.update_one({"_id": ObjectId(user_id)},
                                       {"$set": {f"paperTrades.{paper_trade_index}.sellPrice": sell_price}})
        return result.acknowledged

    # Delete method -------
    def delete_paper_trade(self, user_id: str, paper_trade_id: int) -> int:
        deleted = collection.update_one({"_id": ObjectId(user_id)},
                                        {"$pull": {"paperTrades": {"tradeId": paper_trade_id}}})
        return deleted.acknowledged


trades = collection.find_one({"_id": ObjectId("6243cebc2fd82726c73f5bf1")})
pprint(trades)

# results = collection.find_one({"paperTrades": {"$elemMatch": {"tradeId": 6971}}})
# paperTrade = results["paperTrades"][0]

# pprint(isinstance(paperTrade, dict))

