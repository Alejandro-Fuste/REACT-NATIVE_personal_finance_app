class PaperTrade:
    def __init__(self,
                 trade_id: int = None,
                 contracts: int = None,
                 call_price: float = None,
                 put_price: float = None,
                 sell_price: float = None,
                 ):
        self.trade_id = trade_id
        self.contracts = contracts
        self.call_price = call_price
        self.put_price = put_price
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
            "contracts": self.contracts,
            "callPrice": self.call_price,
            "putPrice": self.put_price,
            "sellPrice": self.sell_price,
            "costPrice": self.calculate_cost_price(),
            "totalSell": self.calculate_total_sell(),
            "totalCost": self.calculate_total_cost(),
            "netProfit": self.calculate_net_profit(),
            "netProfitPercentage": self.calculate_net_profit_percentage(),
            "status": "closed"
        }

        return dictionary

    def __str__(self):
        return f"tradeId: {self.trade_id}, contracts: {self.contracts}, call_price: {self.call_price}, " \
               f"put_price: {self.put_price}, sell_price: {self.sell_price}, cost_price: " \
               f"{self.calculate_cost_price()}, total_sell: {self.calculate_total_sell()}, total_cost: " \
               f"{self.calculate_total_cost()}, net_profit: {self.calculate_net_profit()}, net_profit_percentage: " \
               f"{self.calculate_net_profit_percentage()}, status: closed"
