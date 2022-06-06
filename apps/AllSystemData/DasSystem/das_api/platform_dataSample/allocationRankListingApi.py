'''
@File: allocationRankListingApi.py
@time:2021/8/27
@Author:quanliu
@Desc:数据采集--分配接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
import json


@api_assemble_new()
def allocationRankListingFunction(platform,searchType,idsList,claimantStr):
    app.logger.info("allocationRankListingFunction -------->start")
    if len(idsList) == 0 or searchType == "" or claimantStr == "":
        app.logger.error("allocationRankListingFunction----->Input Parameter is null")
        return "请求参数searchType或ids或分配人字段为空!"
    # 拼接请求参数
    allocationProduct02 = DasApiInputParam.allocationProduct02
    allocationProduct02["ids"] = idsList
    allocationProduct02["claimant"] = claimantStr
    allocationProduct01 = DasApiInputParam.allocationProduct01
    allocationProduct01["args"] = json.dumps(allocationProduct02)
    url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType) # 请求地址
    return url,allocationProduct01