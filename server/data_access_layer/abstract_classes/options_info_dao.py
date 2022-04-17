from abc import ABC, abstractmethod


class StockInfoDAO(ABC):

    @abstractmethod
    def get_live_stock_price(self, ticker: str) -> float:
        pass
