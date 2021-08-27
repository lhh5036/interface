'''
@File: test_paramConfigQueryInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:参数配置-取消开发备注查询用例
'''
from apps.Das.das_interface_service.param_config.parameterConfigSelectApi import ParameterConfigQueryInterface
import unittest

# 参数配置-取消开发备注查询用例类
class Test_paramConfigQuery(unittest.TestCase):

    def testCase01(self):
        responseResult01 = ParameterConfigQueryInterface().paramConfigQuery()
        print(responseResult01)

