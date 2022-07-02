# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_threeLevelEmployee
@time:2022/6/23
@Author:majiaqin 170479
@Desc:threeLevelEmployee接口测试用例
'''
import random
import unittest
from loggerUtils import MyLog
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgt_api_ware.threeLevelEmployee import threeLevelEmployeeApi
from apps.AllSystemData.UsermgtSystem.test.moduleFile.test_threeLevelEmployee_data import Test_ThreeLevelEmployee_Data
from apps.utils.assert_new_utils import new_assert_utils
# 实例化日志类
logger = MyLog("Test_ThreeLevelEmployeeApi").getlog()
class Test_ThreeLevelEmployeeApi(unittest.TestCase):
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

    def get_ready_data(self):
        self.paramMap = list(self.get_paramMap())[random.randint(0, len(list(self.get_paramMap())) - 1)]
        self.resp = threeLevelEmployeeApi({"servicePlatform": self.paramMap[1],
                                           "employeeNo": self.paramMap[0]})
        self.data_list = Test_ThreeLevelEmployee_Data(self.paramMap, self.resp).expect_data()
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