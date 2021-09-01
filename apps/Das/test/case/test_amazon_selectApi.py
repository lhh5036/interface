'''
@File: test_amazon_selectApi.py
@time:2021/8/19
@Author: quanliu 181324
@Desc:数据管理-我的数据Amazon查询接口用例
'''

import unittest

# 数据管理-我的数据Amazon查询接口用例类
class Test_amazonSelectApi(unittest.TestCase):

    def testCase01(self):
        testCaseReq_01 = {"country": "11US"}
        testCaseRep_01 = MyDataAmazonSelectApi().myDataAmazonSelect(testCaseReq_01)
        print(testCaseRep_01)

    def testCase02(self):
        testCaseReq_02 = {"country": "US","sellerName":"Gardenwed"}
        testCaseRep_02 = MyDataAmazonSelectApi().myDataAmazonSelect(testCaseReq_02)
        print(testCaseRep_02)











