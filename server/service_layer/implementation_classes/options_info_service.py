import pandas

from server.data_access_layer.implementation_classes.options_info_dao import OptionsInfoImp
from server.service_layer.abstract_classes.options_info_service_abs import OptionsInfoService


class OptionsInfoServiceImp(OptionsInfoService):
    def __init__(self, options_info_dao):
        self.options_info_dao: OptionsInfoImp = options_info_dao

    def get_stock_price(self, ticker: str) -> float:
        pass

    def get_calls(self, ticker: str) -> pandas:
        pass

    def get_puts(self, ticker: str) -> pandas:
        pass

