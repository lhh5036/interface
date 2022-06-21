'''
@File: releaseProductApi.py
@time:2021/8/7
@Author:quanliu 181324
@Desc:我的数据Amazon-释放产品接口
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from loggerUtils import MyLog

logger = MyLog("releaseProductInfo").getlog()
# 我的数据Amazon-释放产品接口
@api_assemble_new()
def releaseProductInfo(platform,searchType,paramList): # 调用该接口使用入参为list
    paramStr = ""
    logger.info("releaseProductInfo ---->start!")
    if len(paramList) == 0:
        logger.error("releaseProductInfo --> request parameters is wrong!")
        return "请求参数为空"

    # 将入参list转为string类型
    for i in range(len(paramList)):
        paramStr += "'"+paramList[i]+"',"
    # 拼接接口请求入参
    reqSelect = DasApiInputParam.releaseProductInfo_select
    reqSelect["ids"] = paramList
    reqParam = DasApiInputParam.releaseProductInfo_param
    reqParam["args"] = str(reqSelect)
    # 组装接口所需要的参数
    url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
    return url,reqParam