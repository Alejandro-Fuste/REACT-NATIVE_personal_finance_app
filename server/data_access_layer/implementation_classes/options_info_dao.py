from server.data_access_layer.abstract_classes.options_info_dao import OptionsInfoDAO
from server.custom_exceptions.option_not_found import OptionNotFound
from server.entities.option import Option

from yahoo_fin import options
from yahoo_fin import stock_info

import pandas

stock_not_found = "Your stock was not able to be located."


class OptionsInfoImp(OptionsInfoDAO):

    # Get stock price -------------------------------------------------------------
    def get_stock_price(self, ticker: str) -> float:
        try:
            price = stock_info.get_live_price(ticker)
            return round(price, 2)
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

    def get_targeted_options(self, ticker: str, expiration_date: str) -> list:
        stock_price = self.get_stock_price(ticker)

        if stock_price == 'No data found, symbol may be delisted':
            raise OptionNotFound(stock_not_found)

        bottom_limit = round(stock_price - 1, 2)
        top_limit = round(stock_price + 1, 2)

        opt_dict = options.get_options_chain(ticker)

        if len(opt_dict["puts"]) == 0:
            raise OptionNotFound(stock_not_found)

        strike_array = []
        array = []

        calls_df = opt_dict["calls"]
        puts_df = opt_dict["puts"]

        for i in range(len(calls_df)):
            if bottom_limit <= calls_df.loc[i, "Strike"] <= top_limit:
                strike_array.append(calls_df.loc[i, "Strike"])

        for i in strike_array:
            call = calls_df.loc[calls_df["Strike"] == i]
            put = puts_df.loc[puts_df["Strike"] == i]
            new_option = Option(ticker, float(call["Strike"].values[0]), float(stock_price), expiration_date,
                                "Straddle", float(call["Ask"].values[0]), float(put["Ask"].values[0]))
            array.append(new_option.make_dictionary())

        return array


