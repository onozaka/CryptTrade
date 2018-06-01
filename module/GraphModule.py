#GraphModule Modified 2018/5/25

from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

import TimeModule
import datetime

def MakeGraph(ohlc_list, directry):
    update_status = 'None'
    if(len(ohlc_list) > 0):
        
        Time, Open, High, Low, Close, Volume, Unknown = [], [], [], [], [], [], []
        for ohlc in ohlc_list:
            Time.append(ohlc[0])
            Open.append(ohlc[1])
            High.append(ohlc[2])
            Low.append(ohlc[3])
            Close.append(ohlc[4])
            Volume.append(ohlc[5])
            Unknown.append(ohlc[6])
            
        start_tm = datetime.datetime.strptime(TimeModule.GetTime_j(Time[0]), '%Y-%m-%d %H:%M:%S')
        end_tm = datetime.datetime.strptime(TimeModule.GetTime_j(Time[-1]), '%Y-%m-%d %H:%M:%S')

        filename = str(start_tm.year) + str(start_tm.month).zfill(2) + str(start_tm.day).zfill(2) + str(start_tm.hour).zfill(2) + str(start_tm.minute).zfill(2) + '_' + \
                   str(end_tm.year) + str(end_tm.month).zfill(2) + str(end_tm.day).zfill(2) + str(end_tm.hour).zfill(2) + str(end_tm.minute).zfill(2)
                
        Date = [start_tm + datetime.timedelta(minutes=mi) for mi in range(len(Time))]
        G_ohlc = zip(mdates.date2num(Date), Open, High, Low, Close)
        

        ax = plt.subplot()
        ax.xaxis.set_major_locator(mdates.MinuteLocator([0, 15, 30, 45]))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

        candlestick_ohlc(ax, G_ohlc, width=(1/24/60)*0.7, colorup='g', colordown='r')

        plt.title(filename + ' BTC/JPY ')

        plt.savefig(directry + '/' + filename + '.png')
        update_status = directry + '/' + filename + '.png'
        ax.clear()
        plt.close()
    else:
        update_status = 'None'
        
    return update_status
