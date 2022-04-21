import pandas

from server.custom_exceptions.input_not_string import InputNotString
from server.custom_exceptions.input_missing import InputMissing

from server.data_access_layer.implementation_classes.options_info_dao import OptionsInfoImp
from server.service_layer.abstract_classes.options_info_service_abs import OptionsInfoService

input_must_be_string: str = "The input must be a string."
input_not_provided: str = "An input must be provided."


class OptionsInfoServiceImp(OptionsInfoService):
    def __init__(self, options_info_dao):
        self.options_info_dao: OptionsInfoImp = options_info_dao

    def get_stock_price(self, ticker: str) -> float:
        pass

    def get_calls(self, ticker: str) -> pandas:
        pass

    def get_puts(self, ticker: str) -> pandas:
        pass

