'''
@File: purchaseSuggestionApi.py
@time:2022/6/7
@Author: quanliu 181324
@Desc: 需求管理-采购建议接口
'''
from copy import deepcopy
from apps.AllSystemData.PmsSystem.pms_api.pmsSystem_interface_param import PmsApiInputParam
from apps.AllSystemData.PmsSystem.pms_api.pmsSystem_interface_url import PmsApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new
import json
from apps.Common_Config.parseRequestDatas import parseRequestDatas
# from flask import current_app as app

# 系统订单查询接口
@api_assemble_new()
def purchaseSuggestionApi(paramMap=None):
    # app.logger.info("purchaseSuggestionApi  ----->start!")
    url = PmsApiUrl.purchaseSuggestion_url
    param03 = deepcopy(PmsApiInputParam.purchaseSuggestion_param03)
    keyList = []
    if paramMap != None:
        for key in paramMap.keys():
            keyList.append(key)
        for i in range(len(keyList)):
            value = parseRequestDatas(keyList[i], paramMap)
            param03[keyList[i]] = value

    param01 = PmsApiInputParam.purchaseSuggestion_param01
    param02 = PmsApiInputParam().purchaseSuggestion_param02

    param02["search"] = param03
    param01["args"] = json.dumps(param02)
    return url,param01

if __name__ == '__main__':
    print(purchaseSuggestionApi())

