# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_queryCapitalIncome
@time:2021/9/23
@Author:majiaqin 170479
@Desc:财务报表-查询资金收入日报表列表数据接口用例
'''

import unittest
import random
import pprint

from apps.FmisSystem.fmis_interface_service.fmisSystem_comConfig import Fmis_Common_Config
from apps.FmisSystem.fmis_interface_service.financial_manage.queryCapitalIncome import QueryCapitalIncome
from apps.utils.mySql_database_util import Mysql_handleOperator
from apps.utils.date_operate_util import getMonthFirstDay
from apps.utils.date_operate_util import getMonthLastDay

class Test_queryCapitalIncome(unittest.TestCase):

    def queryCapitalIncome(self):
        global lis
        lis = []
        # 获取当前月份的第一天和最后一天
        start_time = getMonthFirstDay()
        end_time = getMonthLastDay()
        lis.append(str(start_time)+"T16:00:00.000Z")
        lis.append(str(end_time)+"T16:00:00.000Z")
        incomeTypes_list = ['业务收入', '内部往来收入']
        incomeType = incomeTypes_list[random.randint(0, len(incomeTypes_list)-1)]
        lis.append(incomeType)
        return lis

    def testCase01(self):
        paramsList = self.queryCapitalIncome()
        responseResult01 = QueryCapitalIncome().querycapitalincome(paramsList)
        return responseResult01


if __name__ == '__main__':
    Test_queryCapitalIncome().testCase01()
    pass