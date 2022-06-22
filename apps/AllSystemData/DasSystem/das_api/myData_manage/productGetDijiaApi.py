'''
@File: productGetDijiaApi.py
@time:2021/8/23
@Author:quanliu
@Desc:低价接口服务
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from loggerUtils import MyLog

logger = MyLog("productDetDiJia").getlog()
# 数据管理-低价接口
@api_assemble_new()
def productDetDiJia(paramStr): # 请求入参为用例名称，string类型的参数
    logger.info("productGenDijia ---->start!")
    if paramStr == "":
        logger.error("productGenDijia --> ReqParam:paramStr is null!")
        return "请求入参不能为空!"
    # 接口请求地址
    url = DasApiUrl.productGenDijia_url
    # 拼接接口请求入参
    paramSelect = DasApiInputParam.productGenDijia_select
    paramSelect["asinUrlStr"] = paramStr
    reqParam = DasApiInputParam.productGenDijia_param
    reqParam["args"] = str(paramSelect) # 替换最外层参数
    return url,reqParam