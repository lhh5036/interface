'''
@File: test_smt_selectApi.py
@time:2021/8/23
@Author:quanliu
@Desc:数据管理-我的数据smt查询接口用例
'''

import unittest
from apps.AllSystemData.DasSystem.das_api.myData_manage.dataManageProductListingApi import dataManageProductListingInfo



# 数据管理-我的数据SMT查询接口用例类
class Test_smtSelectApi(unittest.TestCase):

    def testCase01(self):
        '''这是第一个测试用例'''
        testCaseReq_01 = {"productId": "4000032062735"}
        testCaseRep_01 = dataManageProductListingInfo("SMT","smt_queryListing",testCaseReq_01)
        print(testCaseRep_01)

    def testCase02(self):
        '''这是第二个测试用例'''
        testCaseReq_02 = {"mainSku": "9SD400194","productId":"4000032062735"}
        testCaseRep_02 = dataManageProductListingInfo("SMT","smt_queryListing",testCaseReq_02)
        print(testCaseRep_02)

if __name__ == '__main__':
    unittest.main(verbosity=2)