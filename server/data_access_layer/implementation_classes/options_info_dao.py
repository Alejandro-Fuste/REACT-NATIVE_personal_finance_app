from pprint import pprint

from server.data_access_layer.abstract_classes.options_info_dao import OptionsInfoDAO
from server.environment_variables import api_key
import requests

# api connection info ----------------------------------------------
url = "https://yh-finance.p.rapidapi.com/stock/v2/get-options"
headers = {
    "X-RapidAPI-Host": "yh-finance.p.rapidapi.com",
    "X-RapidAPI-Key": api_key
}


class OptionsInfoImp(OptionsInfoDAO):

    def get_live_stock_price(self, ticker: str) -> float:
        pass

    def get_options(self, ticker: str) -> dict:
        querystring = {"symbol": ticker, "date": "1562284800", "region": "US"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()


new_opt = OptionsInfoImp()
one = new_opt.get_calls("t")
print(isinstance(one, dict))
print(len(one))
