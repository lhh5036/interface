# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_blackedBuyer_data
@time:2022/7/19
@Author:majiaqin 170479
@Desc:blackedBuyer用例实际出参和期望出参拼接
'''
import random
from loggerUtils import MyLog
from apps.AllSystemData.SaleSystem.sale_common_setting import Sale_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list

# 实例化日志类
logger = MyLog("Test_BlackedBuyer_Data").getlog()
class Test_BlackedBuyer_Data():
    def __init__(self, paramMap, resp_list):
        self.paramMap = paramMap
        self.resp_list = resp_list
        logger.info(self.paramMap)
        logger.info(self.resp_list)

    '''获取出参数据'''
    def get_json(self):
        self.resp_json = self.resp_list[1]['rows']
        json_dict = {"saleChannel": [i['saleChannel'] for i in self.resp_json],
                     "accountNumber": [i['accountNumber'] for i in self.resp_json],
                     "customerName": [i['customerName'] for i in self.resp_json],
                     "blackedType": [i['blackedType'] for i in self.resp_json],
                     "recipientName": [i['recipientName'] for i in self.resp_json]}
        return json_dict

    '''获取期望出参数据'''
    @convert_list
    @get_data(Sale_Common_Setting.sale_mysql)
    def get_except(self, params_list):
        self.params_list = params_list
        sql = "SELECT sale_channel, account_number, customer_name, \
blacked_type, recipient_name \
FROM blacked_buyer_record \
WHERE sale_channel = '{0}' \
AND account_number = '{1}' \
AND customer_name = '{2}' \
AND blacked_type = '{3}' \
AND recipient_name = '{4}';".format(*self.params_list)
        return sql

    '''拼接实际出参code，实际出参和期望结果'''
    def expect_data(self, params_list):
        self.params_list = params_list
        self.except_list = self.get_except(self.params_list)
        expect_dict = {"saleChannel": [self.except_list[0]],
                       "accountNumber": [self.except_list[1]],
                       "customerName": [self.except_list[2]],
                       "blackedType": [self.except_list[3]],
                       "recipientName": [self.except_list[4]]}
        return [self.resp_list[0], self.get_json(), expect_dict]

if __name__ == '__main__':
    pass