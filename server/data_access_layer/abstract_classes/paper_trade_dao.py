from abc import ABC, abstractmethod
from typing import List

from server.entities.paper_trade import PaperTrade


class PaperTradeDAO(ABC):

    # Create method -------
    @abstractmethod
    def add_paper_trade(self, paper_trade: PaperTrade) -> dict:
        pass

    # Read methods --------
    def get_paper_trade(self, paper_trade_id: int) -> PaperTrade:
        pass

    def get_paper_trades(self) -> List[PaperTrade]:
        pass

    # Update method -------
    @abstractmethod
    def update_paper_trade(self, paper_trade_id: int, paper_trade: PaperTrade) -> PaperTrade:
        pass

    # Delete method -------
    @abstractmethod
    def delete_paper_trade(self, paper_trade_id: int) -> int:
        pass
