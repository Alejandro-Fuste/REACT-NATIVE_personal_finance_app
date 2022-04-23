from server.data_access_layer.abstract_classes.options_info_dao import OptionsInfoDAO
from server.custom_exceptions.option_not_found import OptionNotFound

from yahoo_fin import options
from yahoo_fin import stock_info

import pandas

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


# # print(isinstance(calls.loc[4, "Strike"], float))
#
# # for i in range(len(calls)):
# #     print(calls.loc[i, "Strike"])

# dow = stock_info.tickers_dow()
# div = stock_info.get_dividends(dow[0], "01-01-2022")
# print(div)
# div_top = div.head()
# div_first_row = list(div_top.index)
# time = div_first_row[0]
# ftime = time.strftime('%Y-%m-%d')
# # print(ftime)
# print(div.loc[ftime, "dividend"])




