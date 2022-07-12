# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: getMenuPermissionTypes
@time:2022/7/12
@Author:majiaqin 170479
@Desc:菜单权限对接(通过传code返回code类型)
'''

import pprint
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_param import UsermgtApiInputParam
from apps.Common_Config.operate_api_data import Splicing_Params, api_assemble_new

@api_assemble_new()
def getMenuPermissionTypesApi(paramMap=None):
    url = UsermgtApiUrl.getMenuPermissionTypes_url
    params_list = [UsermgtApiInputParam.getMenuPermissionTypes_param01,
                   UsermgtApiInputParam.getMenuPermissionTypes_param02]
    api_params = Splicing_Params(params_list, paramMap).splicing_params()
    return url, api_params

if __name__ == '__main__':
    pprint.pprint(getMenuPermissionTypesApi({'employeeNo': '170479',
                                             'codes': ['1501010101', '1501010102']}))
    pass