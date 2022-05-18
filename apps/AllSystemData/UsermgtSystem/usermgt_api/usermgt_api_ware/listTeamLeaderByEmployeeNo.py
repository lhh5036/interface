# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: listTeamLeaderByEmployeeNo
@time:2022/5/17
@Author:majiaqin 170479
@Desc:判断员工是否为负责人,返回相关员工信息
'''

import pprint
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list

class ListTeamLeaderByEmployeeNoApi():
    def __init__(self):
        pass

    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_data(self):
        sql = "SELECT employee_no, service_platform \
FROM employee \
WHERE service_platform IS NOT NULL \
GROUP BY service_platform \
LIMIT 10;"
        return sql

    @classmethod
    def splicing_params_list(cls):
        params_list = list(cls().get_data())
        return params_list

if __name__ == '__main__':
    pprint.pprint(ListTeamLeaderByEmployeeNoApi().splicing_params_list())
    pass