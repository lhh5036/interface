'''
@File: test_amazon_selectInterface.py
@time:2021/8/19
@Author: quanliu 181324
@Desc:数据管理-我的数据Amazon查询接口用例
'''

from apps.Das.das_interface_service.myData_manage.amazonSelectInterface import MyDataAmazonSelectInterface
import unittest

# 数据管理-我的数据Amazon查询接口用例类
class Test_amazonSelectInterface(unittest.TestCase):

    def test01(self):
        testCaseReq_01 = {"country": "11US"}
        testCaseRep_01 = MyDataAmazonSelectInterface().myDataAmazonSelect(testCaseReq_01)
        print(testCaseRep_01)

    def test02(self):
        testCaseReq_02 = {"country": "US","sellerName":"Gardenwed"}
        testCaseRep_02 = MyDataAmazonSelectInterface().myDataAmazonSelect(testCaseReq_02)
        print(testCaseRep_02)











