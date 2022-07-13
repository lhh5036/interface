# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_getOaccountCodeAndNames_data
@time:2022/7/13
@Author:majiaqin 170479
@Desc:getOaccountCodeAndNames用例实际出参和期望出参拼接
'''

from loggerUtils import MyLog
from apps.AllSystemData.FmisSystem.fmis_common_settting import Fmis_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list

# 实例化日志类
logger = MyLog("Test_GetOaccountCodeAndNames_Data").getlog()
class Test_GetOaccountCodeAndNames_Data():
    def __init__(self, resp_list):
        self.resp_list = resp_list
        logger.info(self.resp_list)

    '''获取出参数据'''
    def get_json(self):
        self.resp_json = self.resp_list[1]
        json_dict = {'oaccountName': []}
        json_list = [i['oaccountName'] for i in self.resp_json['result']]
        json_dict['oaccountName'] = json_list
        return json_dict

    '''获取期望数据'''
    @convert_list
    @get_data(Fmis_Common_Setting.fmis_mysql)
    def expect_json(self):
        sql = "SELECT DISTINCT oaccount_name \
FROM payment_record \
WHERE oaccount_name IS NOT NULL;"
        return sql

    '''拼接实际出参code，实际出参和期望结果'''
    def expect_data(self):
        expect_dict = {'oaccountName': self.expect_json()}
        return [self.resp_list[0], self.get_json(), expect_dict]

if __name__ == '__main__':
    pass