#TimeModule Modified 2018/5/24

import calendar
import datetime

def GetUtime_j(Year, Mon, Day, Hour, Min, Sec):
    dt = datetime.datetime(Year, Mon, Day, Hour, Min, Sec)
    return calendar.timegm(dt.utctimetuple()) - 9*60*60

def GetUtime_u(Year, Mon, Day, Hour, Min, Sec):
    dt = datetime.datetime(Year, Mon, Day, Hour, Min, Sec)
    return calendar.timegm(dt.utctimetuple())

def GetTime_j(unixtime):
    dt = datetime.datetime.utcfromtimestamp(unixtime + 9*60*60)
    return str(dt)

def GetTime_u(unixtime):
    dt = datetime.datetime.utcfromtimestamp(unixtime)
    return str(dt)
