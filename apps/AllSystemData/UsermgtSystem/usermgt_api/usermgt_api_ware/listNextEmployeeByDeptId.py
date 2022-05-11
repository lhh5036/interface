# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: listNextEmployeeByDeptId
@time:2022/5/10
@Author:majiaqin 170479
@Desc:查看该组织架构id的下级员工
'''
import pprint
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list

class ListNextEmployeeByDeptIdApi():
    def __init__(self):
        pass

    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_deptid(self):
        sql = "SELECT id FROM org_struct LIMIT 10;"
        return sql

    @classmethod
    def splicing_params_list(cls):
        params_list = cls().get_deptid()
        return params_list

if __name__ == '__main__':
    pprint.pprint(ListNextEmployeeByDeptIdApi().splicing_params_list())
    pass