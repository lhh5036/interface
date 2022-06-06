'''
@File: checkAccountProductByRankApi.py
@time:2021/8/26
@Author:quanliu
@Desc:校验哪些产品已经被认领过接口类
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
import json


# 校验哪些产品已经被认领过接口类
@api_assemble_new()
def checkProductByRankFunction(platform,searchType,salechannelname,idsList):
    app.logger.info("checkProductByRankFunction------>start")
    if salechannelname == "" or len(idsList) == 0:
        app.logger.error("checkProductByRankFunction --> request parameters is wrong!")
        return "请求参数为空"

    # 拼接内层参数
    checkAccountProductByRank02 = DasApiInputParam.checkAccountProductByRank02
    checkAccountProductByRank02["saleChannel"] = salechannelname
    checkAccountProductByRank02["baseIdList"] = idsList
    # 拼接外层参数
    checkAccountProductByRank01 = DasApiInputParam.checkAccountProductByRank01
    checkAccountProductByRank01["args"] = json.dumps(checkAccountProductByRank02)
    url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
    return url,checkAccountProductByRank01