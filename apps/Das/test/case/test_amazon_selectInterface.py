'''
@File: test_amazon_selectInterface.py
@time:2021/8/19
@Author: quanliu 181324
@Desc:数据管理-我的数据Amazon查询接口用例
'''


from apps.Das.das_interface_service.myData_manage.dataManageAmazon.amazonSelectInterface import MyDataAmazonSelectInterface
import json


# 数据管理-我的数据Amazon查询接口用例类
def test_amazonSelectInterface():

    result = []
    # 用例1
    testCaseReq_01 = {"country": "11US"}
    testCaseRep_01 = MyDataAmazonSelectInterface().myDataAmazonSelect("第一个用例",testCaseReq_01)
    result.append(testCaseRep_01)

    # 用例2
    testCaseReq_02 = {"country": "US","sellerName":"Gardenwed"}
    testCaseRep_02 = MyDataAmazonSelectInterface().myDataAmazonSelect("第二个用例",testCaseReq_02)
    result.append(testCaseRep_02)

    # 将每条用例执行的结果返回
    return result







