'''
@File: test_smt_associateSystemSkuApi.py
@time:2021/8/23
@Author:quanliu
@Desc:我的数据SMT关联系统SKU接口用例
'''

import random

from apps.AllSystemData.DasSystem.das_common_settting import Das_Common_Setting
from apps.AllSystemData.DasSystem.das_api.dasSystem_comConfig import Das_Common_Config
from apps.AllSystemData.DasSystem.das_api.myData_manage.associateSystemSkuApi import AssociateSystemSkuApi

from apps.utils.es_database_util import Es_handleOperator
import unittest

# 数据管理-我的数据SMT关联系统SKU接口用例类
class Test_smtAssociateSySkuApi(unittest.TestCase):
    def firstInputParam(self):
        # 生成随机数
        num = random.randint(1,20)
        query = {
              "from": "{0}".format(num*10),
              "size": 10,
              "query": {
                "match_all": {}
              }
            }
        index = Das_Common_Config.smt_account_product_info
        # 连接数据库从ES数据库随机取出数据
        result = Es_handleOperator(Das_Common_Setting.das_es).data_es(index,query)
        resultList = [] # 用来存放接口第一个入参list
        for i in range(len(result["hits"])):
            resultList.append(result["hits"][i]["_id"]) # 接口第一个入参
        return resultList

    # 用例1接口第二个入参（输入存在SKU）
    def testCase01(self):
        '''SMT关联系统SKU第一个用例'''
        resultList = self.firstInputParam()
        systemSkuStr01 = "8ZZ800161-S-B"
        responseResult01 = AssociateSystemSkuApi().associateSystemSku("SMT","smt_associateSystemSku",resultList, systemSkuStr01)
        print(responseResult01)

    #用例2接口第二个入参（输入不存在SKU）
    def testCase02(self):
        '''SMT关联系统SKU第二个用例'''
        resultList = self.firstInputParam()
        systemSkuStr02 = "8ZZ800161S"
        responseResult02 = AssociateSystemSkuApi().associateSystemSku("SMT","smt_associateSystemSku",resultList, systemSkuStr02)
        print(responseResult02)
