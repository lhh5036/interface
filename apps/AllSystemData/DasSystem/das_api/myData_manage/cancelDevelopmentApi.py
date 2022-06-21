'''
@File: cancelDevelopmentApi.py
@time:2021/8/23
@Author:quanliu
@Desc:取消开发接口服务
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from loggerUtils import MyLog

# 我的数据-取消开发接口服务类
logger = MyLog("cancelDevelopmentFunction").getlog()
@api_assemble_new()
def cancelDevelopmentFunction(platform,searchType,paramList,cancelNotesInfoStr):
    logger.info("cancelDevelopmentFunction ---->start!")
    if len(paramList) == 0 or cancelNotesInfoStr == "" or searchType == "" or platform == "":
        logger.error("cancelDevelopmentFunction --> request parameters is wrong!")
        return "请求参数为空"
    # 将入参list转为string类型
    paramStr = ""
    for i in range(len(paramList)):
        paramStr += "'" + paramList[i] + "',"
    # 拼接接口请求入参
    reqSelect = DasApiInputParam.cancelDevelop_select
    reqSelect["ids"] = paramList
    reqSelect["cancelNotesInfo"] = cancelNotesInfoStr
    reqParam = DasApiInputParam.cancelDevelop_param
    reqParam["args"] = str(reqSelect)
    url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
    return url,reqParam