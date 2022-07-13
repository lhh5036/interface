# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: getOaccountCodeAndNames
@time:2022/7/13
@Author:majiaqin 170479
@Desc:获取付款单供应商账户列表
'''
import pprint
from apps.AllSystemData.FmisSystem.fmis_api.fmisSystem_interface_url import FmisApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new

@api_assemble_new(api_method='get')
def getOaccountCodeAndNamesApi(paramMap=None):
    url = FmisApiUrl.getOaccountCodeAndNames_url
    return url, paramMap

if __name__ == '__main__':
    pprint.pprint(getOaccountCodeAndNamesApi())
    pass