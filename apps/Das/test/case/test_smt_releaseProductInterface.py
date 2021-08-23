'''
@File: test_smt_releaseProductInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:我的数据smt释放产品接口用例
'''
import random
from apps.Das.das_interface_service.myDataManageComConfig import Das_Common_Config
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl
from apps.Das.das_interface_service.myData_manage.releaseProductInterface import releaseProductInfoInterface
from apps.utils.es_database_util import Es_handleOperator

# 数据管理-我的数据SMT释放产品接口用例
def test_smtReleaseRroductInterface():
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
    result = Es_handleOperator("das","test").data_es(index,query)
    for i in range(len(result["hits"])):
        resultList.append(result["hits"][i]["_id"])

    # 接口地址
    url = MyDataManageInterUrl.smt_releaseProduct_url

    responseResultList = []
    # 随机取出10条数据，作为入参调用释放产品接口
    responseResult = releaseProductInfoInterface().releaseProductInfo("第一个用例",url,resultList)
    responseResultList.append(responseResult)

    return responseResultList
