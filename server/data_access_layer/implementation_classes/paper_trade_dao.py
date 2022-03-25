from pprint import pprint

from pymongo import MongoClient
from environment_variables import mongo_url
from server.data_access_layer.abstract_classes.paper_trade_dao import PaperTradeDAO
from server.entities.paper_trade import PaperTrade
from typing import List
from bson.objectid import ObjectId

# database connection -------------
connection_string = mongo_url
client = MongoClient(connection_string)
database = client.finance_app
collection = database.users


class PaperTradeDAOImp(PaperTradeDAO):
    # Create method -------
    def add_paper_trade(self, user_id: str, paper_trade: PaperTrade) -> dict:
        return collection.update_one({"_id": ObjectId(user_id)}, {"$push": {"paperTrades": paper_trade}})

    # Read methods --------
    def get_paper_trades(self, user_id: str) -> list:
        trades = collection.find_one({"_id": ObjectId(user_id)})
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


# deleted = collection.update_one({"_id": ObjectId("623ddc582a8e2cee29b0b62d")},
# {"$pull":{"paperTrades": {"tradeId": 7721}}})
# print(deleted.acknowledged)

# users[0]["paperTrades"][-1]["tradeId"]
# users = collection.find({"_id": ObjectId("623ddc582a8e2cee29b0b62d")})
# for user in users:
#     pprint(user["paperTrades"][-1]["tradeId"])
