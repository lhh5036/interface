# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: getRDPEmployees
@time:2022/4/21
@Author:majiaqin 170479
@Desc:查看账号在该页面下的数据权限
'''
import pprint
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.Common_Config.operate_api_data import api_assemble
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list


class GetRDPEmployeesApi():
    def __init__(self):
        pass

    '''数据库获取员工账号'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_employeeNo(self):
        sql = "SELECT employee_no FROM employee LIMIT 10;"
        return sql

    '''数据库获取菜单code'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_menuCode(self):
        sql = "SELECT code FROM menu LIMIT 10;"
        return sql

    @classmethod
    def splicing_params_list(cls):
        get_employeeNo_list = cls().get_employeeNo()
        get_menuCode_list = cls().get_menuCode()
        params_list = []
        for i in range(len(get_employeeNo_list)):
            params_list.append([get_employeeNo_list[i],
                                get_menuCode_list[i]])
        return params_list


if __name__ == '__main__':
    pprint.pprint(GetRDPEmployeesApi().splicing_params_list())
    pass