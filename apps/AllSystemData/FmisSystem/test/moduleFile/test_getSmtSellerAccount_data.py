# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_getSmtSellerAccount_data
@time:2022/7/13
@Author:majiaqin 170479
@Desc:getSmtSellerAccount用例实际出参和期望出参拼接
'''
from loggerUtils import MyLog
from apps.AllSystemData.SaleSystem.sale_common_setting import Sale_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list

# 实例化日志类
logger = MyLog("Test_GetSmtSellerAccount_Data").getlog()
class Test_GetSmtSellerAccount_Data():
    def __init__(self, resp_list):
        self.resp_list = resp_list
        logger.info(self.resp_list)

    '''获取出参数据'''
    def get_json(self):
        self.resp_json = self.resp_list[1]
        json_dict = {'account': []}
        json_list = self.resp_json['result']
        json_dict['account'] = json_list
        return json_dict

    '''获取期望数据'''
    @convert_list
    @get_data(Sale_Common_Setting.sale_mysql)
    def expect_json(self):
        sql = "SELECT account_number \
FROM sale_account \
WHERE sale_channel = 'SMT';"
        return sql

    '''拼接实际出参code，实际出参和期望结果'''
    def expect_data(self):
        expect_dict = {'account': self.expect_json()}
        return [self.resp_list[0], self.get_json(), expect_dict]

if __name__ == '__main__':
    pass