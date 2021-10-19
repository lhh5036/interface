'''
@File: test_queryCapitalCost
@time:2021/9/25
@Author:majiaqin 170479
@Desc:财务报表-查询资金支出日报表列表数据接口用例
'''

import unittest
import random

from apps.Fmis.fmis_interface_service.financial_manage.queryCapitalCost import QueryCapitalCost
from apps.utils.date_operate_util import getMonthFirstDay
from apps.utils.date_operate_util import getMonthLastDay

class Test_queryCapitalCost(unittest.TestCase):

    def queryCapitalCost(self):
        global lis
        lis = []
        # 获取当前月份的第一天和最后一天
        start_time = getMonthFirstDay()
        end_time = getMonthLastDay()
        lis.append(str(start_time) + "T16:00:00.000Z")
        lis.append(str(end_time) + "T16:00:00.000Z")
        costTypes_list = ['业务支出', '内部往来支出']
        costType = costTypes_list[random.randint(0, len(costTypes_list)-1)]
        lis.append(costType)
        return lis

    def testCase01(self):
        paramsList = self.queryCapitalCost()
        responseResult01 = QueryCapitalCost().querycapitalcost(paramsList)
        return responseResult01

if __name__ == '__main__':
    Test_queryCapitalCost().testCase01()