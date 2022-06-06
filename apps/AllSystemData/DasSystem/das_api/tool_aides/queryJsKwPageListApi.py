'''
@File: queryJsKwPageListApi.py
@time:2021/9/16
@Author:quanliu 181324
@Desc:工具助手-Amazon关键词库查询接口
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from flask import current_app as app
import json

@api_assemble_new()
def queryJsKwPageListFunction(kwargs):# 参数为dict格式
    app.logger.info("queryJsKwPageListFunction------------------->start")
    url = DasApiUrl.queryJsKw_url  # 请求地址
    # 请求参数
    queryJsKw_param03 = DasApiInputParam.queryJsKw_param03
    queryJsKw_param02 = DasApiInputParam.queryJsKw_param02
    queryJsKw_param01 = DasApiInputParam.queryJsKw_param01
    keyList = []
    if kwargs != "":
        for key in kwargs.keys():
            keyList.append(key)
        for i in range(len(keyList)):
            value = parseRequestDatas(keyList[i],kwargs)
            queryJsKw_param03[keyList[i]] = value
    queryJsKw_param02["search"] = queryJsKw_param03
    queryJsKw_param01["args"] = json.dumps(queryJsKw_param02)
    return url,queryJsKw_param01

if __name__ == '__main__':
    print(queryJsKwPageListFunction({}))
