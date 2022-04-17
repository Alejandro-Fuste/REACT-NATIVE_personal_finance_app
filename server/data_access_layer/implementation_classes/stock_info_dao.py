from server.data_access_layer.abstract_classes.stock_info_dao import StockInfoDAO

import yahoo_fin.stock_info as si


class StockInfoImp(StockInfoDAO):
    def get_live_stock_price(self, ticker: str) -> float:
        return si.get_live_price("t")


# print()
# print(isinstance(si.get_live_price("t"), float))
