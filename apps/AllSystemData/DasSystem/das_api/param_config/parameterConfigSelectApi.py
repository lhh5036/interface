'''
@File: parameterConfigSelectApi.py
@time:2021/8/23
@Author:quanliu
@Desc:参数配置-取消开发备注查询接口服务
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from loggerUtils import MyLog

logger = MyLog("paramConfigQuery").getlog()
@api_assemble_new()
def paramConfigQuery():
    logger.info("paramConfigQuery ---->start!")
    # 接口地址
    url = DasApiUrl.paramConfigSelect_url
    # 接口请求参数
    formData = DasApiInputParam.paramConfigQuery
    return url,formData
