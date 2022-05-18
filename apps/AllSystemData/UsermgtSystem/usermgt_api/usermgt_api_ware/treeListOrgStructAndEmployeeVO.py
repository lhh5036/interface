# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: treeListOrgStructAndEmployeeVO
@time:2022/5/18
@Author:majiaqin 170479
@Desc:根据平台和工号获取级联获取员工信息（树形返回）
'''

import pprint
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list

class TreeListOrgStructAndEmployeeVOApi():
    def __init__(self):
        pass

    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_data(self):
        sql = "SELECT o.org_name, e.employee_no \
FROM employee e \
LEFT JOIN org_struct o \
ON o.id = e.dept_id \
WHERE o.org_name IS NOT NULL \
GROUP BY o.org_name \
LIMIT 10;"
        return sql

    @classmethod
    def splicing_params_list(cls):
        params_list = list(cls().get_data())
        return params_list

if __name__ == '__main__':
    pprint.pprint(TreeListOrgStructAndEmployeeVOApi().splicing_params_list())
    pass