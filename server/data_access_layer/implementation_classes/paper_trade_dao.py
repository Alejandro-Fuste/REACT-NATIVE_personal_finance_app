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
    def update_paper_trade(self, user_id: str, paper_trade_id: int, paper_trade: PaperTrade) -> dict:
        pass

    # Delete method -------
    def delete_paper_trade(self, user_id: str, paper_trade_id: int) -> int:
        pass


# result = collection.find({"_id": ObjectId("623ddc582a8e2cee29b0b62d")})
# for x in result:
#     print(x["paperTrades"])
#     print(isinstance(x["paperTrades"], list))



