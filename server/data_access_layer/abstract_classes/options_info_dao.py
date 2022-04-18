from abc import ABC, abstractmethod


class OptionsInfoDAO(ABC):

    @abstractmethod
    def get_live_stock_price(self, ticker: str) -> float:
        pass

    @abstractmethod
    def get_options(self, ticker: str) -> dict:
        pass
