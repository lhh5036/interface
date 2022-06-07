'''
@File: syncLogisticsTrackingApi.py
@time:2022/6/7
@Author:quanliu 181324
@Desc:同步追踪号
'''


from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_param import SaleApiInputParam
from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_url import SaleApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new
import json
from flask import current_app as app

# 系统订单查询接口
@api_assemble_new(login_method="old")
def syncLogisticsTrackingFunc(platform,paramList):
    app.logger.info("systemOrderQueryFun  ----->start!")
    if platform == "" or len(paramList) <= 0:
        app.logger.error("systemOrderQueryFun ------>request parameter is wrong!")
        return "请求参数为空"

    # 获取url
    url = SaleApiUrl.syncLogisticsTracking_url
    # 获取参数
    param02 = SaleApiInputParam.syncLogisticsTracking_param02
    param01 = SaleApiInputParam.syncLogisticsTracking_param01
    param02 = paramList
    param01["args"] = json.dumps(param02)
    return url,param01