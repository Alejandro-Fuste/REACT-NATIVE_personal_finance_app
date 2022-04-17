from abc import ABC, abstractmethod


class StockInfoDAO(ABC):

    @abstractmethod
    def get_stock_price(self, ticker: str):
        pass
