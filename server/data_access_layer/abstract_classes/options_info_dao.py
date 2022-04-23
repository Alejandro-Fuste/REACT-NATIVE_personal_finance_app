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

    @abstractmethod
    def get_tickers_dow(self) -> list:
        pass

    @abstractmethod
    def get_tickers_ftse100(self) -> list:
        pass

    @abstractmethod
    def get_tickers_ftse250(self) -> list:
        pass

    @abstractmethod
    def get_tickers_nasdaq(self) -> list:
        pass

    @abstractmethod
    def get_tickers_sp500(self) -> list:
        pass

    @abstractmethod
    def get_all_dividends(self, ticker: str) -> pandas:
        pass

    @abstractmethod
    def get_dividends_for_specific_period(self, ticker: str, start_date: str, end_date: str) -> pandas:
        pass

    @abstractmethod
    def get_dividends_previous_year(self, ticker: str) -> pandas:
        pass

    @abstractmethod
    def get_dividends_current_year(self, ticker: str) -> pandas:
        pass

    @abstractmethod
    def get_targeted_dividends(self, tickers: list) -> list:
        pass

    @abstractmethod
    def get_dow_targets(self) -> list:
        pass

    @abstractmethod
    def get_dividend_investment_amount(self, tickers: list) -> dict:
        pass
