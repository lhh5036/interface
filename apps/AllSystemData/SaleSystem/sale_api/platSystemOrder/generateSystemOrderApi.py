'''
@File: generateSystemOrderApi.py
@time:2022/6/7
@Author:quanliu 181324
@Desc:生成系统订单接口
'''


from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_param import SaleApiInputParam
from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_url import SaleApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new
import json
from flask import current_app as app

# 系统订单查询接口
@api_assemble_new(login_method="old")
def generateSystemOrderApi(platform,saleChannelOrderId,accountNumber): # 平台/平台订单ID/账号
    app.logger.info("generateSystemOrderApi  ----->start!")
    if platform == "Lazada" and saleChannelOrderId == "" and accountNumber=="":
        app.logger.error("generateSystemOrderApi ------>request parameter is wrong!")
        return "平台{0}请求参数{1}/{2}为空".format(platform,saleChannelOrderId,accountNumber)
    else:
        if saleChannelOrderId == "":
            # app.logger.error("generateSystemOrderApi ------>request parameter is wrong!")
            return "平台{0}请求参数{1}为空".format(platform, saleChannelOrderId)

    if platform == "Lazada":
        url = SaleApiUrl.lazadaGenerateSysOrder_url # lazada平台的地址
        param01 = SaleApiInputParam.lazadaGenerateSysOrder_param01
        param01[0]["saleChannelOrderId"] = saleChannelOrderId
        param01[0]["accountNumber"] = accountNumber
    else:
        url = SaleApiUrl.otherGenerateSysOrder_url # 其他平台地址
        param02 = SaleApiInputParam.otherGenerateSysOrder_param02
        param01 = SaleApiInputParam.otherGenerateSysOrder_param01
        param02["saleChannel"] = platform
        param02["saleChannelOrderId"] = saleChannelOrderId
        param01["args"] = json.dumps(param02)
    return url, param01
