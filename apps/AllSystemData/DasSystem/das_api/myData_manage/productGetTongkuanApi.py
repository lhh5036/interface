'''
@File: productGetTongkuanApi.py
@time:2021/8/23
@Author:quanliu
@Desc:产品同款接口服务
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app

# 数据管理-同款接口服务
@api_assemble_new()
def productGetTongkuan(paramStr):
    app.logger.info("productGetTongkuan ---->start!")
    if paramStr == "":
        app.logger.error("productGetTongkuan --> ReqParam:paramStr is null!")
        return "请求入参不能为空!"

    # 接口请求地址
    url = DasApiUrl.productGenTongkuan_url

    # 拼接接口请求入参
    paramSelect = DasApiInputParam.productGenTongkuan_select
    paramSelect["asinUrlStr"] = paramStr
    reqParam = DasApiInputParam.productGenTongkuan_param
    reqParam["args"] = str(paramSelect)  # 替换最外层参数
    return url,reqParam
