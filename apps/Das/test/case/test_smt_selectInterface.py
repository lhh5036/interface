'''
@File: test_smt_selectInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:数据管理-我的数据smt查询接口用例
'''

# 数据管理-我的数据SMT查询接口用例类
from apps.Das.das_interface_service.myData_manage.smtProductSelectInterface import \
    SmtProductSelectInterface


def test_smtSelectInterface():

    result = []
    # 用例1
    testCaseReq_01 = {"productId": "4000032062735"}
    testCaseRep_01 = SmtProductSelectInterface().smtQueryProductListing("第一个用例",testCaseReq_01)
    result.append(testCaseRep_01)

    # 用例2
    testCaseReq_02 = {"mainSku": "9SD400194","productId":"4000032062735"}
    testCaseRep_02 = SmtProductSelectInterface().smtQueryProductListing("第二个用例",testCaseReq_02)
    result.append(testCaseRep_02)

    # 将每条用例执行的结果返回
    return result
