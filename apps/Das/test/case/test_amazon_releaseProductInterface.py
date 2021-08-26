'''
@File: test_amazon_releaseProductInterface.py
@time:2021/8/19
@Author:quanliu 181324
@Desc:数据管理-我的数据Amazon释放产品接口用例
'''

import random
import unittest
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl
from apps.Das.das_interface_service.myDataManageComConfig import Das_Common_Config
from apps.Das.das_interface_service.myData_manage.releaseProductInterface import releaseProductInfoInterface
from apps.utils.es_database_util import Es_handleOperator

# 数据管理-我的数据Amazon释放产品接口用例
class Test_amazonReleaseRroductInterface(unittest.TestCase):
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
        result = Es_handleOperator("das","test").data_es(index,query)
        for i in range(len(result["hits"])):
            resultList.append(result["hits"][i]["_id"])
        return resultList

    def test01(self):
        resultList = self.firstInputParam()
        # 接口地址
        url = MyDataManageInterUrl.amazon_releaseProduct_url
        responseResult = releaseProductInfoInterface().releaseProductInfo(url,resultList)
        print(responseResult)

