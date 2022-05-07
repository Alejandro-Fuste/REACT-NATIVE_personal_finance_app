import pandas

from server.custom_exceptions.input_not_string import InputNotString
from server.custom_exceptions.input_missing import InputMissing

from server.data_access_layer.implementation_classes.options_info_dao import OptionsInfoDAOImp
from server.service_layer.abstract_classes.options_info_service_abs import OptionsInfoService

input_must_be_string: str = "The input must be a string."
input_not_provided: str = "An input must be provided."


class OptionsInfoServiceImp(OptionsInfoService):
    def __init__(self, options_info_dao):
        self.options_info_dao: OptionsInfoDAOImp = options_info_dao

    def get_stock_price(self, ticker: str) -> float:
        # check ticker not blank
        if ticker is None:
            raise InputMissing(input_not_provided)

        # check ticker is a string
        if isinstance(ticker, str) is False:
            raise InputNotString(input_must_be_string)

        # check ticker not empty
        if len(ticker.strip()) == 0:
            raise InputMissing(input_not_provided)

        return self.options_info_dao.get_stock_price(ticker)

    def get_calls(self, ticker: str) -> pandas:
        # check ticker not blank
        if ticker is None:
            raise InputMissing(input_not_provided)

        # check ticker is a string
        if isinstance(ticker, str) is False:
            raise InputNotString(input_must_be_string)

        # check ticker not empty
        if len(ticker.strip()) == 0:
            raise InputMissing(input_not_provided)

        return self.options_info_dao.get_calls(ticker)

    def get_puts(self, ticker: str) -> pandas:
        # check ticker not blank
        if ticker is None:
            raise InputMissing(input_not_provided)

        # check ticker is a string
        if isinstance(ticker, str) is False:
            raise InputNotString(input_must_be_string)

        # check ticker not empty
        if len(ticker.strip()) == 0:
            raise InputMissing(input_not_provided)

        return self.options_info_dao.get_puts(ticker)

    def get_targeted_options(self, ticker: str, expiration_date: str) -> list:
        # check ticker not blank
        if ticker is None or expiration_date is None:
            raise InputMissing(input_not_provided)

        # check ticker is a string
        if isinstance(ticker, str) is False or isinstance(expiration_date, str) is False:
            raise InputNotString(input_must_be_string)

        # check ticker not empty
        if len(ticker.strip()) == 0 or len(expiration_date.strip()) == 0:
            raise InputMissing(input_not_provided)

        return self.options_info_dao.get_targeted_options(ticker, expiration_date)
