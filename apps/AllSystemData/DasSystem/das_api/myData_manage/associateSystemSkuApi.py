'''
@File: associateSystemSkuApi.py
@time:2021/8/20
@Author:quanliu 181324
@Desc:我的数据-Amazon关联系统SKU接口
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from loggerUtils import MyLog

# 关联系统SKU接口
logger = MyLog("associateSystemSku").getlog()
@api_assemble_new()
def associateSystemSku(platform, searchType, paramList, systemSkuStr):
    logger.info("associateSystemSku ---->start!")
    if len(paramList) == 0 or systemSkuStr == "" or searchType == "" or platform == "":
        logger.error("associateSystemSku --> request parameters is wrong!")
        return "请求参数为空"
    # 将入参list转为string类型
    paramStr = ""
    for i in range(len(paramList)):
        paramStr += "'" + paramList[i] + "',"
    # 拼接接口请求入参
    reqSelect = DasApiInputParam.associateSySku_select
    reqSelect["ids"] = paramList
    reqSelect["systemSku"] = systemSkuStr
    reqParam = DasApiInputParam.associateSySku_param
    reqParam["args"] = str(reqSelect)
    url = PublicCommonUrlServiceClass().getApiUrl(platform, searchType) # 接口地址
    return url,reqParam # 返回接口的地址和接口参数