# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_threeLevelEmployee_data
@time:2022/6/23
@Author:majiaqin 170479
@Desc:threeLevelEmployee用例数据准备
'''

import random
import pprint
from loggerUtils import MyLog
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgt_api_ware.threeLevelEmployee import threeLevelEmployeeApi
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list
from apps.utils.search_subordinate_deptid import Search_Subordinate_Deptid

# 实例化日志类
logger = MyLog("Test_ThreeLevelEmployee_Data").getlog()
class Test_ThreeLevelEmployee_Data():
    def __init__(self):
        self.paramMap = list(self.get_paramMap())[random.randint(0, len(list(self.get_paramMap())) - 1)]
        logger.info(self.paramMap)

    def get_resp(self):
        self.resp = threeLevelEmployeeApi({"servicePlatform": self.paramMap[1],
                                           "employeeNo": self.paramMap[0]})
        return self.resp

    '''获取入参数据'''
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_paramMap(self):
        sql = "SELECT employee_no, service_platform \
FROM employee \
WHERE service_platform IS NOT NULL \
AND service_platform NOT LIKE '%,%' \
GROUP BY service_platform \
LIMIT 10;"
        logger.info(sql)
        return sql

    '''获取出参数据'''
    def get_json(self):
        self.resp_json = self.get_resp()[1]
        json_dict = {'employeeNo': []}
        json_list = [employeeNo['employeeNo'] for employeeNo in self.resp_json['result']['employeeList']] + \
                    [employeeNo['employeeNo'] for employeeNo in self.resp_json['result']['groupList']] + \
                    [employeeNo['employeeNo'] for employeeNo in self.resp_json['result']['leaderList']]
        json_dict['employeeNo'] = json_list
        return json_dict

    '''获取employeeNo所在的组织架构'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_employeeNo_deptid(self):
        sql = "SELECT id FROM org_struct \
WHERE employee_no = {0};".format(self.paramMap[0])
        return sql

    '''获取期望数据'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def expect_json(self):
        # 获取用户对应deptid和下级所有deptid
        deptid_tuple = tuple(Search_Subordinate_Deptid(self.get_employeeNo_deptid()).search_subordinate_deptid())
        print(deptid_tuple)
        sql = "SELECT employee_no FROM employee \
WHERE service_platform LIKE '%{0}%' \
AND dept_id in {1};".format(self.paramMap[1], deptid_tuple)
        logger.info(sql)
        return sql

    def expect_data(self):
        expect_dict = {'employeeNo': []}
        if self.expect_json() == 0:
            expect_dict['employeeNo'] = [self.paramMap[0]]
        else:
            expect_dict['employeeNo'] = self.expect_json()
        return [self.get_resp()[0], self.get_json(), expect_dict]


if __name__ == '__main__':
    pprint.pprint(Test_ThreeLevelEmployee_Data().expect_data())
    pass