from abc import ABC, abstractmethod

from server.django_app.api.entities.paper_trade import PaperTrade


class PaperTradeService(ABC):

    # Create method -------
    @abstractmethod
    def add_paper_trade(self, user_id: str, paper_trade: PaperTrade) -> dict:
        pass

    # Read methods --------
    @abstractmethod
    def get_paper_trades(self, user_id: str) -> list:
        pass

    # Update method -------
    @abstractmethod
    def update_paper_trade_sell_price(self, user_id: str, paper_trade_index: int, sell_price: float) -> bool:
        pass

    # Delete method -------
    @abstractmethod
    def delete_paper_trade(self, user_id: str, paper_trade_id: int) -> int:
        pass
