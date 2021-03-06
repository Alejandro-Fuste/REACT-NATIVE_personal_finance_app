from abc import ABC, abstractmethod

from server.entities.option import Option
from server.entities.paper_trade import PaperTrade


class PaperTradeDAO(ABC):

    # Create method -------
    @abstractmethod
    def add_paper_trade(self, user_id: str, paper_trade: Option) -> dict:
        pass

    # Read methods --------
    @abstractmethod
    def get_paper_trades(self, user_id: str) -> list:
        pass

    # Update method -------
    @abstractmethod
    def update_paper_trade(self, user_id: str, paper_trade_index: int, paper_trade: PaperTrade) -> bool:
        pass

    # Delete method -------
    @abstractmethod
    def delete_paper_trade(self, user_id: str, paper_trade_id: int) -> int:
        pass
