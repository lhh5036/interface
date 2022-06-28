# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_superByEmpNo_data
@time:2022/6/27
@Author:majiaqin 170479
@Desc:superByEmpNo用例实际出参和期望出参拼接
'''
from loggerUtils import MyLog
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list
from apps.utils.search_subordinate_deptid import Search_Subordinate_Deptid
# 实例化日志类
logger = MyLog("Test_SuperByEmpNo_Data").getlog()
class Test_SuperByEmpNo_Data():
    def __init__(self, paramMap, resp_list):
        self.paramMap = paramMap
        self.resp_list = resp_list
        logger.info(self.paramMap)
        logger.info(self.resp_list)

    '''获取出参数据'''
    def get_json(self):
        self.resp_json = self.resp_list[1]
        json_dict = {'superEmployeeNo': []}
        json_list = [self.resp_json['result']['superEmployeeNo']]
        json_dict['superEmployeeNo'] = json_list
        return json_dict

    '''获取员工的组织架构id'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_employee_deptId(self):
        sql = "SELECT dept_id \
FROM employee \
WHERE employee_no = '{0}';".format(self.paramMap[0])
        return sql

    '''获取某个工号的上级工号'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_superEmployeeNo(self, deptId):
        self.deptId = deptId
        sql = "SELECT os.employee_no \
FROM employee e \
LEFT JOIN org_struct os \
ON os.id = e.dept_id \
WHERE e.dept_id = '{0}';".format(self.deptId)
        return sql

    '''获取期望数据'''
    def expect_json(self):
        expect_dict = {}
        deptid_list = Search_Subordinate_Deptid(self.get_employee_deptId()).search_subordinate_superdeptid()
        for i in deptid_list:
            if list(set(self.get_superEmployeeNo(i))) == [None]:
                continue
            else:
                expect_dict['superEmployeeNo'] = list(set(self.get_superEmployeeNo(i)))
                break
        return expect_dict

    '''拼接实际出参code，实际出参和期望结果'''
    def expect_data(self):
        expect_dict = self.expect_json()
        if expect_dict['superEmployeeNo'] == 0:
            logger.error('入参账号所在的组织架构及所有上级组织架构均未配置部门主管')
            return '入参账号所在的组织架构及所有上级组织架构均未配置部门主管'
        else:
            logger.info(self.paramMap[0], self.get_json(), expect_dict)
            return [self.resp_list[0], self.get_json(), expect_dict]

if __name__ == '__main__':
    pass