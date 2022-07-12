# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_getMenuPermissionTypes
@time:2022/7/12
@Author:majiaqin 170479
@Desc:getMenuPermissionTypes接口测试用例
'''
import random
import unittest
from loggerUtils import MyLog
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgt_api_ware.getMenuPermissionTypes import getMenuPermissionTypesApi
from apps.AllSystemData.UsermgtSystem.test.moduleFile.test_getMenuPermissionTypes_data import Test_GetMenuPermissionTypes_Data

# 实例化日志类
logger = MyLog("Test_GetMenuPermissionTypesApi").getlog()
class Test_GetMenuPermissionTypesApi(unittest.TestCase):
    '''获取入参code数据'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_menucode(self):
        self.num = random.randint(1, 5000)
        sql = "SELECT code FROM menu_permission \
    LIMIT {0}, 5;".format(self.num)
        return sql

    def get_ready_data(self):
        self.paramMap = self.get_menucode()
        self.resp = getMenuPermissionTypesApi({'employeeNo': '170479',
                                               'codes': self.paramMap})
        self.data_list = Test_GetMenuPermissionTypes_Data(self.paramMap, self.resp).expect_data(self.paramMap)
        return self.data_list

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