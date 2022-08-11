# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_listEmployeeByDeptName
@time:2022/8/5
@Author:majiaqin 170479
@Desc:listEmployeeByDeptName接口测试用例
'''
import random
import unittest
from loggerUtils import MyLog
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgt_api_ware.listEmployeeByDeptName import listEmployeeByDeptNameApi
from apps.AllSystemData.UsermgtSystem.test.moduleFile.test_listEmployeeByDeptName_data import Test_ListEmployeeByDeptName_Data
from apps.utils.assert_new_utils import new_assert_utils
# 实例化日志类
logger = MyLog("Test_ListEmployeeByDeptNameApi").getlog()
class Test_ListEmployeeByDeptNameApi(unittest.TestCase):
    '''获取入参数据'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_paramMap(self):
        num = random.randint(1, 350)
        sql = "SELECT org_name FROM org_struct \
LIMIT {0}, 1;".format(num)
        return sql

    def get_ready_data(self):
        self.paramMap = self.get_paramMap()
        self.resp = listEmployeeByDeptNameApi({"args": self.paramMap[0]})
        self.data_list = Test_ListEmployeeByDeptName_Data(self.paramMap, self.resp).expect_data()
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