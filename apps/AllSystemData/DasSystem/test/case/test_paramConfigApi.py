'''
@File: test_paramConfigApi.py
@time:2021/8/23
@Author:quanliu
@Desc:参数配置保存接口用例
'''

import unittest
from apps.AllSystemData.DasSystem.das_api.param_config.parameterConfigSaveApi import paramConfigFunction

# 参数配置保存接口用例类
class Test_parameterConfigSaveApi(unittest.TestCase):

    def testCase01(self):
        # 用例2接口第二个入参（单个参数）
        '''这是第一个用例'''
        paramStr01 = "'test01'"
        responseResult01 = paramConfigFunction(paramStr01)
        print(responseResult01)


    def testCase02(self):
        # 用例2接口第二个入参（多个参数）
        '''这是第二个用例'''
        paramStr02 = "'test01','test02'"
        responseResult02 = paramConfigFunction(paramStr02)
        print(responseResult02)

if __name__ == '__main__':
    unittest.main(verbosity=2)




