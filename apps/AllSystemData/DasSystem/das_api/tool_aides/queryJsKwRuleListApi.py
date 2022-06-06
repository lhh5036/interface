'''
@File: queryJsKwRuleListApi.py
@time:2021/9/16
@Author:quanliu 181324
@Desc:工具助手-Jungle Scout规则配置查询接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from flask import current_app as app
import json

@api_assemble_new()
def queryJsKwRuleListFunction(kwargs):# 参数为dict格式
    app.logger.info("queryJsKwRuleListFunction------------------->start")
    url = DasApiUrl.queryJsKwRule_url  # 请求地址
    # 请求参数
    queryJsKwRule_param03 = DasApiInputParam.queryJsKwRule_param03
    queryJsKwRule_param02 = DasApiInputParam.queryJsKwRule_param02
    queryJsKwRule_param01 = DasApiInputParam.queryJsKwRule_param01
    keyList = []
    if kwargs != "":
        for key in kwargs.keys():
            keyList.append(key)
        for i in range(len(keyList)):
            value = parseRequestDatas(keyList[i],kwargs)
            queryJsKwRule_param03[keyList[i]] = value
    queryJsKwRule_param02["search"] = queryJsKwRule_param03
    queryJsKwRule_param01["args"] = json.dumps(queryJsKwRule_param02)
    return url,queryJsKwRule_param01

if __name__ == '__main__':
    print(queryJsKwRuleListFunction({}))
