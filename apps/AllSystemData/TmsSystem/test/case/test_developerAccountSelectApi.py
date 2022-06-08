'''
@File: test_developerAccountSelectApi.py
@time:2022/6/8
@Author:quanliu 181324
@Desc:物流配置-管理开发者账号
'''
import unittest
from apps.AllSystemData.TmsSystem.tms_api.logisticsEngineConfig.developerAccountSelectApi import \
    developerAccountSelectApi


class Test_developerAccountSelectApi(unittest.TestCase):

    def testCase01(self):
        '''管理开发者账号-查询'''
        responseResult01 = developerAccountSelectApi({})
        print(responseResult01)

