'''
@File: claimRankListingApi.py
@time:2021/8/26
@Author:quanliu
@Desc:数据采集-认领产品接口类
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
import json


@api_assemble_new()
def claimRankListingFun(platform,searchType,paramList):
    app.logger.info("claimRankListingFun -------->start")
    if len(paramList) == 0:
        app.logger.error("claimRankListingFun----->Input Parameter is null")
        return "请求参数为空"
    # 参数化接口入参
    claimProduct02 = DasApiInputParam.claimProduct02
    claimProduct02["ids"] = paramList
    claimProduct01 = DasApiInputParam.claimProduct01
    claimProduct01["args"] = json.dumps(claimProduct02)
    url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
    return url,claimProduct01