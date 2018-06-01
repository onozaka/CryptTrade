#CryptWatchModule Modified 2018/5/24

import requests
import json

class CryptWatchModule:
    def __init__(self):
        self.remain = 0
        self.cost = 0

    def __Request(self, url):
        r_dict = requests.get(url).json()
        result = r_dict["result"]
        self.remain = r_dict["allowance"]["remaining"]
        self.cost = r_dict["allowance"]["cost"]
        return result

    def __Request_o(self, url, option):
        r_dict = requests.get(url, params=option).json()
        result = r_dict["result"]
        self.remain = r_dict["allowance"]["remaining"]
        self.cost = r_dict["allowance"]["cost"]
        return result
        
    def GetPrice(self):
        result = self.__Request('https://api.cryptowat.ch/markets/bitflyer/btcjpy/price')
        price = result["price"]
        print(price)
        return price

    def GetOHLC(self, end, start, periods):
        option = {'before':end, 'after':start, 'periods':periods}
        result = self.__Request_o('https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc', option)
        if(result[str(periods)] is None):
            return []
        else:
            return result[str(periods)]
