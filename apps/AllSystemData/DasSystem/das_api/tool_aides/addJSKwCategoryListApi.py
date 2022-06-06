'''
@File: addJSKwCategoryListApi.py
@time:2021/9/16
@Author:quanliu 181324
@Desc:工具助手-Jungle Scout规则配置新增规则接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from flask import current_app as app
import json

@api_assemble_new()
def addJSKwCategoryListFunction(kwargs):
    app.logger.info("addJSKwCategoryListFunction------------------->start")
    ruleName = parseRequestDatas("ruleName",kwargs) # 规则名
    category = parseRequestDatas("category",kwargs) # 类目
    country = parseRequestDatas("country",kwargs) # 国家
    if ruleName == "" or country == "" or category == "":
        app.logger.error("addJSKwCategoryListFunction------>ruleName or country or category is null")
        return "规则名或国家或类目为空!"
    url = DasApiUrl.addJsKwRule_url  # 请求地址
    # 请求参数
    addJsKwRule_param02 = DasApiInputParam.addJsKwRule_param02
    addJsKwRule_param01 = DasApiInputParam.addJsKwRule_param01
    keyList = []
    if kwargs != "":
        for key in kwargs.keys():
            keyList.append(key)
        for i in range(len(keyList)):
            value = parseRequestDatas(keyList[i], kwargs)
            addJsKwRule_param02[keyList[i]] = value
    addJsKwRule_param01["args"] = json.dumps(addJsKwRule_param02)
    return url,addJsKwRule_param01

if __name__ == '__main__':
    print(addJSKwCategoryListFunction({"ruleName":"fsdfsdf01","country":"United States","category":"Arts; Crafts & Sewing"}))
