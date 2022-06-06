'''
@File: addStoreTaskListApi.py
@time:2021/9/15
@Author:quanliu 181324
@Desc:任务中心-店铺监控-新增店铺接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from flask import current_app as app
import json


@api_assemble_new()
def addStoresTaskListFunction(kwargs):
    app.logger.info("addStoresTaskListFunction------------------->start")
    country = parseRequestDatas("country", kwargs)
    saleChannel = parseRequestDatas("saleChannel",kwargs)
    sellerUrl = parseRequestDatas("sellerUrl",kwargs)
    sellerName = parseRequestDatas("sellerName",kwargs)
    notesInfo = parseRequestDatas("notesInfo",kwargs)
    if country == "" or saleChannel == "" or sellerUrl == "" or sellerName == "":
        app.logger.error("addStoresTaskListFunction---------->Input Params is null")
        return "请求参数为空!"
    # 获取请求参数
    addStoreTask_param02 = DasApiInputParam.addStoreTask_param02
    addStoreTask_param01 = DasApiInputParam.addStoreTask_param01
    # 获取请求地址
    addTask_url = DasApiUrl.addTask_url
    addStoreTask_param02["country"] = country
    addStoreTask_param02["saleChannel"] = saleChannel
    addStoreTask_param02["sellerUrl"] = sellerUrl
    addStoreTask_param02["sellerName"] = sellerName
    addStoreTask_param02["notesInfo"] = notesInfo

    addStoreTask_param01["args"] = json.dumps(addStoreTask_param02)
    return addTask_url,addStoreTask_param01
if __name__ == '__main__':
    print(addStoresTaskListFunction({}))
