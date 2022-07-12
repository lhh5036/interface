# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_getMenuPermissionTypes_data
@time:2022/7/12
@Author:majiaqin 170479
@Desc:getMenuPermissionTypes用例实际出参和期望出参拼接
'''
from loggerUtils import MyLog

# 实例化日志类
logger = MyLog("Test_GetMenuPermissionTypes_Data").getlog()
class Test_GetMenuPermissionTypes_Data():
    def __init__(self, paramMap, resp_list):
        self.paramMap = paramMap
        self.resp_list = resp_list
        logger.info(self.paramMap)
        logger.info(self.resp_list)

    '''获取出参数据'''
    def get_json(self):
        self.resp_json = self.resp_list[1]
        json_dict = {'code': []}
        json_list = [i['code'] for i in self.resp_json['result']]
        json_dict['code'] = json_list
        return json_dict

    '''获取期望数据'''
    def expect_json(self, code_list):
        self.code_list = code_list
        expect_json = {'code': self.code_list}
        return expect_json

    '''拼接实际出参code，实际出参和期望结果'''
    def expect_data(self, code_list):
        self.code_list = code_list
        logger.info(self.paramMap[0], self.get_json(), self.expect_json(self.code_list))
        return [self.resp_list[0], self.get_json(), self.expect_json(self.code_list)]

if __name__ == '__main__':
    pass