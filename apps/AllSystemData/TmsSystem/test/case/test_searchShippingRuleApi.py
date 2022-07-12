'''
@File: test_searchShippingRuleApi.py
@time:2022/7/12
@Author:quanliu 181324
@Desc:物流规则-查询
'''
import unittest
from apps.AllSystemData.TmsSystem.tms_api.logisticsPlanning.searchShippingRuleApi import searchShippingRuleApi


class Test_searchShippingRuleApi(unittest.TestCase):
    def testCase01(self):
        '''物流规则-物流自定义规则-查询(无参)'''
        responseResult01 = searchShippingRuleApi({})
        print(responseResult01)

    def testCase02(self):
        '''物流规则-物流自定义规则-查询(有参)'''
        responseResult02 = searchShippingRuleApi({"statusList":["10"]})
        print(responseResult02)

if __name__ == '__main__':
    unittest.main()