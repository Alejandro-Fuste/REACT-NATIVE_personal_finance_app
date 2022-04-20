import pandas

from server.data_access_layer.abstract_classes.options_info_dao import OptionsInfoDAO

from yahoo_fin import options


class OptionsInfoImp(OptionsInfoDAO):

    def get_stock_price(self, ticker: str) -> float:
        pass

    def get_calls(self, ticker: str) -> pandas:
        pass

    def get_puts(self, ticker: str) -> pandas:
        pass


calls = options.get_calls("t")
# print(isinstance(calls.loc[4, "Strike"], float))
print(type(calls))
print(isinstance(calls, pandas))

# for i in range(len(calls)):
#     print(calls.loc[i, "Strike"])
