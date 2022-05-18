# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: employee
@time:2022/5/18
@Author:majiaqin 170479
@Desc:获取页面数据权限
'''
import random
import pprint
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list

class EmployeeApi():
    def __init__(self):
        pass

    '''获取接口入参方法'''
    def get_method(self):
        method_list = ["getOpEmployee",
                       "getCreaterAndOEmployee",
                       "getUserForGoodsSource",
                       "getPurchaserAndProducter"]
        return method_list

    '''获取员工,菜单数据'''
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_data(self):
        sql = "SELECT e.employee_no, rrm.menu_code \
FROM employee e \
LEFT JOIN rs_employee_role rer \
ON rer.employee_id = e.employee_id \
LEFT JOIN rs_role_menu rrm \
ON rrm.role_id = rer.role_id \
GROUP BY e.employee_no \
LIMIT 10;"
        return sql

    @classmethod
    def splicing_params_list(cls):
        params = cls().get_data()[random.randint(0, len(cls().get_data())-1)]
        params_list = list(params)
        params_list.append(cls().get_method()[random.randint(0, len(cls().get_method())-1)])
        return params_list

if __name__ == '__main__':
    pprint.pprint(EmployeeApi().splicing_params_list())
    pass