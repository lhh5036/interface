'''
@File: test_amazon_associateSystemSkuApi.py
@time:2021/8/20
@Author:quanliu 181324
@Desc:数据管理-我的数据Amazon关联系统SKU接口用例
'''

import random

from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.Das.das_interface_service.dasSystem_comConfig import Das_Common_Config
from apps.Das.das_interface_service.myData_manage.associateSystemSkuApi import AssociateSystemSkuApi
from apps.utils.es_database_util import Es_handleOperator
import unittest

# 数据管理-我的数据Amazon关联系统SKU接口用例类
class Test_amazonAssociateSySkuApi(unittest.TestCase):

    # 生成第一个入参
    def firstInputParam(self):
        # 生成随机数
        num = random.randint(1, 20)
        query = {
            "from": "{0}".format(num * 10),
            "size": 10,
            "query": {
                "match_all": {}
            }
        }
        index = Das_Common_Config.amazon_account_product_info
        # 连接数据库从ES数据库随机取出数据
        result = Es_handleOperator("das", "test").data_es(index, query)
        resultList = []  # 用来存放接口第一个入参list
        for i in range(len(result["hits"])):
            resultList.append(result["hits"][i]["_id"])  # 接口第一个入参
        return resultList

    # 用例1接口第二个入参（输入存在SKU）
    def testCase01(self):
        # 接口地址
        url = DasApiUrl.amazon_associateSySku_url
        systemSkuStr01 = "8ZZ800161-S-B"
        paramList = self.firstInputParam()
        responseResult01 = AssociateSystemSkuApi().associateSystemSku(url, paramList, systemSkuStr01)
        print(responseResult01)

    # 用例2接口第二个入参（输入不存在SKU）
    def testCase02(self):
        # 接口地址
        url = DasApiUrl.amazon_associateSySku_url
        systemSkuStr02 = "8ZZ800161S"
        paramList = self.firstInputParam()
        responseResult02 = AssociateSystemSkuApi().associateSystemSku(url,paramList, systemSkuStr02)
        print(responseResult02)

