'''
@File: test_queryCapitalContrast
@time:2021/9/25
@Author:majiaqin 170479
@Desc:财务报表-查询资金对比日报表列表数据接口用例
'''

import unittest

from apps.AllSystemData.FmisSystem.fmis_interface_service.financial_manage.queryCapitalContrast import \
    QueryCapitalContrast
from apps.utils.date_operate_util import getMonthFirstDay
from apps.utils.date_operate_util import getMonthLastDay

class Test_queryCapitalContrast(unittest.TestCase):

    def queryCapitalContrast(self):
        global lis
        lis = []
        # 获取当前月份的第一天和最后一天
        start_time = getMonthFirstDay()
        end_time = getMonthLastDay()
        lis.append(str(start_time) + "T16:00:00.000Z")
        lis.append(str(end_time) + "T16:00:00.000Z")
        return lis

    def testCase01(self):
        paramsList = self.queryCapitalContrast()
        responseResult01 = QueryCapitalContrast().querycapitalcontrast(paramsList)
        return responseResult01

if __name__ == '__main__':
    Test_queryCapitalContrast().testCase01()
    pass