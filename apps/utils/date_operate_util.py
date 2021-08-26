'''
@File: date_operate_util.py
@time:2021/8/26
@Author:quanliu
@Desc:日期工具类
'''
import datetime
from pandas import *
from dateutil.relativedelta import relativedelta

class DateUtils():
    # 获取当前时间
    def getCurrentTimeFormate(self,dateFormate):
        return datetime.datetime.now().strftime(dateFormate)  # 2021-08-26 17:14:32

    # 获取当前年月日
    def getCurrentDateFormate(self):
        return datetime.datetime.now().strftime('%Y-%m-%d')  # 2021-08-26

    # 当前时间往前往后推几天
    def getTheDate(self,num,dateFormate):
        dt = datetime.datetime.now()
        dt_date = (dt + self.num * tseries.offsets.Day()).strftime(dateFormate)
        return dt_date

    # 当前时间往前往后推几个月
    def getTheMonth(self,num,dateFormate): # +1---往前推1个月  -1---往后推1个月
        dt = datetime.date.today()
        dt_date = (dt - relativedelta(months=num)).strftime(dateFormate) # "%Y-%m"---年月
        return dt_date

    # 获取当前时间是星期几
    def getTheWeek(self,date): # 1-7对应周一到周末
        weekFormate = datetime.datetime.strptime(date, "%Y-%m-%d").weekday() + 1
        if weekFormate == 1:
            return "Monday"
        elif weekFormate == 2:
            return "Tuesday"
        elif weekFormate == 3:
            return "Wednesday"
        elif weekFormate == 4:
            return "Thursday"
        elif weekFormate == 5:
            return "Friday"
        elif weekFormate == 6:
            return "Saturday"
        elif weekFormate == 7:
            return "Sunday"


