# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_getSmtSellerAccount
@time:2022/7/13
@Author:majiaqin 170479
@Desc:getSmtSellerAccount接口测试用例
'''

import unittest
from loggerUtils import MyLog
from apps.AllSystemData.FmisSystem.fmis_api.performance_manage.getSmtSellerAccount import getSmtSellerAccountApi
from apps.AllSystemData.FmisSystem.test.moduleFile.test_getSmtSellerAccount_data import Test_GetSmtSellerAccount_Data
from apps.utils.assert_new_utils import new_assert_utils
# 实例化日志类
logger = MyLog("Test_GetSmtSellerAccount").getlog()
class Test_GetSmtSellerAccount(unittest.TestCase):
    def get_ready_data(self):
        self.resp = getSmtSellerAccountApi()
        self.data_list = Test_GetSmtSellerAccount_Data(self.resp).expect_data()
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