'''
@File: queryCategoryListApi.py
@time:2021/9/11
@Author:quanliu
@Desc:分类监控页面-查询各个平台的分类信息
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonJudgeEmptySevice import PublicCommonJudgeEmptySevice
from apps.AllSystemData.DasSystem.das_api.publicCommonParamService import PublicCommonParamServiceClass
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.operate_api_data import api_assemble_new
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from flask import current_app as app
import json


@api_assemble_new()
def queryCategoryListFunction(platform,searchType,kwargs):# 字典格式
    app.logger.info("queryCategoryListFunction------------------->start")
    # 是否校验入参
    needJudge = PublicCommonJudgeEmptySevice().needJudgeEmpty(platform, searchType, kwargs)
    if needJudge == True:
        app.logger.error("queryCategoryListFunction-------->InputParam is null")
        return "请求参数为空!"
    # 获取请求参数
    categoryListing03, categoryListing02, categoryListing01 = PublicCommonParamServiceClass().getApiInputParam(platform, searchType)
    url = PublicCommonUrlServiceClass().getApiUrl(platform, searchType)  # 获取请求地址
    keyList = []
    if kwargs != "":
        for key in kwargs.keys():
            keyList.append(key)
        for i in range(len(keyList)):
            value = parseRequestDatas(keyList[i], kwargs)
            categoryListing02[keyList[i]] = value
    # 替换最外层
    categoryListing01["args"] = json.dumps(categoryListing02)
    return url,categoryListing01


if __name__ == '__main__':
    print(queryCategoryListFunction("SMT","smt_listCategoryMonitor",{}))
