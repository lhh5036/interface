'''
@File: deleteRankListingApi.py
@time:2021/8/27
@Author:quanliu
@Desc:数据采集-删除接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
import json

@api_assemble_new()
def deleteRankListingFunction(platform,searchType,paramList): # 请求参数为List
    app.logger.info("deleteRankListingFunction--------->start")
    if len(paramList) == 0:
        app.logger.error("deleteRankListingFunction----->InputParameter is null")
        return "请求参数为空!"
    # 对入参进行参数化
    deleteProduct02 = DasApiInputParam.deleteProduct02
    deleteProduct02["ids"] = paramList
    deleteProduct01 = DasApiInputParam.deleteProduct01
    deleteProduct01["args"] = json.dumps(deleteProduct02)
    url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
    return url,deleteProduct01
