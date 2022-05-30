'''
@File: test_amazon_associateSystemSkuApi.py
@time:2021/8/20
@Author:quanliu 181324
@Desc:数据管理-我的数据Amazon关联系统SKU接口用例
'''

import random
from apps.AllSystemData.DasSystem.das_common_settting import Das_Common_Setting
from apps.AllSystemData.DasSystem.das_api.dasSystem_comConfig import Das_Common_Config
from apps.AllSystemData.DasSystem.das_api.myData_manage.associateSystemSkuApi import AssociateSystemSkuApi

from apps.utils.es_database_util import Es_handleOperator
import unittest
import ddt
import os
# 参数化
paramList01 = ["8ZZ800161-S-B","8ZZ800161S"]
# 获取当前文件所在目录的上一级目录
upPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# 数据管理-我的数据Amazon关联系统SKU接口用例类
@ddt.ddt
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
        result = Es_handleOperator(Das_Common_Setting.das_es).data_es(index, query)
        resultList = []  # 用来存放接口第一个入参list
        for i in range(len(result["hits"])):
            resultList.append(result["hits"][i]["_id"])  # 接口第一个入参
        return resultList

    # 配置为yaml文件驱动
    @ddt.file_data(upPath+"/moduleFile/amazonAssociateSkuYaml.yaml")
    @ddt.unpack
    def testCase01(self,sysSkuStr):
        '''Amazon关联系统SKU测试用例'''
        paramList = self.firstInputParam()
        responseResult01 = AssociateSystemSkuApi().associateSystemSku("Amazon","amazon_associateSystemSku", paramList, sysSkuStr)
        print(responseResult01)

    # 参数化驱动
    @ddt.data(*paramList01)
    def testCase02(self, sysSkuStr):
        '''Amazon关联系统SKU测试用例'''
        paramList = self.firstInputParam()
        responseResult02 = AssociateSystemSkuApi().associateSystemSku("Amazon", "amazon_associateSystemSku", paramList,sysSkuStr)
        print(responseResult02)

if __name__ == '__main__':
    unittest.main(verbosity=2)