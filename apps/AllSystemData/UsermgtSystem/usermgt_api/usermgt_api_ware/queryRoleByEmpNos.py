# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: queryRoleByEmpNos
@time:2022/5/19
@Author:majiaqin 170479
@Desc:返回新用户系统某个账号关联的角色名
'''

import pprint
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_param import UsermgtApiInputParam
from apps.Common_Config.operate_api_data import Splicing_Params, api_assemble_new

@api_assemble_new()
def queryRoleByEmpNosApi(paramMap=None):
    url = UsermgtApiUrl.queryRoleByEmpNos_url
    params_list = [UsermgtApiInputParam.queryRoleByEmpNos_param01]
    api_params = Splicing_Params(params_list, paramMap).splicing_params()
    return url, api_params

if __name__ == '__main__':
    pprint.pprint(queryRoleByEmpNosApi(["170763", "170479"]))