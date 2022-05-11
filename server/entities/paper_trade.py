class PaperTrade:
    def __init__(self,
                 trade_id: int = None,
                 ticker: str = None,
                 strike_price: float = None,
                 expiration_date: str = None,
                 contracts: int = None,
                 strategy_type: str = None,
                 call_price: float = None,
                 put_price: float = None,
                 call_breakeven_amount: float = None,
                 put_breakeven_amount: float = None,
                 straddle_call_breakeven_amount: float = None,
                 straddle_put_breakeven_amount: float = None,
                 sell_price: float = None,
                 ):
        self.trade_id = trade_id
        self.ticker = ticker
        self.strike_price = strike_price
        self.expiration_date = expiration_date
        self.contracts = contracts
        self.strategy_type = strategy_type
        self.call_price = call_price
        self.put_price = put_price
        self.call_breakeven_amount = call_breakeven_amount
        self.put_breakeven_amount = put_breakeven_amount
        self.straddle_call_breakeven_amount = straddle_call_breakeven_amount
        self.straddle_put_breakeven_amount = straddle_put_breakeven_amount
        self.sell_price = sell_price

    # Calculate Cost Price
    def calculate_cost_price(self):
        amount = self.call_price + self.put_price
        return amount

    # Calculate Total Sell Amount ----------------------------------------------------------------
    def calculate_total_sell(self):
        contract_amount = self.contracts * 100
        amount = self.sell_price * contract_amount
        return amount

    # Calculate Total Cost Amount ----------------------------------------------------------------
    def calculate_total_cost(self):
        contract_amount = self.contracts * 100
        amount = self.calculate_cost_price() * contract_amount
        return amount

    # Calculate Net Profit Amount ----------------------------------------------------------------
    def calculate_net_profit(self):
        amount = self.calculate_total_sell() - self.calculate_total_cost()
        return amount

    # Calculate Net Profit Percentage ------------------------------------------------------------
    def calculate_net_profit_percentage(self):
        amount = (self.calculate_net_profit() / self.calculate_total_sell()) * 100
        return round(amount, 2)

    # Dictionary and str methods -----------------------------------------------------------------
    def make_dictionary(self):
        dictionary = {
            "tradeId": self.trade_id,
            "ticker": self.ticker,
            "strikePrice": self.strike_price,
            "expirationDate": self.expiration_date,
            "strategyType": self.strategy_type,
            "callPrice": self.call_price,
            "putPrice": self.put_price,
            "callBreakevenPoint": self.call_breakeven_amount,
            "putBreakevenPoint": self.put_breakeven_amount,
            "straddleCallBreakevenPoint": self.straddle_call_breakeven_amount,
            "straddlePutBreakevenPoint": self.straddle_put_breakeven_amount,
            "sellPrice": self.sell_price,
            "costPrice": self.calculate_cost_price(),
            "totalSell": self.calculate_total_sell(),
            "totalCost": self.calculate_total_cost(),
            "netProfit": self.calculate_net_profit(),
            "netProfitPercentage": self.calculate_net_profit_percentage()
        }

        return dictionary

    def __str__(self):
        return f"tradeId: {self.trade_id}, ticker: {self.ticker}, strike_price: {self.strike_price}, " \
               f"expiration_date: {self.expiration_date}, strategy_type: {self.strategy_type}, call_price: " \
               f"{self.call_price}, put_price: {self.put_price}, call_breakeven_point: {self.call_breakeven_amount}," \
               f"put_breakeven_point: {self.put_breakeven_amount}, straddle_call_breakeven_point: " \
               f"{self.straddle_call_breakeven_amount}, straddle_put_breakeven_point: " \
               f"{self.straddle_put_breakeven_amount}, sell_price: {self.sell_price}, cost_price: " \
               f"{self.calculate_cost_price()}, total_sell: {self.calculate_total_sell()}, total_cost: " \
               f"{self.calculate_total_cost()}, net_profit: {self.calculate_net_profit()}, net_profit_percentage: " \
               f"{self.calculate_net_profit_percentage()}"
