import pandas

from server.custom_exceptions.input_not_string import InputNotString
from server.custom_exceptions.input_missing import InputMissing
from server.custom_exceptions.input_not_int import InputNotInteger
from server.custom_exceptions.input_not_float import InputNotFloat

from server.data_access_layer.implementation_classes.options_info_dao import OptionsInfoDAOImp
from server.entities.option import Option
from server.service_layer.abstract_classes.options_info_service_abs import OptionsInfoService

input_must_be_string: str = "The input must be a string."
input_not_provided: str = "An input must be provided."
input_not_integer: str = "The input must be a integer."
input_not_float: str = "The input must be a float."


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

    def get_option_info(self, data: dict) -> Option:
        # check properties are strings
        if isinstance(data["ticker"], str) is False \
                or isinstance(data["expirationDate"], str) is False \
                or isinstance(data["strategyType"], str) is False:
            raise InputNotString(input_must_be_string)

        # check if property is not empty
        if data["ticker"] is None or len(data["ticker"].strip()) == 0 \
                or data["strikePrice"] is None \
                or data["stockPrice"] is None \
                or data["expirationDate"] is None or len(data["expirationDate"].strip()) == 0 \
                or data["strategyType"] is None or len(data["strategyType"].strip()) == 0 \
                or data["contracts"] is None \
                or data["callPrice"] is None \
                or data["putPrice"] is None:
            raise InputMissing(input_not_provided)

        # check if value is a float
        if isinstance(data["strikePrice"], float) is False \
                or isinstance(data["stockPrice"], float) is False \
                or isinstance(data["callPrice"], float) is False \
                or isinstance(data["putPrice"], float) is False:
            raise InputNotFloat(input_not_float)

        if isinstance(data["contracts"], int) is False:
            raise InputNotInteger(input_not_integer)

        return self.options_info_dao.get_option_info(data)
