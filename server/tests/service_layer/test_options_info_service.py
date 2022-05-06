from server.custom_exceptions.input_not_string import InputNotString
from server.custom_exceptions.input_missing import InputMissing

from server.data_access_layer.implementation_classes.options_info_dao import OptionsInfoDAO, OptionsInfoImp
from server.service_layer.implementation_classes.options_info_service import OptionsInfoService, OptionsInfoServiceImp

options_info_dao: OptionsInfoDAO = OptionsInfoImp()
options_info_service: OptionsInfoService = OptionsInfoServiceImp(options_info_dao)

input_must_be_string: str = "The input must be a string."
input_not_provided: str = "An input must be provided."


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
        options_info_service.(int_ticker)
        assert False
    except InputNotString as e:
        assert str(e) == input_must_be_string


def test_get_targeted_options_ticker_empty_string(empty_string):
    try:
        options_info_service.(empty_string)
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


def test_get_targeted_options_ticker_blank(none_ticker):
    try:
        options_info_service.(none_ticker)
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided
