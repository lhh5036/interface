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


    # 同步追踪号
    syncLogisticsTracking_url = InterfaceCommonInfo.common_url + "/sale/customerOrder/isAllocateProducts/true"