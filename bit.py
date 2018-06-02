#bit.py
import sys
sys.path.append('./module')

import bitFlyerModule
####

def p_list(item):
    for i in range(len(item)):
        print(item[i])

####

bitAPI = bitFlyerModule.bitFlyerModule()

'''
p_list(bitAPI.getmarkets())
print(bitAPI.gethealth())
print(bitAPI.getboard())
print(bitAPI.execution(100))
print(bitAPI.getticker())
print('bids')
p_list(bitAPI.getboard()['bids'])
print('asks')
p_list(bitAPI.getboard()['asks'])
'''
print('mid_price')
print(bitAPI.getboard()['mid_price'])
print(bitAPI.getticker()['ltp'])
