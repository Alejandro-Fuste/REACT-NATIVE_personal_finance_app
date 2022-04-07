class PaperTrade:
    def __init__(self,
                 trade_id: int = None,
                 ticker: str = None,
                 strike_price: float = None,
                 trade_type: str = None,
                 expiration_date: str = None,
                 strategy_type: str = None,
                 call_price: float = None,
                 put_price: float = None,
                 call_breakeven_point: float = None,
                 put_breakeven_point: float = None,
                 straddle_call_breakeven_point: float = None,
                 straddle_put_breakeven_point: float = None,
                 sell_price: float = None,
                 cost_price: float = None,
                 total_sell: float = None,
                 total_cost: float = None,
                 net_profit: float = None,
                 net_profit_percentage: int = None
                 ):
        self.trade_id = trade_id
        self.ticker = ticker
        self.strike_price = strike_price
        self.trade_type = trade_type
        self.expiration_date = expiration_date
        self.strategy_type = strategy_type
        self.call_price = call_price
        self.put_price = put_price
        self.call_breakeven_point = call_breakeven_point
        self.put_breakeven_point = put_breakeven_point
        self.straddle_call_breakeven_point = straddle_call_breakeven_point
        self.straddle_put_breakeven_point = straddle_put_breakeven_point
        self.sell_price = sell_price
        self.cost_price = cost_price
        self.total_sell = total_sell
        self.total_cost = total_cost
        self.net_profit = net_profit
        self.net_profit_percentage = net_profit_percentage

    def make_dictionary(self):
        dictionary = {
            "tradeId": self.trade_id,
            "ticker": self.ticker,
            "strikePrice": self.strike_price,
            "tradeType": self.trade_type,
            "expirationDate": self.expiration_date,
            "strategyType": self.strategy_type,
            "callPrice": self.call_price,
            "putPrice": self.put_price,
            "callBreakevenPoint": self.call_breakeven_point,
            "putBreakevenPoint": self.put_breakeven_point,
            "straddle_call_breakeven_point": self.straddle_call_breakeven_point,
            "straddle_put_breakeven_point": self.straddle_put_breakeven_point,
            "sellPrice": self.sell_price,
            "costPrice": self.cost_price,
            "totalSell": self.total_sell,
            "totalCost": self.total_cost,
            "netProfit": self.net_profit,
            "netProfitPercentage": self.net_profit_percentage
        }

        return dictionary

    def __str__(self):
        return f"tradeId: {self.trade_id}, ticker: {self.ticker}, strike_price: {self.strike_price}, " \
               f"trade_type: {self.trade_type}, expiration_date: {self.expiration_date}, " \
               f"strategy_type: {self.strategy_type}, call_price: {self.call_price}, put_price: {self.put_price}, " \
               f"call_breakeven_point: {self.call_breakeven_point}, put_breakeven_point: {self.put_breakeven_point}, " \
               f"straddle_call_breakeven_point: {self.straddle_call_breakeven_point}, " \
               f"straddle_put_breakeven_point: {self.straddle_put_breakeven_point} sell_price: {self.sell_price}, " \
               f"cost_price: {self.cost_price}, total_sell: {self.total_sell}, " \
               f"total_cost: {self.total_cost}, net_profit: {self.net_profit}, " \
               f"net_profit_percentage: {self.net_profit_percentage}"
