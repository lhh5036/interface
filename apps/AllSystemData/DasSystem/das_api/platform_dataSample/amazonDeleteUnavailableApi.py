'''
@File: amazonDeleteUnavailableApi.py
@time:2021/9/1
@Author:quanliu
@Desc:数据采集-Amazon死贴数据删除接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
import json


@api_assemble_new()
def amazonDeleteUnavilableFunction(platform,searchType,idsList):
    app.logger.info("amazonDeleteUnavilableFunction -------->start")
    if len(idsList) == 0 or searchType == "":
        app.logger.error("amazonDeleteUnavilableFunction----->Input Parameter is null")
        return "请求参数searchType或ids或分配人字段为空!"
    # 拼接请求参数
    amazon_deleteUnavailable02 = DasApiInputParam.amazon_deleteUnavailable02
    amazon_deleteUnavailable02["ids"] = idsList
    amazon_deleteUnavailable01 = DasApiInputParam.amazon_deleteUnavailable01
    amazon_deleteUnavailable01["args"] = json.dumps(amazon_deleteUnavailable02)
    url = DasApiUrl.amazon_deleteUnavailable_url
    return url,amazon_deleteUnavailable01
