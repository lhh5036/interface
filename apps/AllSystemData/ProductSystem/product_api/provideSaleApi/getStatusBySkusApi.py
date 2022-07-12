'''
@File: getStatusBySkusApi.py
@time:2022/7/11
@Author:quanliu 181324
@Desc:查询多个货号对应状态
'''

from apps.AllSystemData.ProductSystem.product_api.productSystem_interface_url import ProductApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Common_Config.operate_api_data import api_assemble_new


# 查询多个货号对应状态
@api_assemble_new(api_header=Common_TokenHeader().token_header_product("new","181324","8010602"))
def getStatusBySkusApi(paramList):
    url = ProductApiUrl.getStatusBySkus_url
    param01 = paramList
    return url,param01


if __name__ == '__main__':
    print(getStatusBySkusApi([]))