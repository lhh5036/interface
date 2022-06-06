'''
@File: getAllocationUserListApi.py
@time:2021/9/1
@Author:quanliu
@Desc:数据采集-获取分配人员信息接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
import json


@api_assemble_new()
def getAllocationUserListFunction(platform,searchType,jobNumber): # 请求参数为用户工号
    app.logger.info("getAllocationUserListFunction--------->start")
    if jobNumber == "":
        app.logger.error("getAllocationUserListFunction----->InputParameter is null")
        return "请求参数为空!"
    # 对入参进行参数化
    allocationPerson02 = DasApiInputParam.allocationPerson02
    allocationPerson02["jobNumber"] = jobNumber
    allocationPerson01 = DasApiInputParam.allocationPerson01
    allocationPerson01["args"] = json.dumps(allocationPerson02)
    url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
    return url,allocationPerson01