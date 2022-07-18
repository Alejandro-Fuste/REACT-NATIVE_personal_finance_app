from server.entities.option import Option

test_call_option = Option("T", 19.00, 18.94, "5/6", 1, "straddle", .25, .38)
option = test_call_option.make_dictionary()


def test_create_option_id():
    option_id = option["tradeId"]
    assert isinstance(option_id, int)


def test_calculate_call_breakeven_amount():
    amount = option["callBreakevenAmount"]
    assert amount == 19.25


def test_calculate_call_breakeven_percent():
    amount = option["callBreakevenPercent"]
    assert amount == 1.64


def test_calculate_put_breakeven_amount():
    amount = option["putBreakevenAmount"]
    assert amount == 18.62


def test_calculate_put_breakeven_percent():
    amount = option["putBreakevenPercent"]
    assert amount == 1.69


def test_calculate_straddle_call_breakeven_amount():
    amount = option["straddleCallBreakevenAmount"]
    assert amount == 19.63


def test_calculate_straddle_call_breakeven_percent():
    amount = option["straddleCallBreakevenPercent"]
    assert amount == 3.64


def test_calculate_straddle_put_breakeven_amount():
    amount = option["straddlePutBreakevenAmount"]
    assert amount == 18.37


def test_calculate_straddle_put_breakeven_percent():
    amount = option["straddlePutBreakevenPercent"]
    assert amount == 3.01
