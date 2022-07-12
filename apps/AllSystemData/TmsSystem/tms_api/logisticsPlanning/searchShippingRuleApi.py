'''
@File: searchShippingRuleApi.py
@time:2022/7/12
@Author:quanliu 181324
@Desc:物流规则-物流自定义规则-查询
'''
from apps.AllSystemData.TmsSystem.tms_api.tmsSystem_interface_param import TmsApiInputParam
from apps.AllSystemData.TmsSystem.tms_api.tmsSystem_interface_url import TmsApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new, Splicing_Params


# 物流规则-物流自定义规则-查询
@api_assemble_new()
def searchShippingRuleApi(paramMap=None):
    url = TmsApiUrl.shippingruleSelect_url
    param01 = TmsApiInputParam.shippingruleSelect_param01
    param02 = TmsApiInputParam.shippingruleSelect_param02
    param03 = TmsApiInputParam.shippingruleSelect_param03
    paramList = []
    paramList.append(param01)
    paramList.append(param02)
    paramList.append(param03)
    requestJson = Splicing_Params(paramList, paramMap).splicing_params()  # 拼接接口参数的方法
    return url,requestJson

if __name__ == '__main__':
    print(searchShippingRuleApi({"statusList":["10"]}))