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
        testCaseRep_01 = MyDataAmazonSelectInterface().myDataAmazonSelect("第一个用例",testCaseReq_01)
        return testCaseRep_01

    def test02(self):
        testCaseReq_02 = {"country": "US","sellerName":"Gardenwed"}
        testCaseRep_02 = MyDataAmazonSelectInterface().myDataAmazonSelect("第二个用例",testCaseReq_02)
        return testCaseRep_02











