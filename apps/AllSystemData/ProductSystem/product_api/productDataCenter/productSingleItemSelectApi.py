'''
@File: productSingleItemSelectApi.py
@time:2022/6/8
@Author:quanliu 181324
@Desc:管理单品查询
'''
from apps.AllSystemData.ProductSystem.product_api.productSystem_interface_param import ProductApiInputParam
from apps.AllSystemData.ProductSystem.product_api.productSystem_interface_url import ProductApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Common_Config.operate_api_data import api_assemble_new, Splicing_Params

# 系统订单查询接口
@api_assemble_new(api_header=Common_TokenHeader().token_header_product("new","181324","8010602"))
def productSingleItemSelectApi(paramMap=None):
    url = ProductApiUrl.singleItemSelect_url
    param01 = ProductApiInputParam.singleItemSelect_param01
    paramList = []
    paramList.append(param01)
    param01 = Splicing_Params(paramList, paramMap).splicing_params()
    return url,param01

if __name__ == '__main__':
    print(productSingleItemSelectApi({"itemStatus":[7009]}))
