'''
@File: saleSystem_interface_url.py
@time:2022/1/18
@Author:全柳 181324
@Desc:订单系统接口地址
'''

from apps.Common_Config.interface_common_info import InterfaceCommonInfo


class SaleApiUrl:
    # 系统订单查询地址
    systemOrder_queryListing_url = InterfaceCommonInfo.common_url + "/sale/customerOrder"

    # 生成系统订单
    lazadaGenerateSysOrder_url = InterfaceCommonInfo.common_url + "/sale/lazadaOrder/generateCustomerOrder"
    otherGenerateSysOrder_url = InterfaceCommonInfo.common_url + "/sale/customerOrder"

    # 同步追踪号
    syncLogisticsTracking_url = InterfaceCommonInfo.common_url + "/sale/customerOrder/isAllocateProducts/true"

    # SMT-《平台订单》地址
    aliexpressOrderQuery_url = InterfaceCommonInfo.common_url + "/sale/aliexpressOrder"

    # 查询资费国家
    tariffCountry_url = InterfaceCommonInfo.common_url + "/sale/country"
