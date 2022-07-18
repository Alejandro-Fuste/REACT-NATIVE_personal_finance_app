from server.entities.paper_trade import PaperTrade

test_paper_trade = PaperTrade(631428, 1, .49, .13, 1.01)
paper_trade = test_paper_trade.make_dictionary()


def test_calculate_cost_price():
    amount = paper_trade["costPrice"]
    assert amount == .62


def test_calculate_total_sell():
    amount = paper_trade['totalSell']
    assert amount == 101


def test_calculate_total_cost():
    amount = paper_trade['totalCost']
    assert amount == 62


def test_calculate_net_profit():
    amount = paper_trade['netProfit']
    assert amount == 39


def test_calculate_net_profit_percentage():
    percentage = paper_trade['netProfitPercentage']
    assert percentage == 38.61

