# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_purchaseRequire_data
@time:2022/7/15
@Author:majiaqin 170479
@Desc:purchaseRequire用例实际出参和期望出参拼接
'''
from loggerUtils import MyLog
from apps.AllSystemData.PmsSystem.pms_common_setting import Pms_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list

# 实例化日志类
logger = MyLog("Test_PurchaseRequire_Data").getlog()
class Test_PurchaseRequire_Data():
    def __init__(self, resp_list):
        self.resp_list = resp_list
        logger.info(self.resp_list)

    '''获取出参数据'''
    def get_json(self):
        self.resp_json = self.resp_list[1]
        json_dict = {'result': []}
        json_list = [self.resp_json['result']]
        json_dict['result'] = json_list
        return json_dict

    '''获取期望数据'''
    def expect_json(self):
        return {'result': [None]}

    '''拼接实际出参code，实际出参和期望结果'''
    def expect_data(self):
        return [self.resp_list[0], self.get_json(), self.expect_json()]

if __name__ == '__main__':
    pass