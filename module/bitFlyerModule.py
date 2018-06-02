#bitFlyerModule
import requests
import json

class bitFlyerModule:
    def __init__(self):
        self.param1 = 0
        self.param2 = 0

    def __Request(self, url):
        end_p = 'https://api.bitflyer.jp/v1/'
        result = requests.get(end_p + url).json()
        return result

    def __Request_o(self, url, option):
        end_p = 'https://api.bitflyer.jp/v1/'
        result = requests.get(end_p + url, params=option).json()
        return result

    def getmarkets(self):
        return self.__Request('getmarkets')
    
    def gethealth(self):
        return self.__Request('gethealth')
    
    def execution(self, count, before, after):
        option = {'count':count, 'before':before, 'after':after, 'product_code':'BTC_JPY'}
        return self.__Request_o('execution', option)
    
    def getboard(self):
        return self.__Request('getboard')

    def getticker(self):
        option = {'product_code':'BTC_JPY'}
        return self.__Request_o('getticker', option)
