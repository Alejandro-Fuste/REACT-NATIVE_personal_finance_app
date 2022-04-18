from abc import ABC, abstractmethod


class OptionsInfoDAO(ABC):

    @abstractmethod
    def get_live_stock_price(self, ticker: str) -> float:
        pass

    @abstractmethod
    def get_expiration_dates(self, ticker: str) -> list:
        pass

    @abstractmethod
    def get_calls(self, ticker: str) -> dict:
        pass

    @abstractmethod
    def get_puts(self, ticker: str) -> dict:
        pass

