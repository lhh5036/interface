# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_getEmplUserIdByEmplNo
@time:2022/8/11
@Author:majiaqin 170479
@Desc:getEmplUserIdByEmplNo接口测试用例
'''
import random
import unittest
from loggerUtils import MyLog
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgt_api_ware.getEmplUserIdByEmplNo import getEmplUserIdByEmplNoApi
from apps.AllSystemData.UsermgtSystem.test.moduleFile.test_getEmplUserIdByEmplNo_data import Test_GetEmplUserIdByEmplNo_Data
from apps.utils.assert_new_utils import new_assert_utils
# 实例化日志类
logger = MyLog("Test_GetEmplUserIdByEmplNoApi").getlog()
class Test_GetEmplUserIdByEmplNoApi(unittest.TestCase):
    '''获取入参数据员工id和员工工号'''
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_employee_info(self):
        num01 = random.randint(1, 3000)
        num02 = random.randint(1, 10)
        sql = "SELECT employee_no, employee_id \
    FROM employee \
    LIMIT {0}, {1}".format(num01, num02)
        return sql

    def get_ready_data(self):
        employee_info_list = self.get_employee_info()
        self.paramMap = [[i[0] for i in employee_info_list], [i[1] for i in employee_info_list]]
        self.resp = getEmplUserIdByEmplNoApi({"idList": self.paramMap[1],
                                              "employeeNoList": self.paramMap[0]})
        self.data_list = Test_GetEmplUserIdByEmplNo_Data(self.paramMap, self.resp).expect_data()
        return self.data_list

    @new_assert_utils
    def testCase01(self):
        '''返回数据list'''
        ready_data_list = self.get_ready_data()
        resp_list = [ready_data_list[0], ready_data_list[1]]
        '''期望数据list'''
        expect_list = [200, ready_data_list[2]]
        logger.info('返回数据list: {0}'.format(resp_list))
        logger.info('期望数据list: {0}'.format(expect_list))
        return resp_list, expect_list

if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass