from pprint import pprint

import pandas
import json

from server.data_access_layer.abstract_classes.dividend_info_dao import DividendInfoDao

from yahoo_fin import stock_info

from datetime import datetime


class DividendInfoImp(DividendInfoDao):
    # Get tickers -----------------------------------------------------------------
    def get_tickers_dow(self) -> list:
        return stock_info.tickers_dow()

    def get_tickers_nasdaq(self) -> list:
        return stock_info.tickers_nasdaq()

    def get_tickers_sp500(self) -> list:
        return stock_info.tickers_sp500()

    def sp500_ticker_dictionary(self) -> dict:
        begin = 0
        end = 36
        array = []
        tickers = self.get_tickers_sp500()

        for i in range(14):
            array.append({i: tickers[begin:end]})
            begin += 37
            end += 36

        return {"sp500": array}

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
            first_div_payment_date = None
            result = self.get_dividends_current_year(ticker)
            result_length = len(result)

            if result_length == 0:
                div += 0
            else:
                div = result.loc[result_length - 1, "dividend"]
                first_div_payment_date = result.loc[0, "date"].strftime('%m-%d-%Y')

            if div > 1.00:
                ticker_list.append({"ticker": ticker, "amount": div, "first_payment_date": first_div_payment_date})

        return ticker_list

    def get_dow_targets(self):
        companies = self.get_tickers_dow()
        res = self.get_targeted_dividends(companies)
        return res

    def get_dividend_investment_amount(self, dividend: float, stock_price: float, investment: float) -> float:
        amount = (investment / stock_price) * dividend
        return amount

    # Write to json file --------------------------------------------------------------

    @staticmethod
    def write_to_json():
        json_string = json.dumps(div.sp500_ticker_dictionary(), indent=1)
        pprint(json_string)

        with open('tickers.json', 'w') as outfile:
            outfile.writelines(json_string)


div = DividendInfoImp()
pprint(div.sp500_ticker_dictionary())

# print(f'GS - {round(div.get_dividend_investment_amount(2.00, 319.77, 5000.00),2)}')
# print(f'HD - {round(div.get_dividend_investment_amount(1.90, 300.11, 5000.00),2)}')
# print(f'UNH - {round(div.get_dividend_investment_amount(2.00, 520.94, 5000.00),2)}')
