'''
@File: test_amazon_releaseProductInterface.py
@time:2021/8/19
@Author:quanliu 181324
@Desc:数据管理-我的数据Amazon释放产品接口用例
'''

from flask import Flask
import random
from apps.Das.das_interface_service.myData_manage.dataManageAmazon.releaseProductInterface import AmazonReleaseProductInfoInterface
from apps.Das.das_interface_service.myData_manage.myDataManageComConfig import Das_Common_Config
from apps.utils.es_database_util import Es_handleOperator

app = Flask(__name__)

# 数据管理-我的数据Amazon释放产品接口用例
@app.route('/dataManage/amazon/releaseRroductInterface')
def test_amazonReleaseRroductInterface():
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

    # 随机取出10条数据，作为入参调用释放产品接口
    responseResult = AmazonReleaseProductInfoInterface().releaseProductInfo(resultList)
    return responseResult


if __name__ == '__main__':
    app.run(debug = True)
