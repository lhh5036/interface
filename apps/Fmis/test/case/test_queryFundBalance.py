'''
@File: test_queryFundBalance
@time:2021/9/25
@Author:majiaqin 170479
@Desc:财务报表-查询资金余额日报表列表数据接口用例
'''

import unittest
import random
import pprint

from apps.Fmis.fmis_interface_service.financial_manage.queryFundBalance import QueryFundBalance
from apps.utils.date_operate_util import getMonthFirstDay
from apps.utils.date_operate_util import getMonthLastDay

class Test_queryFundBalance(unittest.TestCase):

    def queryFundBalance(self):
        global lis
        lis = []
        # 获取当前月份的第一天和最后一天
        start_time = getMonthFirstDay()
        end_time = getMonthLastDay()
        lis.append(str(start_time) + "T16:00:00.000Z")
        lis.append(str(end_time) + "T16:00:00.000Z")
        lis.append(str(start_time) + "T16:00:00.000Z")
        lis.append(str(end_time) + "T16:00:00.000Z")
        return lis

    # 根据日期查询资金余额日报表列表数据
    def testCase01(self):
        paramsList01 = self.queryFundBalance()
        keyList01 = ["startDate", "endDate"]
        responseResult01 = QueryFundBalance().queryfundbalance(keyList01, paramsList01)
        return responseResult01

    # 根据修改时间查询资金余额日报表列表数据
    def testCase02(self):
        paramsList02 = self.queryFundBalance()
        keyList02 = ["startModifyTime", "endModifyTime"]
        responseResult02 = QueryFundBalance().queryfundbalance(keyList02, paramsList02)
        return responseResult02

    # 根据日期和修改时间查询资金余额日报表列表数据
    def testCase03(self):
        paramsList03 = self.queryFundBalance()
        keyList03 = ["startDate", "endDate", "startModifyTime", "endModifyTime"]
        responseResult03 = QueryFundBalance().queryfundbalance(keyList03, paramsList03)
        return responseResult03


if __name__ == '__main__':
    Test_queryFundBalance().testCase01()
    Test_queryFundBalance().testCase02()
    Test_queryFundBalance().testCase03()
    pass