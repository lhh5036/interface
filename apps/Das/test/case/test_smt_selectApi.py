'''
@File: test_smt_selectApi.py
@time:2021/8/23
@Author:quanliu
@Desc:数据管理-我的数据smt查询接口用例
'''

import unittest

from apps.Das.das_interface_service.myData_manage.smtProductSelectApi import SmtProductSelectApi


# 数据管理-我的数据SMT查询接口用例类
class Test_smtSelectApi(unittest.TestCase):

    def testCase01(self):
        # 用例1
        testCaseReq_01 = {"productId": "4000032062735"}
        testCaseRep_01 = SmtProductSelectApi().smtQueryProductListing(testCaseReq_01)
        print(testCaseRep_01)

    def testCase02(self):
        testCaseReq_02 = {"mainSku": "9SD400194","productId":"4000032062735"}
        testCaseRep_02 = SmtProductSelectApi().smtQueryProductListing(testCaseReq_02)
        print(testCaseRep_02)
