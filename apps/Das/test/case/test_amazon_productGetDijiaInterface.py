'''

File: test_amazon_productGetDijiaInterface.py
@ bme:2021/8/23
@Author:quanliu
@Desc:数据管理-我的数据Amazon页面低价接口用例
'''
from apps.Das.das_interface_service.myData_manage.productGetDijiaInterface import \
    ProductGetDijiaInterface
from apps.Das.das_interface_service.myDataManageComConfig import Das_Common_Config
from apps.utils.es_database_util import Es_handleOperator
import random
import unittest

# 数据管理-我的数据Amazon页面低价接口用例类
class Test_amazonProdcutGetDijia(unittest.TestCase):
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
        reqParam = result["hits"][0]["_source"]["amazonAsinIncrementInfos"][0]["imageUrls"][0] # 接口第一个入参string
        return reqParam

    def test01(self):
        reqParam = self.firstInputParam()
        responseResult = ProductGetDijiaInterface().productDetDiJia(reqParam)
        print(responseResult)

