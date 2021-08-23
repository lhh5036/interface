'''
@File: test_paramConfigQueryInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:参数配置-取消开发备注查询用例
'''
from apps.Das.das_interface_service.param_config.parameterConfigSelect import ParameterConfigQueryInterface


def test_paramConfigQuery():

    responseResult = []
    # 第一个用例
    responseResult01 = ParameterConfigQueryInterface().paramConfigQuery("第一个用例")
    responseResult.append(responseResult01)

    return responseResult


