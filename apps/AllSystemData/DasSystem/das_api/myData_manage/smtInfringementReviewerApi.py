'''
@File: smtInfringementReviewerApi.py
@time:2021/8/30
@Author:quanliu
@Desc:我的数据-SMT分配侵权审核人接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
import json


@api_assemble_new()
def smtInfringementReviewerFun(paramList,paramStr):# paramList--id集合,paramStr---侵权审核人字段
    app.logger.info("smtInfringementReviewerFun--------------->start")
    if paramStr == "" or len(paramList) == 0:
        app.logger.error("smtInfringementReviewerFun---->Input Parameters is null")
        return "请求参数为空"
    # 替换参数
    smt_infringementReviewer02 = DasApiInputParam.smt_infringementReviewer02
    smt_infringementReviewer02["ids"] = paramList
    smt_infringementReviewer02["infringementReviewer"] = paramStr
    smt_infringementReviewer01 = DasApiInputParam.smt_infringementReviewer01
    smt_infringementReviewer01["args"] = json.dumps(smt_infringementReviewer02)
    # 获取请求地址
    url = DasApiUrl.smt_infringementReviewer_url
    return url,smt_infringementReviewer01