# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: getEmployeeList
@time:2022/5/16
@Author:majiaqin 170479
@Desc:根据职位查询员工
'''
import pprint
from apps.utils.mySql_database_util import get_data, convert_list
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting

class GetEmployeeListApi():
    def __init__(self):
        pass

    '''获取职位名称'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_position_name(self):
        sql = "SELECT position_name FROM employee \
WHERE position_name IS NOT NULL \
LIMIT 10;"
        return sql

    @classmethod
    def splicing_params_list(cls):
        params_list = cls().get_position_name()
        return params_list

if __name__ == '__main__':
    pprint.pprint(GetEmployeeList().splicing_params_list())
    pass