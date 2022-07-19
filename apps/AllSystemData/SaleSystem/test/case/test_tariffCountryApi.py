# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_tariffCountryApi
@time:2022/7/18
@Author:majiaqin 170479
@Desc:tariffCountry接口测试用例
'''
import random
import unittest
from loggerUtils import MyLog
from apps.AllSystemData.SaleSystem.sale_common_setting import Sale_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list
from apps.AllSystemData.SaleSystem.sale_api.basicData.tariffCountryApi import tariffCountryApi
from apps.AllSystemData.SaleSystem.test.moduleFile.test_tariffCountry_data import Test_TariffCountry_Data
from apps.utils.assert_new_utils import new_assert_utils

# 实例化日志类
logger = MyLog("Test_TariffCountryApi").getlog()
class Test_TariffCountryApi(unittest.TestCase):
    '''获取入参数据'''
    @convert_list
    @get_data(Sale_Common_Setting.sale_mysql)
    def get_params(self, name):
        self.name = name
        self.num = random.randint(1, 300)
        if self.name == 'name':
            sql = "SELECT name FROM country \
LIMIT {0}, 1;".format(self.num)
        elif self.name == 'chineseName':
            sql = "SELECT chinese_name FROM country \
LIMIT {0}, 1;".format(self.num)
        return sql

    def get_ready_data(self):
        self.name_list = ['chineseName', 'name']
        name = self.name_list[random.randint(0, len(self.name_list) - 1)]
        self.paramMap = self.get_params(name)
        self.resp = tariffCountryApi({"name": name,
                                      "inputText": self.paramMap[0]})
        self.data_list = Test_TariffCountry_Data(self.paramMap, self.resp).expect_data(name, self.paramMap[0])
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