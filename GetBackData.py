#GetBackData.py
#Modifled 2018/5/24
import sys
sys.path.append('../module')

import CryptWatchModule
import DataModule
import TimeModule


DataDir = './tradedata'
filename = 'Before_20180524_000000'
CryWat = CryptWatchModule.CryptWatchModule()
DataMod = DataModule.DataModule(str(DataDir) + '/' + str(filename))

end_time = TimeModule.GetUtime_j(2018, 5, 24, 0, 0, 0)
start_time = end_time - 60*60

end_flag = False
count = 0
while(not end_flag):
    ohlc_list = CryWat.GetOHLC(end_time, start_time, 60)
    ohlc_list.reverse()

    if(len(ohlc_list) != 0):
        if(count != 0):
            del ohlc_list[0]
        DataMod.AddOHLC(ohlc_list)
        
        print(TimeModule.GetTime_j(end_time) + ' - ' + TimeModule.GetTime_j(start_time))
        print('remain :' + str(CryWat.remain), end=' ')
        print('cost :' + str(CryWat.cost))
        print()

        end_time = end_time - 60*60
        start_time = start_time - 60*60
        count = count + 1

        if(CryWat.remain < CryWat.cost*2):
            print("There is no remain")
            end_flag=True

    else:
        print("There are no mora datas")
        end_flag=True
        

    


