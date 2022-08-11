# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: listEmployeeByDeptName
@time:2022/8/5
@Author:majiaqin 170479
@Desc:根据组织架构名称,获取当前级和下级用户
'''

import pprint
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_param import UsermgtApiInputParam
from apps.Common_Config.operate_api_data import Splicing_Params, api_assemble_new

@api_assemble_new()
def listEmployeeByDeptNameApi(paramMap=None):
    url = UsermgtApiUrl.listEmployeeByDeptName_url
    params_list = [UsermgtApiInputParam.listEmployeeByDeptName_param01]
    api_params = Splicing_Params(params_list, paramMap).splicing_params()
    return url, api_params

if __name__ == '__main__':
    pprint.pprint(listEmployeeByDeptNameApi({"args": "Amazon"}))
    pass