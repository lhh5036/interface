'''
@File: productSystem_interface_url.py
@time:2022/1/18
@Author:全柳 181324
@Desc:产品系统接口地址
'''

from apps.Common_Config.interface_common_info import InterfaceCommonInfo


class ProductApiUrl:
    # 管理单品
    singleItemSelect_url = InterfaceCommonInfo.common_url + "/product/singleItem/getinfo"