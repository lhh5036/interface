'''
@File: date_operate_util.py
@time:2021/8/26
@Author:quanliu
@Desc:日期工具类
'''
import calendar
from pandas import *
import datetime
from dateutil.relativedelta import relativedelta

class DateUtils():
    # 获取当前时间
    def getCurrentTimeFormate(self, dateFormate):
        self.dateFormate = dateFormate

        return datetime.datetime.now().strftime(self.dateFormate)  # 2021-08-26 17:14:32

    # 获取当前年月日
    def getCurrentDateFormate(self, dateFormate):
        self.dateFormate = dateFormate

        return datetime.datetime.now().strftime(self.dateFormate)  # 2021-08-26

    # 当前时间往前往后推几天
    def getTheDate(self, num, dateFormate):
        self.num = num
        self.dateFormate = dateFormate

        dt = datetime.datetime.now()
        dt_date = (dt + self.num * tseries.offsets.Day()).strftime(self.dateFormate)
        return dt_date

    # 当前时间往前往后推几个月
    def getTheMonth(self, num, dateFormate): # +1---往前推1个月  -1---往后推1个月
        self.num = num
        self.dateFormate = dateFormate

        dt = datetime.date.today()
        dt_date = (dt - relativedelta(months=self.num)).strftime(self.dateFormate) # "%Y-%m"---年月
        return dt_date

    # 获取当前时间是星期几
    def getTheWeek(self, date): # 1-7对应周一到周末
        self.date = date

        weekFormate = datetime.datetime.strptime(self.date, "%Y-%m-%d").weekday() + 1
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

# 获取某月份的第一天
def getMonthFirstDay(year=None, month=None):

    '''year&month默认本年本月 例:year=2021 month=9'''
    if year:
        year = int(year)
    else:
        year = datetime.date.today().year

    if month:
        month = int(month)
    else:
        month = datetime.date.today().month

    # 获取当月第一天的星期和当月的总天数
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)
    first_day = datetime.date(year=year, month=month, day=1)
    return first_day

# 获取某月份的最后一天
def getMonthLastDay(year=None, month=None):

    '''year&month默认本年本月 例:year=2021 month=9'''
    if year:
        year = int(year)
    else:
        year = datetime.date.today().year

    if month:
        month = int(month)
    else:
        month = datetime.date.today().month

    # 获取当月第一天的星期和当月的总天数
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)
    last_day = datetime.date(year=year, month=month, day=monthRange)
    return last_day

if __name__ == '__main__':
    s = getMonthLastDay(2019, 6)
    print(s)