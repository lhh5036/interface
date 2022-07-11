'''
@File: getEnrollDateBySkusApi.py
@time:2022/7/11
@Author:quanliu 181324
@Desc:查询最近七天的sku信息
'''

import pprint
from apps.AllSystemData.ProductSystem.product_api.productSystem_interface_url import ProductApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Common_Config.operate_api_data import api_assemble_new

# 查询最近七天的sku信息
@api_assemble_new(api_method="get",api_header=Common_TokenHeader().token_header_product("new","181324","8010602"))
def getEnrollDateBySkusApi():
    url = ProductApiUrl.getEnrollDateBySkus_url
    param01 = ""
    return url,param01

if __name__ == '__main__':
    pprint.pprint(getEnrollDateBySkusApi())