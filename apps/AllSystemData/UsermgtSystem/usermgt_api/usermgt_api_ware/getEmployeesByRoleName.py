# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: getEmployeesByRoleName
@time:2022/7/12
@Author:majiaqin 170479
@Desc:根据角色名称获取关联该角色的所有账号
'''
import pprint
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new

@api_assemble_new(api_method='get')
def getEmployeesByRoleNameApi(paramMap=None):
    url = UsermgtApiUrl.getEmployeesByRoleName_url.format(paramMap['roldname'])
    return url, paramMap

if __name__ == '__main__':
    pprint.pprint(getEmployeesByRoleNameApi({'roldname': '全部权限'}))
    pass