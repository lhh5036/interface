'''
@File: productSingleItemSelectApi.py
@time:2022/6/8
@Author:quanliu 181324
@Desc:管理单品查询
'''
from apps.AllSystemData.ProductSystem.product_api.productSystem_interface_param import ProductApiInputParam
from apps.AllSystemData.ProductSystem.product_api.productSystem_interface_url import ProductApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Common_Config.operate_api_data import api_assemble_new
from copy import deepcopy
from flask import current_app as app

# 系统订单查询接口
@api_assemble_new(api_header=Common_TokenHeader().token_header_product("new","181324","8010602"))
def productSingleItemSelectApi(paramMap=None):
    app.logger.info("productSingleItemSelectApi  ----->start!")
    url = ProductApiUrl.singleItemSelect_url
    param01 = deepcopy(ProductApiInputParam.singleItemSelect_param01)
    keyList = []
    if paramMap != "":
        for key in paramMap.keys():
            keyList.append(key)
        for i in range(len(keyList)):
            param01[keyList[i]] = paramMap[keyList[i]]
    return url,param01

if __name__ == '__main__':
    print(productSingleItemSelectApi({"itemStatus":[7009]}))
