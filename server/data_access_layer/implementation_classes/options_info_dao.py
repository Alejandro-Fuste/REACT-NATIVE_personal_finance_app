from server.data_access_layer.abstract_classes.options_info_dao import OptionsInfoDAO

import yahoo_fin.stock_info as si
from yahoo_fin.options import get_options_chain


class OptionsInfoImp(OptionsInfoDAO):

    def get_live_stock_price(self, ticker: str) -> float:
        return si.get_live_price(ticker)

    def get_expiration_dates(self, ticker: str) -> list:
        pass

    def get_calls(self, ticker: str) -> dict:
        pass

    def get_puts(self, ticker: str) -> dict:
        pass


# print()
# print(isinstance(si.get_live_price("t"), float))
# options = get_options_chain("t")
# print(len(options["calls"]))

print(si.get_live_price("t"))

