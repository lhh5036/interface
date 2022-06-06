'''
@File: test_amazon_cancelDevelopApi.py
@time:2021/8/23
@Author:quanliu
@Desc:我的数据-Amazon取消开发接口用例(SMT共用)
'''
import random

from apps.AllSystemData.DasSystem.das_common_settting import Das_Common_Setting
from apps.AllSystemData.DasSystem.das_api.dasSystem_comConfig import Das_Common_Config
from apps.AllSystemData.DasSystem.das_api.myData_manage.cancelDevelopmentApi import cancelDevelopmentFunction
from apps.AllSystemData.DasSystem.das_api.param_config.parameterConfigSelectApi import \
    ParameterConfigQueryApi

from apps.utils.es_database_util import Es_handleOperator
import unittest

class Test_amazonCancelDevelopApi(unittest.TestCase):
    # 生成第一个入参
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
        index = Das_Common_Config.amazon_account_product_info
        # 连接数据库从ES数据库随机取出数据
        result = Es_handleOperator(Das_Common_Setting.das_es).data_es(index,query)
        resultList = [] # 用来存放接口第一个入参list
        for i in range(len(result["hits"])):
            resultList.append(result["hits"][i]["_id"]) # 接口第一个入参
        return resultList

    def testCase01(self):
        '''这是第一个测试用例'''
        responseData = ParameterConfigQueryApi().paramConfigQuery()
        secondParam = ",".join(random.sample(responseData.split('[')[1].rstrip("]").split(","),1))
        resultList = self.firstInputParam()
        responseResult01 = cancelDevelopmentFunction("Amazon","amazon_cancelDevelopment", resultList, secondParam)
        print(responseResult01)

