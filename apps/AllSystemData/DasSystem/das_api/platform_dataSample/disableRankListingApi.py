'''
@File: disableRankListingApi.py
@time:2021/8/27
@Author:quanliu
@Desc:数据采集-禁用接口类
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
import json


@api_assemble_new()
def disableRankListingFunction(platform,searchType,paramList): # 请求参数为List
    app.logger.info("disableRankListingFunction--------->start")
    if len(paramList) == 0:
        app.logger.error("disableRankListingFunction----->InputParameter is null")
        return "请求参数为空!"
    # 对入参进行参数化
    disableProduct02 = DasApiInputParam.disableProduct02
    disableProduct02["ids"] = paramList
    disableProduct01 = DasApiInputParam.disableProduct01
    disableProduct01["args"] = json.dumps(disableProduct02)
    url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
    return url,disableProduct01