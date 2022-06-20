'''
@File: purchaseSuggestionApi.py
@time:2022/6/7
@Author: quanliu 181324
@Desc: 需求管理-采购建议接口
'''
from apps.AllSystemData.PmsSystem.pms_api.pmsSystem_interface_param import PmsApiInputParam
from apps.AllSystemData.PmsSystem.pms_api.pmsSystem_interface_url import PmsApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new, Splicing_Params
from flask import current_app as app

# 系统订单查询接口
@api_assemble_new()
def purchaseSuggestionApi(paramMap=None):
    app.logger.info("purchaseSuggestionApi  ----->start!")
    url = PmsApiUrl.purchaseSuggestion_url
    param01 = PmsApiInputParam.purchaseSuggestion_param01
    param02 = PmsApiInputParam.purchaseSuggestion_param02
    param03 = PmsApiInputParam.purchaseSuggestion_param03
    paramList = []
    paramList.append(param01)
    paramList.append(param02)
    paramList.append(param03)
    requestJson = Splicing_Params(paramList,paramMap).splicing_params() # 拼接接口参数的方法
    return url,requestJson

if __name__ == '__main__':
    print(purchaseSuggestionApi({"warehouseAttr":"美景仓"}))
    print(purchaseSuggestionApi({"articleNumber":"5AC304821-A03"}))
