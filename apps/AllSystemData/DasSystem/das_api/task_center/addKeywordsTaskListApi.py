'''
@File: addKeywordsTaskListApi.py
@time:2021/9/15
@Author:quanliu 181324
@Desc:任务中心-关键词监控-新增关键词接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from flask import current_app as app
import json


@api_assemble_new()
def addKeywordsTaskListFunction(kwargs):
    app.logger.info("addKeywordsTaskListFunction------------------->start")
    country = parseRequestDatas("country", kwargs)
    saleChannel = parseRequestDatas("saleChannel",kwargs)
    keyword = parseRequestDatas("keyword",kwargs)
    if country == "" or saleChannel == "" or keyword == "":
        app.logger.error("addKeywordsTaskListFunction---------->Input Params is null")
        return "请求参数为空!"
    # 获取请求地址
    addTask_url = DasApiUrl.addTask_url
    # 获取请求参数
    addKeywordsTask_param02 = DasApiInputParam.addKeywordsTask_param02
    addKeywordsTask_param01 = DasApiInputParam.addKeywordsTask_param01
    addKeywordsTask_param02["country"] = country
    addKeywordsTask_param02["saleChannel"] = saleChannel
    addKeywordsTask_param02["keyword"] = keyword

    addKeywordsTask_param01["args"] = json.dumps(addKeywordsTask_param02)
    return addTask_url,addKeywordsTask_param01


if __name__ == '__main__':
    print(addKeywordsTaskListFunction({"taskType":2,"country":"US","keyword":"椅子","saleChannel":"Amazon"}))
