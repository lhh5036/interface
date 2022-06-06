'''
@File: tradeMarkListApi.py
@time:2021/9/16
@Author:quanliu 181324
@Desc:工具助手-侵权查询接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from flask import current_app as app
import json
from apps.Common_Config.operate_api_data import api_assemble_new


@api_assemble_new()
def tradeMarkListFunction(tradeMark,paramStr):
    app.logger.info("tradeMarkListFunction------------------->start")
    if tradeMark == "":
        app.logger.error("tradeMarkListFunction------------------->The query region is empty!")
        return "请选择查询地区!"
    if tradeMark == "US":
        url = DasApiUrl.listUsTradeMark_url  # 请求地址
    elif tradeMark == "EU":
        url = DasApiUrl.listEuTradeMark_url  # 请求地址
    # 请求参数
    listTradeMark_param03 = DasApiInputParam.listTradeMark_param03
    listTradeMark_param02 = DasApiInputParam.listTradeMark_param02
    listTradeMark_param01 = DasApiInputParam.listTradeMark_param01
    listTradeMark_param03["keyword"] = paramStr
    listTradeMark_param02["search"] = listTradeMark_param03
    listTradeMark_param01["args"] = json.dumps(listTradeMark_param02)
    return url,listTradeMark_param01

if __name__ == '__main__':
    print(tradeMarkListFunction("US","TSDR"))


