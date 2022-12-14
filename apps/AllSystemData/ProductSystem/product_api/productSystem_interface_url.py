'''
@File: productSystem_interface_url.py
@time:2022/1/18
@Author:全柳 181324
@Desc:产品系统接口地址
'''

from apps.Common_Config.interface_common_info import InterfaceCommonInfo


class ProductApiUrl:
    # 管理单品
    singleItemSelect_url = InterfaceCommonInfo.common_url + "/product-service/singleItem/getinfo"

    # 查询最近七天的sku信息
    getEnrollDateBySkus_url = InterfaceCommonInfo.common_url + "/product-service/api/order/getEnrollDateBySkus?day=7"

    # 查询多个货号对应状态
    getStatusBySkus_url = InterfaceCommonInfo.common_url + "/product-service/api/order/getStatusBySkus"