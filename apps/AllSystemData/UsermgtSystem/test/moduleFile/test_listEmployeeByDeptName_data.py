# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_listEmployeeByDeptName_data
@time:2022/8/5
@Author:majiaqin 170479
@Desc:listEmployeeByDeptName用例实际出参和期望出参拼接
'''
from loggerUtils import MyLog
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list
from apps.utils.search_subordinate_deptid import Search_Subordinate_Deptid

# 实例化日志类
logger = MyLog("Test_ListEmployeeByDeptName_Data").getlog()
class Test_ListEmployeeByDeptName_Data():
    def __init__(self, paramMap, resp_list):
        self.paramMap = paramMap
        self.resp_list = resp_list
        logger.info(self.paramMap)
        logger.info(self.resp_list)

    '''获取出参数据'''
    def get_json(self):
        self.resp_json = self.resp_list[1]
        json_dict = {'employeeNo': []}
        try:
            json_list = [i['employeeNo'] for i in self.resp_json['result']]
        except:
            json_list = []
        json_dict['employeeNo'] = json_list
        return json_dict

    '''获取组织架构名和其下的全部组织架构id'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_deptId_list(self):
        sql = "SELECT id FROM org_struct \
WHERE org_name = '{0}';".format(self.paramMap[0])
        return sql

    '''获取期望数据'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def expect_json(self):
        deptId_list = Search_Subordinate_Deptid(self.get_deptId_list()).search_subordinate_deptid()
        if len(deptId_list) == 1:
            sql = "SELECT employee_no \
FROM employee \
WHERE dept_id_list_str = {0} \
OR dept_id = {0};".format(deptId_list[0])
        elif len(deptId_list) > 1:
            sql = "SELECT employee_no \
FROM employee \
WHERE dept_id_list_str IN {0} \
OR dept_id IN {0};".format(tuple(deptId_list))
        logger.info('获取期望数据sql: {0}'.format(sql))
        return sql

    '''拼接实际出参code，实际出参和期望结果'''
    def expect_data(self):
        if self.expect_json() == []:
            expect_dict = {'employeeNo': []}
        else:
            expect_dict = {'employeeNo': []}
            expect_dict['employeeNo'] = self.expect_json()
        logger.info(self.paramMap[0], self.get_json(), expect_dict)
        return [self.resp_list[0], self.get_json(), expect_dict]

if __name__ == '__main__':
    pass