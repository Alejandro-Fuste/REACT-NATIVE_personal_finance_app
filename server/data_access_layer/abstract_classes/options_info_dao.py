from abc import ABC, abstractmethod

import pandas


class OptionsInfoDAO(ABC):

    @abstractmethod
    def get_stock_price(self, ticker: str) -> float:
        pass

    @abstractmethod
    def get_calls(self, ticker: str) -> pandas:
        pass

    @abstractmethod
    def get_puts(self, ticker: str) -> pandas:
        pass

   