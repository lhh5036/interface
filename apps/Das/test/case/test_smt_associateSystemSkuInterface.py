'''
@File: test_smt_associateSystemSkuInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:我的数据SMT关联系统SKU接口用例
'''

import random
from apps.Das.das_interface_service.myDataManageComConfig import Das_Common_Config
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl
from apps.Das.das_interface_service.myData_manage.associateSystemSkuInterface import AssociateSystemSkuInterface
from apps.utils.es_database_util import Es_handleOperator

# 数据管理-我的数据SMT关联系统SKU接口用例类
def test_smtAssociateSySkuInterface():
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
    resultList = [] # 用来存放接口第一个入参list
    for i in range(len(result["hits"])):
        resultList.append(result["hits"][i]["_id"]) # 接口第一个入参

    # 接口地址
    url = MyDataManageInterUrl.smt_associateSySku_url

    responseResult = []
    # 用例1接口第二个入参（输入存在SKU）
    systemSkuStr01 = "8ZZ800161-S-B"
    responseResult01 = AssociateSystemSkuInterface().associateSystemSku("第一个用例",url,resultList, systemSkuStr01)
    responseResult.append(responseResult01)



    #用例2接口第二个入参（输入不存在SKU）
    systemSkuStr02 = "8ZZ800161S"
    # 随机取出10条数据，作为入参调用释放产品接口
    responseResult02 = AssociateSystemSkuInterface().associateSystemSku("第二个用例",url,resultList, systemSkuStr02)
    responseResult.append(responseResult02)


    return responseResult