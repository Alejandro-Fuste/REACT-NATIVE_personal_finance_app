from pymongo import MongoClient
from environment_variables import mongo_url
from server.data_access_layer.abstract_classes.paper_trade_dao import PaperTradeDAO
from server.entities.paper_trade import PaperTrade

# database connection -------------
connection_string = mongo_url
client = MongoClient(connection_string)
database = client.finance_app
collection = database.users


class PaperTradeDAOImp(PaperTradeDAO):
    # Create method -------
    def add_paper_trade(self, user_id: str, paper_trade: PaperTrade) -> dict:
        return collection.update_one({})

    def update_paper_trade(self, user_id: str, paper_trade_id: int, paper_trade: PaperTrade) -> dict:
        pass

    def delete_paper_trade(self, user_id: str, paper_trade_id: int) -> int:
        pass
