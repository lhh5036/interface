# -*- coding:utf-8 -*-
#!/usr/bin/python3

'''
@File: pmsSystem_interface_url.py
@time: 2022/6/7
@Author:quanliu 181324
@Desc:采购系统接口地址
'''
from apps.Common_Config.interface_common_info import InterfaceCommonInfo

class PmsApiUrl:

    # 需求管理-采购建议
    purchaseSuggestion_url = InterfaceCommonInfo.common_url + "/newpms/purchaseSuggestion"

    # 需求管理-采购需求
    purchaseRequire_url = InterfaceCommonInfo.common_url + "/newpms/purchaseRequire"
