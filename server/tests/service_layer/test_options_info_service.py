from server.custom_exceptions.input_not_string import InputNotString
from server.custom_exceptions.input_missing import InputMissing
from server.custom_exceptions.input_not_int import InputNotInteger
from server.custom_exceptions.input_not_float import InputNotFloat

from server.data_access_layer.implementation_classes.options_info_dao import OptionsInfoDAO, OptionsInfoDAOImp
from server.service_layer.implementation_classes.options_info_service import OptionsInfoService, OptionsInfoServiceImp

options_info_dao: OptionsInfoDAO = OptionsInfoDAOImp()
options_info_service: OptionsInfoService = OptionsInfoServiceImp(options_info_dao)

input_must_be_string: str = "The input must be a string."
input_not_provided: str = "An input must be provided."
input_not_integer: str = "The input must be a integer."
input_not_float: str = "The input must be a float."


# Read Tests --------------------------------------------------------------------------------
# Get Stock Price Tests ---------------------------------------------------------------------
def test_get_stock_price_ticker_not_string(int_ticker):
    try:
        options_info_service.get_stock_price(int_ticker)
        assert False
    except InputNotString as e:
        assert str(e) == input_must_be_string


def test_get_stock_price_ticker_empty_string(empty_string):
    try:
        options_info_service.get_stock_price(empty_string)
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


def test_get_stock_price_ticker_blank(none_ticker):
    try:
        options_info_service.get_stock_price(none_ticker)
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


# Get Calls Tests ---------------------------------------------------------------------
def test_get_calls_ticker_not_string(int_ticker):
    try:
        options_info_service.get_calls(int_ticker)
        assert False
    except InputNotString as e:
        assert str(e) == input_must_be_string


def test_get_calls_ticker_empty_string(empty_string):
    try:
        options_info_service.get_calls(empty_string)
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


def test_get_calls_ticker_blank(none_ticker):
    try:
        options_info_service.get_calls(none_ticker)
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


# Get Puts Tests ---------------------------------------------------------------------
def test_get_puts_ticker_not_string(int_ticker):
    try:
        options_info_service.get_puts(int_ticker)
        assert False
    except InputNotString as e:
        assert str(e) == input_must_be_string


def test_get_puts_ticker_empty_string(empty_string):
    try:
        options_info_service.get_puts(empty_string)
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


def test_get_puts_ticker_blank(none_ticker):
    try:
        options_info_service.get_puts(none_ticker)
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


# Get Targeted Options Tests ---------------------------------------------------------------------
def test_get_targeted_options_ticker_not_string(int_ticker):
    try:
        options_info_service.get_targeted_options(int_ticker, "5/6")
        assert False
    except InputNotString as e:
        assert str(e) == input_must_be_string


def test_get_targeted_options_ticker_empty_string(empty_string):
    try:
        options_info_service.get_targeted_options(empty_string, "5/6")
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


def test_get_targeted_options_ticker_blank(none_ticker):
    try:
        options_info_service.get_targeted_options(none_ticker, "5/6")
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


def test_get_targeted_options_expiration_not_string(int_ticker):
    try:
        options_info_service.get_targeted_options("t", int_ticker)
        assert False
    except InputNotString as e:
        assert str(e) == input_must_be_string


def test_get_targeted_options_expiration_empty_string(empty_string):
    try:
        options_info_service.get_targeted_options("t", empty_string)
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


def test_get_targeted_options_expiration_blank(none_ticker):
    try:
        options_info_service.get_targeted_options("t", none_ticker)
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


# Get Option Info Tests -------------------------------------------------------------------------
# not string
def test_get_option_info_ticker_not_string():
    try:
        pass
    except InputNotString as e:
        assert str(e) == input_must_be_string


# missing
def test_get_option_info_missing_exp_date():
    try:
        pass
    except InputMissing as e:
        assert str(e) == input_not_provided


# not float
def test_get_option_info_stock_price_not_float():
    try:
        pass
    except InputNotFloat as e:
        assert str(e) == input_not_float


# not int
def test_get_option_info_contract_not_int():
    try:
        pass
    except InputNotInteger as e:
        assert str(e) == input_not_integer
