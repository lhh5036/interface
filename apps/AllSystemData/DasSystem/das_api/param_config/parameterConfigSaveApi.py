'''
@File: parameterConfigSaveApi.py
@time:2021/8/23
@Author:quanliu
@Desc:数据分析-参数配置页面接口服务
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app


# 参数配置页面接口服务
@api_assemble_new()
def paramConfigFunction(paramStr):
    app.logger.info("paramConfigFunction ---->start!")
    if paramStr == "":
        app.logger.error("paramConfigFunction --> request parameters is wrong!")
        return "请求参数为空"

    # 接口地址
    url = DasApiUrl.paramConfigSave_url
    # 拼接接口请求入参
    reqSelect = DasApiInputParam.paramConfig_select
    reqSelectStr = reqSelect.replace("{notesInfoList}", paramStr)  # 替换参数
    reqParam = DasApiInputParam.paramConfig_param
    reqParam["args"] = reqSelectStr
    return url,reqParam