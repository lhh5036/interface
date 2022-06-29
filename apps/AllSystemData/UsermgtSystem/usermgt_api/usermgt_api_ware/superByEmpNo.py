# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: superByEmpNo
@time:2022/6/27
@Author:majiaqin 170479
@Desc:根据账号获取该账号的上一级
'''
import pprint
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_param import UsermgtApiInputParam
from apps.Common_Config.operate_api_data import Splicing_Params, api_assemble_new

@api_assemble_new()
def superByEmpNoApi(paramMap=None):
    url = UsermgtApiUrl.superByEmpNo_url
    params_list = [UsermgtApiInputParam.superByEmpNo_param01]
    api_params = Splicing_Params(params_list, paramMap).splicing_params()
    return url, api_params

if __name__ == '__main__':
    pprint.pprint(superByEmpNoApi({"empNo": "170479"}))
    pass