# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: getEmployeesByRoleIds
@time:2022/8/12
@Author:majiaqin 170479
@Desc:根据角色id集合，查询角色对应员工信息
'''
import pprint
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.Common_Config.operate_api_data import Splicing_Params, api_assemble

@api_assemble(api_url=UsermgtApiUrl.getEmployeesByRoleIds_url, params=False)
def getEmployeesByRoleIdsApi(paramMap=None):
    return paramMap

if __name__ == '__main__':
    pprint.pprint(getEmployeesByRoleIdsApi('20040709000001, 20120915000035'))
    pass