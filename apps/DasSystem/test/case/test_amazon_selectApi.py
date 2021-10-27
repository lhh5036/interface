'''
@File: test_amazon_selectApi.py
@time:2021/8/19
@Author: quanliu 181324
@Desc:数据管理-我的数据Amazon查询接口用例
'''

import unittest
from apps.DasSystem.das_interface_service.myData_manage.dataManageProductListingApi import DataManageProductListingApi

# 数据管理-我的数据Amazon查询接口用例类
class Test_amazonSelectApi(unittest.TestCase):

    def testCase01(self):
        '''第一个测试用例'''
        testCaseReq_01 = {"country": "11US"}
        testCaseRep_01 = DataManageProductListingApi().dataManageProductListingInfo("Amazon","amazon_queryListing",testCaseReq_01)
        print(testCaseRep_01)

    def testCase02(self):
        '''第二个测试用例'''
        testCaseReq_02 = {"country": "US","sellerName":"Gardenwed"}
        testCaseRep_02 = DataManageProductListingApi().dataManageProductListingInfo("Amazon","amazon_queryListing",testCaseReq_02)
        print(testCaseRep_02)











