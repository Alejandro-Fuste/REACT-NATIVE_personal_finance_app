from server.data_access_layer.implementation_classes.paper_trade_dao import PaperTradeDAOImp
from server.entities.paper_trade import PaperTrade
from server.service_layer.abstract_classes.paper_trade_service_abs import PaperTradeService


class PaperTradeServiceImp(PaperTradeService):
    def __init__(self, paper_trade_dao):
        self.paper_trade_dao: PaperTradeDAOImp = paper_trade_dao

    def add_paper_trade(self, user_id: str, paper_trade: PaperTrade) -> dict:
        pass

    def get_paper_trades(self, user_id: str) -> list:
        pass

    def update_paper_trade_sell_price(self, user_id: str, paper_trade_index: int, sell_price: float) -> bool:
        pass

    def delete_paper_trade(self, user_id: str, paper_trade_id: int) -> int:
        pass



