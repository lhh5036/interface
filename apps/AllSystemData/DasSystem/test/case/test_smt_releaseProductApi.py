'''
@File: test_smt_releaseProductApi.py
@time:2021/8/23
@Author:quanliu
@Desc:我的数据smt释放产品接口用例
'''
import random
import unittest

from apps.AllSystemData.DasSystem.das_common_settting import Das_Common_Setting

from apps.AllSystemData.DasSystem.das_api.dasSystem_comConfig import Das_Common_Config
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.myData_manage.releaseProductApi import releaseProductInfo

from apps.utils.es_database_util import Es_handleOperator

# 数据管理-我的数据SMT释放产品接口用例
class Test_smtReleaseRroductApi(unittest.TestCase):
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
        index = Das_Common_Config.smt_account_product_info
        # 连接数据库从ES数据库随机取出数据
        result = Es_handleOperator(Das_Common_Setting.das_es).data_es(index,query)
        for i in range(len(result["hits"])):
            resultList.append(result["hits"][i]["_id"])
        return resultList

    def testCase01(self):
        '''SMT释放产品第一个用例'''
        # 接口地址
        url = DasApiUrl.smt_releaseProduct_url
        resultList = self.firstInputParam()
        responseResult = releaseProductInfo("SMT","smt_releaseProduct",resultList)
        print(responseResult)


if __name__ == '__main__':
    unittest.main(verbosity=2)