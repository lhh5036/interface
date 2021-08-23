'''
@File: test_amazon_cancelDevelopInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:我的数据-Amazon取消开发接口用例
'''
import random

from apps.Das.das_interface_service.myDataManageComConfig import Das_Common_Config
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl
from apps.Das.das_interface_service.myData_manage.cancelDevelopmentInterface import CancelDevelopmentInterface
from apps.Das.das_interface_service.param_config.parameterConfigSelect import ParameterConfigQueryInterface
from apps.utils.es_database_util import Es_handleOperator


def test_amazonCancelDevelopInterface():
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
    resultList = [] # 用来存放接口第一个入参list
    for i in range(len(result["hits"])):
        resultList.append(result["hits"][i]["_id"]) # 接口第一个入参

    # 接口第二个入参
    responseData = ParameterConfigQueryInterface().paramConfigQuery("第一个用例")
    secondParam = ",".join(random.sample(responseData.split('[')[1].rstrip("]").split(","),1))

    # 接口地址
    url = MyDataManageInterUrl.amazon_cancelDevelopment_url

    responseResult = []
    responseResult01 = CancelDevelopmentInterface().cancelDevelopmentFunction("第一个用例",url,resultList, secondParam)
    responseResult.append(responseResult01)
    return responseResult

