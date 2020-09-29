# import modules
import requests
import json

# import files
from config import client_id


class Info:
    def __init__(self, symbol):
        self.symbol = symbol

    # show 'symbol', 'current_price', previous_price'
    # def __str__(self):
    #     return str({
    #         'symbol': self.symbol,
    #         'current_price': self.get_current_price(),
    #         'previous_price': self.get_previous_price()
    #     })

    def show_symbol(self, symbol):
        print(symbol)

    # get current hour close price
    def get_current_price(self, symbol):
        # define our endpoint
        endpoint = rf"https://api.tdameritrade.com/v1/marketdata/{symbol}/quotes"

        # define our payload
        payload = {
            'apikey': client_id,
            'symbol': symbol
            # CANNOT have space after comma! else cannot loop through every 'symbol'
        }

        # make a request of 'quotes'
        response = requests.get(
            url=endpoint,
            params=payload
        )

        # convert it to a dictionary
        quotes_result = response.json()
        # to get all result --> json.dumps(response.json(), indent=4)

        # Return closePrice of a company
        closePrice = quotes_result[symbol]['regularMarketLastPrice']
        return closePrice

    # get previous hour close price
    def get_previous_price(self, symbol):
        # define our endpoint
        endpoint = rf"https://api.tdameritrade.com/v1/marketdata/{symbol}/pricehistory"

        # define our payload
        payload = {
            'apikey': client_id,
            'period': '2',
            'periodType': 'day',
            'frequency': '30',
            'frequencyType': 'minute',
            'needExtendedHoursData': 'true'
        }

        # make a request of 'price_history'
        response = requests.get(
            url=endpoint,
            params=payload
        )

        # convert it to a string dictionary
        result = json.dumps(response.json(), indent=4)  # response.json()

        # convert it to a dictionary
        dictionary = json.loads(result)
        return dictionary['candles'][-1]['close']

        # Available Period
        # day: 1, 2, 3, 4, 5, 10*
        # month: 1*, 2, 3, 6
        # year: 1*, 2, 3, 5, 10, 15, 20
        # ytd: 1*

        # Available Frequency
        # minute: 1*, 5, 10, 15, 30
        # daily: 1*
        # weekly: 1*
        # monthly: 1*

        # defaults marked with an asterisk

    # get current 200MA
    def get_current_200MA(self, symbol):
        pass

    # get previous week 200MA
    def get_previous_200MA(self, symbol):
        pass

    # get current 50MA
    def get_current_50MA(self, symbol):
        pass

    # get previous week 50MA
    def get_previous_50MA(self, symbol):
        pass

    # get 5MA
    def get_5MA(self, symbol):
        pass

    # get 10MA
    def get_10MA(self, symbol):
        pass
