from pprint import pprint

from server.data_access_layer.abstract_classes.options_info_dao import OptionsInfoDAO
from server.custom_exceptions.option_not_found import OptionNotFound

from yahoo_fin import options
from yahoo_fin import stock_info

import pandas
from datetime import datetime

stock_not_found = "Your stock was not able to be located."


class OptionsInfoImp(OptionsInfoDAO):

    # Get stock price -------------------------------------------------------------
    def get_stock_price(self, ticker: str) -> float:
        try:
            price = stock_info.get_live_price(ticker)
            return price
        except AssertionError as e:
            return e.args[0]['chart']['error']['description']

    # Get options -----------------------------------------------------------------
    def get_calls(self, ticker: str) -> pandas:
        calls = options.get_calls(ticker)
        columns = list(calls.columns)

        if columns[0] == 'Contract Name':
            return calls
        else:
            raise OptionNotFound(stock_not_found)

    def get_puts(self, ticker: str) -> pandas:
        puts = options.get_puts(ticker)
        columns = list(puts.columns)

        if columns[0] == 'Contract Name':
            return puts
        else:
            raise OptionNotFound(stock_not_found)

    # Get tickers -----------------------------------------------------------------
    def get_tickers_dow(self) -> list:
        return stock_info.tickers_dow()

    def get_tickers_ftse100(self) -> list:
        return stock_info.tickers_ftse100()

    def get_tickers_ftse250(self) -> list:
        return stock_info.tickers_ftse250()

    def get_tickers_nasdaq(self) -> list:
        return stock_info.tickers_nasdaq()

    def get_tickers_sp500(self) -> list:
        return stock_info.tickers_sp500()

    # Get Dividends -----------------------------------------------------------------
    def get_all_dividends(self, ticker: str) -> pandas:
        return stock_info.get_dividends(ticker, index_as_date=False)

    def get_dividends_for_specific_period(self, ticker: str, start_date: str, end_date: str) -> pandas:
        return stock_info.get_dividends(ticker, start_date, end_date, index_as_date=False)

    def get_dividends_previous_year(self, ticker: str) -> pandas:
        previous_year = datetime.now().year - 1
        start_date = f'01-01-{previous_year}'
        end_date = f'12-31-{previous_year}'
        return stock_info.get_dividends(ticker, start_date, end_date, index_as_date=False)

    def get_dividends_current_year(self, ticker: str) -> pandas:
        current_year = datetime.now().year
        start_date = f'01-01-{current_year}'
        return stock_info.get_dividends(ticker, start_date, index_as_date=False)

    def get_targeted_dividends(self, tickers: list) -> list:
        ticker_list = []
        for ticker in tickers:
            div = 0
            result = option.get_dividends_current_year(ticker)
            result_length = len(result)

            if result_length == 0:
                div += 0
            else:
                div = result.loc[result_length - 1, "dividend"]

            if div > 1.00:
                ticker_list.append({"ticker": ticker, "amount": div})

        return ticker_list

    def get_dow_targets(self):
        companies = option.get_tickers_dow()
        res = option.get_targeted_dividends(companies)
        return res


option = OptionsInfoImp()

# pprint(res)
print(option.get_dow_targets())
