'''
@File: test_amazon_releaseProductApi.py
@time:2021/8/19
@Author:quanliu 181324
@Desc:数据管理-我的数据Amazon释放产品接口用例
'''

import random
import unittest

from apps.DasSystem.das_common_settting import Das_Common_Setting
from apps.DasSystem.das_interface_service.dasSystem_comConfig import Das_Common_Config
from apps.DasSystem.das_interface_service.myData_manage.releaseProductApi import releaseProductInfoApi
from apps.utils.es_database_util import Es_handleOperator

# 数据管理-我的数据Amazon释放产品接口用例
class Test_amazonReleaseRroductApi(unittest.TestCase):
    def firstInputParam(self):
        resultList = []
        # 用例,封装接口入参
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
        for i in range(len(result["hits"])):
            resultList.append(result["hits"][i]["_id"])
        return resultList

    def testCase01(self):
        '''第一个测试用例'''
        resultList = self.firstInputParam()
        responseResult = releaseProductInfoApi().releaseProductInfo("Amazon","amazon_releaseProduct",resultList)
        print(responseResult)

