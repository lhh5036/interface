'''
@File: enableRankListingApi.py
@time:2021/8/27
@Author:quanliu
@Desc:数据采集-启用接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
import json


@api_assemble_new()
def enableRankListingFunction(platform,searchType,paramList): # 请求参数为List
    app.logger.info("enableRankListingFunction--------->start")
    if len(paramList) == 0:
        app.logger.error("enableRankListingFunction----->InputParameter is null")
        return "请求参数为空!"
    # 对入参进行参数化
    enableProduct02 = DasApiInputParam.enableProduct02
    enableProduct02["ids"] = paramList
    enableProduct01 = DasApiInputParam.enableProduct01
    enableProduct01["args"] = json.dumps(enableProduct02)
    url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
    return url,enableProduct01