# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_getEmployeesByRoleName_data
@time:2022/7/12
@Author:majiaqin 170479
@Desc:getEmployeesByRoleName用例实际出参和期望出参拼接
'''
from loggerUtils import MyLog
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list

# 实例化日志类
logger = MyLog("Test_GetEmployeesByRoleName_Data").getlog()
class Test_GetEmployeesByRoleName_Data():
    def __init__(self, paramMap, resp_list):
        self.paramMap = paramMap
        self.resp_list = resp_list
        logger.info(self.paramMap)
        logger.info(self.resp_list)

    '''获取出参数据'''
    def get_json(self):
        self.resp_json = self.resp_list[1]
        json_dict = {'employeeId': []}
        json_list = [i['employeeId'] for i in self.resp_json['result']]
        json_dict['employeeId'] = json_list
        return json_dict

    '''获取角色名下的工号'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_employeeId_by_rolename(self, rolename):
        self.rolename = rolename
        sql = "SELECT rer.employee_id \
FROM rs_employee_role rer \
LEFT JOIN employee e \
ON e.employee_id = rer.employee_id \
LEFT JOIN role r \
ON r.id = rer.role_id \
WHERE r.role_name = '{0}';".format(self.rolename)
        return sql

    '''拼接实际出参code，实际出参和期望结果'''
    def expect_data(self, rolename):
        self.rolename = rolename
        employeeId_list = self.get_employeeId_by_rolename(self.rolename)
        expect_dict = {'employeeId': employeeId_list}
        logger.info(self.paramMap[0], self.get_json(), expect_dict)
        return [self.resp_list[0], self.get_json(), expect_dict]

if __name__ == '__main__':
    pass