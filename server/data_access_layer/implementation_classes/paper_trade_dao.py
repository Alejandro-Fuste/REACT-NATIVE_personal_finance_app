from server.data_access_layer.abstract_classes.paper_trade_dao import PaperTradeDAO
from server.entities.paper_trade import PaperTrade


class PaperTradeDAOImp(PaperTradeDAO):
    def add_paper_trade(self, paper_trade: PaperTrade) -> dict:
        pass

    def update_paper_trade(self, paper_trade_id: int, paper_trade: PaperTrade) -> PaperTrade:
        pass

    def delete_paper_trade(self, paper_trade_id: int) -> int:
        pass
