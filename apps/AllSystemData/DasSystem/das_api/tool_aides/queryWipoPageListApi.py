'''
@File: queryWipoPageListApi.py
@time:2021/9/16
@Author:quanliu 181324
@Desc:工具助手-WIPO商标词
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from flask import current_app as app
import json


@api_assemble_new()
def queryWipoPageListFunciton(kwargs):# 参数为dict格式
    app.logger.info("queryWipoPageListFunciton------------------->start")
    url = DasApiUrl.queryWipoPage_url  # 请求地址
    # 请求参数
    queryWipoPage_param03 = DasApiInputParam.queryWipoPage_param03
    queryWipoPage_param02 = DasApiInputParam.queryWipoPage_param02
    queryWipoPage_param01 = DasApiInputParam.queryWipoPage_param01
    keyList = []
    if kwargs != "":
        for key in kwargs.keys():
            keyList.append(key)
        for i in range(len(keyList)):
            value = parseRequestDatas(keyList[i],kwargs)
            queryWipoPage_param03[keyList[i]] = value
    queryWipoPage_param02["search"] = queryWipoPage_param03
    queryWipoPage_param01["args"] = json.dumps(queryWipoPage_param02)
    return url,queryWipoPage_param01

if __name__ == '__main__':
    print(queryWipoPageListFunciton({"source":"AETM","startCrawlTime":"2021-03-26 00:00:00","endCrawlTime":"2021-03-27 00:00:00"}))
