# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: getSmtSellerAccount
@time:2022/7/13
@Author:majiaqin 170479
@Desc:平台账单-SMT-账单数据&退款详情&支付宝报告-获取账号接口
'''
import pprint
from apps.AllSystemData.FmisSystem.fmis_api.fmisSystem_interface_url import FmisApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new

@api_assemble_new(api_method='get')
def getSmtSellerAccountApi(paramMap=None):
    url = FmisApiUrl.smtPlatformBill_getSmtSellerAccount_url
    return url, paramMap

if __name__ == '__main__':
    pprint.pprint(getSmtSellerAccountApi())
    pass