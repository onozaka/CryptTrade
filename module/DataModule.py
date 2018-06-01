#DataModule Modified 2018/5/24

import pandas as pd
pd.set_option('display.width', 100)
import glob
import csv

class DataModule:
    Columns = ["UnixTime", "OpenPrice", "HighPrice", "LowPrice", "ClosePrice", "Volume", "Unknown"]
    
    def __init__(self, directry, name):
        self.FileName = str(directry) + '/' + str(name) + '.csv'
        self.LastTime = 0
        self.Data = pd.DataFrame([], columns = DataModule.Columns)
        self.Find_Flag = False
        
        CSVfilelist = glob.glob(str(directry) + '/*.csv')
        if(self.FileName in CSVfilelist):
            self.Find_Flag = True
        else:
            self.Find_Flag = False
                     
        if(self.Find_Flag == False):
            self.Data.to_csv(self.FileName, mode='w', index=False)
        else:
            csv_f = open(self.FileName, 'r')
            read_data = csv.reader(csv_f)
            for line in read_data:
                time = line[0]
            
            self.LastTime = int(time)
            print('Start From :' + str(self.LastTime) + ' [UnixTime]')
            del csv_f
            del read_data

    def __del__(self):
        return 0
        
    def AddOHLC(self, ohlc_list):
        N = len(ohlc_list)
        add_index = -1
        for i in range(N):
            Time = ohlc_list[i][0]
            if(Time == self.LastTime):
                add_index = i
        if(add_index > -1):
            for i in range(add_index+1):
                del ohlc_list[0]
                
        if(len(ohlc_list) > 0):
            self.Data = pd.DataFrame(ohlc_list, columns = DataModule.Columns)
            #self.Data.to_csv(self.FileName, mode='a', index=False)
            self.Data.to_csv(self.FileName, mode='a', index=False, header=False)
            self.LastTime = ohlc_list[-1][0]
