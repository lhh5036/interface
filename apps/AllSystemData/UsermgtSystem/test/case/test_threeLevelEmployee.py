# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_threeLevelEmployee
@time:2022/6/23
@Author:majiaqin 170479
@Desc:threeLevelEmployee接口测试用例
'''

import unittest
from loggerUtils import MyLog
from apps.AllSystemData.UsermgtSystem.test.moduleFile.test_threeLevelEmployee_data import Test_ThreeLevelEmployee_Data
from apps.utils.assert_new_utils import new_assert_utils
# 实例化日志类
logger = MyLog("Test_ThreeLevelEmployeeApi").getlog()
class Test_ThreeLevelEmployeeApi(unittest.TestCase):
    def get_ready_data(self):
        self.data_list = Test_ThreeLevelEmployee_Data().expect_data()
        return self.data_list

    @new_assert_utils
    def testCase01(self):
        '''返回数据list'''
        resp_list = [self.get_ready_data()[0], self.get_ready_data()[1]]
        '''期望数据list'''
        expect_list = [200, self.get_ready_data()[2]]
        logger.info('返回数据list: {0}'.format(resp_list))
        logger.info('期望数据list: {0}'.format(expect_list))
        return resp_list, expect_list

if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass