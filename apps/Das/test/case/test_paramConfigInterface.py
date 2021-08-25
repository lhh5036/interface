'''
@File: test_paramConfigInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:参数配置保存接口用例
'''
from apps.Das.das_interface_service.param_config.parameterConfigSave import ParameterConfigInterface
import unittest

# 参数配置保存接口用例类
class Test_parameterConfigSaveInterface(unittest.TestCase):

    def test01(self):
        # 用例2接口第二个入参（单个参数）
        paramStr01 = "'test01'"
        responseResult01 = ParameterConfigInterface().paramConfigFunction("第一个用例",paramStr01)
        return responseResult01


    def test02(self):
        # 用例2接口第二个入参（多个参数）
        paramStr02 = "'test01','test02'"
        responseResult02 = ParameterConfigInterface().paramConfigFunction("第二个用例",paramStr02)
        return responseResult02





