# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: getMenuCodes
@time:2022/6/29
@Author:majiaqin 170479
@Desc:根据账号获取该账号的菜单按钮code
'''

import pprint
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_param import UsermgtApiInputParam
from apps.Common_Config.operate_api_data import Splicing_Params, api_assemble_new

@api_assemble_new()
def getMenuCodesApi(paramMap=None):
    url = UsermgtApiUrl.getMenuCodes_url
    params_list = [UsermgtApiInputParam.getMenuCodes_param01]
    api_params = Splicing_Params(params_list, paramMap).splicing_params()
    return url, api_params

if __name__ == '__main__':
    pprint.pprint(getMenuCodesApi({"args": "171080"}))
    pass