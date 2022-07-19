# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_blackedBuyerApi
@time:2022/7/19
@Author:majiaqin 170479
@Desc:blackedBuyer接口测试用例
'''
import random
import unittest
from loggerUtils import MyLog
from apps.AllSystemData.SaleSystem.sale_common_setting import Sale_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list
from apps.AllSystemData.SaleSystem.sale_api.basicData.blackedBuyerApi import blackedBuyerApi
from apps.AllSystemData.SaleSystem.test.moduleFile.test_blackedBuyer_data import Test_BlackedBuyer_Data
from apps.utils.assert_new_utils import new_assert_utils

# 实例化日志类
logger = MyLog("Test_blackedBuyerApi").getlog()
class Test_blackedBuyerApi(unittest.TestCase):
    '''获取符合入参条件的数据数量'''
    @convert_list
    @get_data(Sale_Common_Setting.sale_mysql)
    def get_num(self):
        sql = "SELECT COUNT(1) \
    FROM blacked_buyer_record \
    WHERE account_number IS NOT NULL \
    AND account_number != '' \
    AND recipient_name IS NOT NULL \
    AND recipient_name != '';"
        return sql

    '''获取入参数据'''
    @convert_list
    @get_data(Sale_Common_Setting.sale_mysql)
    def get_params(self):
        self.num = random.randint(1, self.get_num()[0]-1)
        sql = "SELECT sale_channel, account_number, customer_name, \
blacked_type, recipient_name \
FROM blacked_buyer_record \
WHERE account_number IS NOT NULL \
AND account_number != '' \
AND recipient_name IS NOT NULL \
AND recipient_name != '' \
LIMIT {0}, 1;".format(self.num)
        return sql

    def get_ready_data(self):
        self.params_list = self.get_params()
        logger.info("获取入参数据: {0}".format(self.params_list))
        self.paramMap = {"saleChannel": self.params_list[0],
                         "accountNumber": self.params_list[1],
                         "customerName": self.params_list[2],
                         "blackedType": self.params_list[3],
                         "recipientName": self.params_list[4]}
        self.resp = blackedBuyerApi(self.paramMap)
        self.data_list = Test_BlackedBuyer_Data(self.paramMap, self.resp).expect_data(self.params_list)
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