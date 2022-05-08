from abc import ABC, abstractmethod

import pandas

from server.entities.option import Option


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

    @abstractmethod
    def get_targeted_options(self, ticker: str, expiration_date: str) -> list:
        pass

    @abstractmethod
    def get_option_info(self, data: dict) -> Option:
        pass
