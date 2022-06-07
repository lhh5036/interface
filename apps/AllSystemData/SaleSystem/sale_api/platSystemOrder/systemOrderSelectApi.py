'''
@File: systemOrderSelectApi.py
@time:2022/1/18
@Author:quanliu 181324
@Desc:系统订单查询接口
'''
from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_param import SaleApiInputParam
from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_url import SaleApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new
import json
# from flask import current_app as app

# 系统订单查询接口
@api_assemble_new(login_method="old")
def systemOrderQueryFun(platform,paramMap=None):
    # app.logger.info("systemOrderQueryFun  ----->start!")
    if platform == "":
        # app.logger.error("systemOrderQueryFun ------>request parameter(platform) is wrong!")
        return "请求参数为空"

    # 获取url
    url = SaleApiUrl.systemOrder_queryListing_url
    # 获取参数
    param03 = SaleApiInputParam.systemOrder_query_param03
    param02 = SaleApiInputParam.systemOrder_query_param02
    param01 = SaleApiInputParam.systemOrder_query_param01
    param03["saleChannel"] = platform
    param02["search"] = param03
    param01["args"] = json.dumps(param02)
    return url,param01

if __name__ == '__main__':
    print(systemOrderQueryFun("Amazon"))