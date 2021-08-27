'''
@File: test_smt_selectInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:数据管理-我的数据smt查询接口用例
'''

from apps.Das.das_interface_service.myData_manage.smtProductSelectInterface import \
    SmtProductSelectInterface
import unittest

# 数据管理-我的数据SMT查询接口用例类
class Test_smtSelectInterface(unittest.TestCase):

    def testCase01(self):
        # 用例1
        testCaseReq_01 = {"productId": "4000032062735"}
        testCaseRep_01 = SmtProductSelectInterface().smtQueryProductListing(testCaseReq_01)
        print(testCaseRep_01)

    def testCase02(self):
        testCaseReq_02 = {"mainSku": "9SD400194","productId":"4000032062735"}
        testCaseRep_02 = SmtProductSelectInterface().smtQueryProductListing(testCaseReq_02)
        print(testCaseRep_02)
