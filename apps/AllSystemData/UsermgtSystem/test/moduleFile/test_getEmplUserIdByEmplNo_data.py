# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_getEmplUserIdByEmplNo_data
@time:2022/8/11
@Author:majiaqin 170479
@Desc:getEmplUserIdByEmplNo用例实际出参和期望出参拼接
'''
import random
from loggerUtils import MyLog
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list
from apps.utils.search_subordinate_deptid import Search_Subordinate_Deptid

# 实例化日志类
logger = MyLog("Test_GetEmplUserIdByEmplNo_Data").getlog()
class Test_GetEmplUserIdByEmplNo_Data():
    def __init__(self, paramMap, resp_list):
        self.paramMap = paramMap
        self.resp_list = resp_list
        logger.info(self.paramMap)
        logger.info(self.resp_list)

    '''获取出参数据'''
    def get_json(self):
        self.resp_json = self.resp_list[1]
        json_dict = {'dinguserId': [i for i in self.resp_json['result']]}
        return json_dict

    '''获取期望数据'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def expect_json(self):
        sql = "SELECT ding_user_id FROM employee \
WHERE employee_no IN {0} \
OR employee_id IN {1};".format(tuple(self.paramMap[0]), tuple(self.paramMap[1]))
        return sql

    '''拼接实际出参code，实际出参和期望结果'''
    def expect_data(self):
        expect_dict = {'dinguserId': self.expect_json()}
        logger.info(self.resp_list[0], self.get_json(), expect_dict)
        return [self.resp_list[0], self.get_json(), expect_dict]

if __name__ == '__main__':
    pass