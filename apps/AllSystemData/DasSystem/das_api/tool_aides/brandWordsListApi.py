'''
@File: brandWordsListApi.py
@time:2021/9/16
@Author:quanliu 181324
@Desc:工具助手-USpto商标词查询接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from flask import current_app as app
import json
from apps.Common_Config.operate_api_data import api_assemble_new


@api_assemble_new()
def brandWordsListFunction(brandWordType,paramStr):
    app.logger.info("brandWordsListFunction------------------->start")
    if brandWordType == "":
        app.logger.error("brandWordsListFunction------------------->Brand Words Type is empty!")
        return "商标词类型为空!"
    if brandWordType == "USpto":
        url = DasApiUrl.listNewUsTradeMark_url  # 请求地址
    elif brandWordType == "EUipo":
        url = DasApiUrl.listNewEuTradeMark_url
    # 请求参数
    listNewTradeMark_param03 = DasApiInputParam.listNewTradeMark_param03
    listNewTradeMark_param02 = DasApiInputParam.listNewTradeMark_param02
    listNewTradeMark_param01 = DasApiInputParam.listNewTradeMark_param01
    listNewTradeMark_param03["wordMark"] = paramStr
    listNewTradeMark_param02["search"] = listNewTradeMark_param03
    listNewTradeMark_param01["args"] = json.dumps(listNewTradeMark_param02)
    return url,listNewTradeMark_param01


if __name__ == '__main__':
    print(brandWordsListFunction("EUipo","EMC3EL"))
