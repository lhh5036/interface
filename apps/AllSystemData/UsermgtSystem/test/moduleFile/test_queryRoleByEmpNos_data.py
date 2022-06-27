# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_queryRoleByEmpNos_data
@time:2022/6/24
@Author:majiaqin 170479
@Desc:queryRoleByEmpNos接口入参数据准备
'''

import pprint
import random
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list

class Get_Params():
    def __init__(self):
        self.num = random.randint(20, 50)

    '''获取员工工号'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_employeeNo(self):
        self.sql = "SELECT employee_no FROM employee LIMIT {0},40;".format(self.num)
        return self.sql

    '''获取员工对应的角色id'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_roleId(self, employeeNo_tuple):
        self.employeeNo_tuple = employeeNo_tuple
        self.sql = "SELECT rer.role_id \
FROM rs_employee_role rer \
LEFT JOIN employee e \
ON e.employee_id = rer.employee_id \
WHERE e.employee_no in {0};".format(self.employeeNo_tuple)
        return self.sql

if __name__ == '__main__':
    pprint.pprint(Get_Params().get_roleId(tuple(Get_Params().get_employeeNo())))