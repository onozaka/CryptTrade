#GetBackData.py Modifled 2018/6/1
import sys
sys.path.append('./module')
import datetime
import time

import CryptWatchModule
import DataModule
import TimeModule
import GraphModule
import TwitterModule

#====Param====
DataDir = '../tradedata'
PicDir = '../pic'
dt_now = datetime.datetime.now()
filename = str(dt_now.year) + str(dt_now.month).zfill(2) + str(dt_now.day).zfill(2)
DataMod = DataModule.DataModule(DataDir, filename)
DataDay = int(dt_now.day)
DataMonth = dt_now.month
CryWat = CryptWatchModule.CryptWatchModule()
#sec
alpha = 10*60
#min
delta = 60
#resume_back[hour]
resume_back = 4
#sleep min
s_delta = 1
#========


#====Resume====
if(DataMod.Find_Flag):
    init_back = resume_back
else:
    init_back = 1
    
dt_now = datetime.datetime.now()
now_stamp = TimeModule.GetUtime_j(dt_now.year, dt_now.month, dt_now.day, dt_now.hour, 0, 0)
last_stamp = now_stamp - init_back*delta*60
ohlc_list = CryWat.GetOHLC(now_stamp, last_stamp, 60)
if(len(ohlc_list) != 0):
    DataMod.AddOHLC(ohlc_list)
    print(TimeModule.GetTime_j(last_stamp) + ' - ' + TimeModule.GetTime_j(now_stamp))
    print('remain :' + str(CryWat.remain), end=' ')
    print('cost :' + str(CryWat.cost))

    update_status = GraphModule.MakeGraph(ohlc_list, PicDir)
    if(update_status != 'None'):
        print(update_status)
        TwitterModule.TweetPic(update_status)
    else:
        print(update_status)
        
    print()
else:
    print('something wrong')

last_stamp = now_stamp    
#========

#====GetOHLC every hour====
while(True):
    dt_now = datetime.datetime.now()
    if((DataDay != int(dt_now.day)) and (dt_now.hour == 1)):
        del DataMod
        filename = str(dt_now.year) + str(dt_now.month).zfill(2) + str(dt_now.day).zfill(2)
        DataMod = DataModule.DataModule(DataDir, filename)
        DataDay = int(dt_now.day)
        
    now_stamp = TimeModule.GetUtime_j(dt_now.year, dt_now.month, dt_now.day, dt_now.hour, 0, 0)
    if(now_stamp - last_stamp >= delta*60 ):
        ohlc_list = CryWat.GetOHLC(now_stamp, last_stamp - alpha, 60)

        if(len(ohlc_list) != 0):
            DataMod.AddOHLC(ohlc_list)
            print(TimeModule.GetTime_j(last_stamp) + ' - ' + TimeModule.GetTime_j(now_stamp))
            print('remain :' + str(CryWat.remain), end=' ')
            print('cost :' + str(CryWat.cost))
            
            update_status = GraphModule.MakeGraph(ohlc_list, PicDir)
            if(update_status != 'None'):
                print(update_status)
                TwitterModule.TweetPic(update_status)
            else:
                print(update_status)
                        
            print()
        else:
            print('something wrong')
        
        last_stamp = now_stamp
        time.sleep(60*s_delta)
    else:
        time.sleep(60*s_delta)
        
#========
