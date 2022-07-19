# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_tariffCountry_data
@time:2022/7/18
@Author:majiaqin 170479
@Desc:tariffCountry用例实际出参和期望出参拼接
'''
import random
from loggerUtils import MyLog
from apps.AllSystemData.SaleSystem.sale_common_setting import Sale_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list

# 实例化日志类
logger = MyLog("Test_TariffCountry_Data").getlog()
class Test_TariffCountry_Data():
    def __init__(self, paramMap, resp_list):
        self.paramMap = paramMap
        self.resp_list = resp_list
        self.name_list = ['chineseName', 'name']
        logger.info(self.paramMap)
        logger.info(self.resp_list)

    '''获取出参数据'''
    def get_json(self, name):
        self.name = name
        self.resp_json = self.resp_list[1]
        json_dict = {'name': []}
        if self.name == 'name':
            json_list = [i['name'] for i in self.resp_json['rows']]
        elif self.name == 'chineseName':
            json_list = [i['chineseName'] for i in self.resp_json['rows']]
        json_dict['name'] = json_list
        return json_dict

    '''获取期望出参数据'''
    @convert_list
    @get_data(Sale_Common_Setting.sale_mysql)
    def get_except_name(self, name, name_params):
        self.name = name
        self.name_params = name_params
        if self.name == 'name':
            sql = "SELECT name FROM country \
WHERE name = '{0}';".format(self.name_params)
        elif self.name == 'chineseName':
            sql = "SELECT chinese_name FROM country \
WHERE chinese_name = '{0}';".format(self.name_params)
        return sql

    '''拼接实际出参code，实际出参和期望结果'''
    def expect_data(self, name, name_params):
        self.name = name
        self.name_params = name_params
        expect_dict = {'name': self.get_except_name(self.name, self.name_params)}
        return [self.resp_list[0], self.get_json(self.name), expect_dict]

if __name__ == '__main__':
    pass