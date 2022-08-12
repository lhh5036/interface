# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_getEmployeesByRoleIds_data
@time:2022/8/12
@Author:majiaqin 170479
@Desc:getEmployeesByRoleIds用例实际出参和期望出参拼接
'''
from loggerUtils import MyLog
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list

# 实例化日志类
logger = MyLog("Test_GetEmployeesByRoleIds_Data").getlog()
class Test_GetEmployeesByRoleIds_Data():
    def __init__(self, paramMap, resp_list):
        self.paramMap = paramMap
        self.resp_list = resp_list
        logger.info(self.paramMap)
        logger.info(self.resp_list)

    '''获取出参数据'''
    def get_json(self):
        self.resp_json = self.resp_list[1]
        json_dict = {'employeeId': [i['employeeId'] for i in self.resp_json['result']]}
        return json_dict

    '''获取期望数据'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def expect_json(self):
        sql = "SELECT employee_id FROM rs_employee_role \
WHERE role_id = '{0}';".format(self.paramMap)
        return sql

    '''拼接实际出参code，实际出参和期望结果'''
    def expect_data(self):
        expect_dict = {'employeeId': []}
        if self.expect_json() == 0:
            expect_dict['employeeNo'] = []
        else:
            expect_dict['employeeNo'] = self.expect_json()
        logger.info(self.resp_list[0], self.get_json(), expect_dict)
        return [self.resp_list[0], self.get_json(), expect_dict]

if __name__ == '__main__':
    pass