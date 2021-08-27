'''
@File: test_paramConfigQueryApi.py
@time:2021/8/23
@Author:quanliu
@Desc:参数配置-取消开发备注查询用例
'''

import unittest


from apps.Das.das_interface_service.param_config.parameterConfigSelectApi import ParameterConfigQueryApi

# 参数配置-取消开发备注查询用例类
class Test_paramConfigQueryApi(unittest.TestCase):

    def testCase01(self):
        responseResult01 = ParameterConfigQueryApi().paramConfigQuery()
        print(responseResult01)

