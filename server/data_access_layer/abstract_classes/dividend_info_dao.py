from abc import ABC, abstractmethod

import pandas


class DividendInfoDao(ABC):

    @abstractmethod
    def get_tickers_dow(self) -> list:
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
    def get_dow_targets(self):
        pass

    @abstractmethod
    def get_dividend_investment_amount(self, tickers: list, stock_price: float, investment: float) -> list:
        pass
