'''
@File: test_paramConfigInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:参数配置保存接口用例
'''
from apps.Das.das_interface_service.param_config.parameterConfigSave import ParameterConfigInterface


def test_parameterConfigSaveInterface():

    responseResult = []
    # 用例1接口第二个入参（单个参数）
    paramStr01 = "'test01'"
    responseResult01 = ParameterConfigInterface().paramConfigFunction("第一个用例",paramStr01)
    responseResult.append(responseResult01)



    #用例2接口第二个入参（多个参数）
    paramStr02 = "'test01','test02'"
    responseResult02 = ParameterConfigInterface().paramConfigFunction("第二个用例",paramStr02)
    responseResult.append(responseResult02)


    return responseResult


