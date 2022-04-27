import random
from pprint import pprint


class Option:
    def __init__(self,
                 ticker: str = None,
                 strike_price: float = None,
                 stock_price: float = None,
                 trade_type: str = None,
                 expiration_date: str = None,
                 strategy_type: str = None,
                 call_price: float = None,
                 put_price: float = None,
                 ):
        self.ticker = ticker
        self.strike_price = strike_price
        self.stock_price = stock_price
        self.trade_type = trade_type
        self.expiration_date = expiration_date
        self.strategy_type = strategy_type
        self.call_price = call_price
        self.put_price = put_price

    @staticmethod
    def create_option_id():
        new_id = round(random.uniform(1, 1000000))
        return new_id

    # Calculate Call Option ----------------------------------------------------------------------

    def calculate_call_breakeven_amount(self):
        amount = round(self.strike_price + self.call_price, 2)
        return amount

    def calculate_call_breakeven_percent(self):
        pass

    # Calculate Put Option ----------------------------------------------------------------------

    def calculate_put_breakeven_amount(self):
        amount = round(self.strike_price - self.put_price, 2)
        return amount

    def calculate_put_breakeven_percent(self):
        pass

    # Calculate Call Straddle -------------------------------------------------------------------

    def calculate_straddle_call_breakeven_amount(self):
        pass

    def calculate_straddle_call_breakeven_percent(self):
        pass

    def calculate_straddle_put_breakeven_amount(self):
        pass

    def calculate_straddle_put_breakeven_percent(self):
        pass

    # Dictionary and str methods -----------------------------------------------------------------
    def make_dictionary(self):
        dictionary = {
            "optionId": self.create_option_id(),
            "ticker": self.ticker,
            "strikePrice": self.strike_price,
            "stockPrice": self.stock_price,
            "tradeType": self.trade_type,
            "expirationDate": self.expiration_date,
            "strategyType": self.strategy_type,
            "callPrice": self.call_price,
            "putPrice": self.put_price,
            "callBreakevenAmount": self.calculate_call_breakeven_amount(),
            "putBreakevenAmount": self.calculate_put_breakeven_amount()
        }
        return dictionary

    def __str__(self):
        return f"option_id: {self.create_option_id()} ticker: {self.ticker}, strike_price: {self.strike_price}, " \
               f"stock_price: {self.stock_price}, trade_type: {self.trade_type}, " \
               f"expiration_date: {self.expiration_date}, strategy_type: {self.strategy_type}, " \
               f"call_price: {self.call_price}, put_price: {self.put_price}, " \
               f"call_breakeven_amount: {self.calculate_call_breakeven_amount()}"


a = Option("T", 20.00, 21.37, "call", "4/30", "straddle", .37, .14)
pprint(a.make_dictionary())
