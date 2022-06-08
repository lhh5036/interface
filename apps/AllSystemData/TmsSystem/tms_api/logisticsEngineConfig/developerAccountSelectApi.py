'''
@File: developerAccountSelectApi.py
@time:2022/6/8
@Author:quanliu 181324
@Desc:物流配置-管理开发者账号查询接口
'''
from apps.AllSystemData.TmsSystem.tms_api.tmsSystem_interface_param import TmsApiInputParam
from apps.AllSystemData.TmsSystem.tms_api.tmsSystem_interface_url import TmsApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new
from copy import deepcopy
# from flask import current_app as app
import json

# 物流配置-管理开发者账号查询接口
@api_assemble_new()
def developerAccountSelectApi(paramMap=None):
    # app.logger.info("developerAccountSelectApi  ----->start!")
    url = TmsApiUrl.developerAccountSelect_url
    param03 = deepcopy(TmsApiInputParam.developerAccountSelect_param03)
    param02 = TmsApiInputParam.developerAccountSelect_param02
    param01 = TmsApiInputParam.developerAccountSelect_param01
    keyList = []
    if paramMap != "":
        for key in paramMap.keys():
            keyList.append(key)
        for i in range(len(keyList)):
            param03[keyList[i]] = paramMap[keyList[i]]

    param02["search"] = param03
    param01["args"] = json.dumps(param02)
    return url,param01


if __name__ == '__main__':
    print(developerAccountSelectApi({}))