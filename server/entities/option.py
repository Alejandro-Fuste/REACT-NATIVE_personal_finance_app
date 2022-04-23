class Option:
    def __init__(self,
                 option_id: int = None,
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
                 straddle_put_breakeven_point: float = None
                 ):
        self.option_id = option_id
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
