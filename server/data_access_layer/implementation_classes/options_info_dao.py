import pandas

from server.data_access_layer.abstract_classes.options_info_dao import OptionsInfoDAO

from yahoo_fin import options
from yahoo_fin import stock_info


class OptionsInfoImp(OptionsInfoDAO):

    def get_stock_price(self, ticker: str) -> float:
        return stock_info.get_live_price(ticker)

    def get_calls(self, ticker: str) -> pandas:
        return options.get_calls(ticker)

    def get_puts(self, ticker: str) -> pandas:
        return options.get_puts(ticker)


# price = stock_info.get_live_price("t")
# # print(isinstance(calls.loc[4, "Strike"], float))
# print(float(price))


# for i in range(len(calls)):
#     print(calls.loc[i, "Strike"])
