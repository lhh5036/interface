'''
@File: queryJsKwCategoryListApi.py
@time:2021/9/16
@Author:quanliu 181324
@Desc:工具助手-Jungle Scout规则配置国家类目查询接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from flask import current_app as app
import json
from apps.Common_Config.operate_api_data import api_assemble_new


@api_assemble_new()
def queryJsKwCategoryListFunction(countryStr):
    app.logger.info("queryJsKwCategoryListFunction------------------->start")
    if countryStr == "":
        app.logger.error("queryJsKwCategoryListFunction------------------->country is empty!")
        return "国家字段为空!"
    url = DasApiUrl.queryJsKeywordCategoryList_url  # 请求地址
    # 请求参数
    queryJsKeywordCategoryList_param02 = DasApiInputParam.queryJsKeywordCategoryList_param02
    queryJsKeywordCategoryList_param01 = DasApiInputParam.queryJsKeywordCategoryList_param01
    queryJsKeywordCategoryList_param02["country"] = countryStr
    queryJsKeywordCategoryList_param01["args"] = json.dumps(queryJsKeywordCategoryList_param02)
    return url,queryJsKeywordCategoryList_param01

if __name__ == '__main__':
    print(queryJsKwCategoryListFunction("United Kingdom"))


