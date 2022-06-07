'''
@File: test_amazon_selectApi.py
@time:2021/8/19
@Author: quanliu 181324
@Desc:数据管理-我的数据Amazon查询接口用例
'''

import unittest
from apps.AllSystemData.DasSystem.das_api.myData_manage.dataManageProductListingApi import dataManageProductListingInfo

# 数据管理-我的数据Amazon查询接口用例类
class Test_amazonSelectApi(unittest.TestCase):

    def testCase01(self):
        '''第一个测试用例'''
        testCaseReq_01 = {"country": "IN","sellerName":"Gardenwed"}
        testCaseRep_01 = dataManageProductListingInfo("Amazon","amazon_queryListing",testCaseReq_01)
        print(testCaseRep_01)

    def testCase02(self):
        '''第二个测试用例'''
        testCaseReq_02 = {"country": "US"}
        testCaseRep_02 = dataManageProductListingInfo("Amazon","amazon_queryListing",testCaseReq_02)
        print(testCaseRep_02)











