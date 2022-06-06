'''
@File: queryTaskCenterListingApi.py
@time:2021/9/1
@Author:quanliu
@Desc:任务中心-查询接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonJudgeEmptySevice import PublicCommonJudgeEmptySevice
from apps.AllSystemData.DasSystem.das_api.publicCommonParamService import PublicCommonParamServiceClass
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json


@api_assemble_new()
def taskCenterRankListingFunction(platform,searchType,kwargs):
    app.logger.info("taskCenterRankListingFunction------------------->start")
    # 是否校验入参
    needJudge = PublicCommonJudgeEmptySevice().needJudgeEmpty(platform,searchType,kwargs)
    if needJudge == True :
        app.logger.error("taskCenterRankListingFunction-------->InputParam is null")
        return "请求参数为空!"
    # 获取请求参数
    rankListing03,rankListing02,rankListing01 = PublicCommonParamServiceClass().getApiInputParam(platform,searchType)
    url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType) # 获取请求地址
    keyList = []
    if kwargs != "":
        for key in kwargs.keys():
            keyList.append(key)
        for i in range(len(keyList)):
            value = parseRequestDatas(keyList[i],kwargs)
            rankListing03[keyList[i]] = value
    # 替换中间层
    rankListing02["search"] = rankListing03
    # 替换最外层参数
    rankListing01["args"] = json.dumps(rankListing02)
    return url,rankListing01


if __name__ == '__main__':
    # Amazon/SMT/Alibaba1688/Shopee
    print(taskCenterRankListingFunction("Amazon","amazon_customizeMarkListing",{"saleChannel":"Amazon","country":"US"}))
