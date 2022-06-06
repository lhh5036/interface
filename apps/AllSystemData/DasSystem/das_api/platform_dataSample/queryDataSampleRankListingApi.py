'''
@File: queryDataSampleRankListingApi.py
@time:2021/9/1
@Author:quanliu
@Desc:数据采集-查询接口服务类(amazon/smt/1688/ebay/shopee全部页面共用)
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonJudgeEmptySevice import PublicCommonJudgeEmptySevice
from apps.AllSystemData.DasSystem.das_api.publicCommonParamService import PublicCommonParamServiceClass
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json


@api_assemble_new()
def dataSampleRankListingFunction(platform,searchType,kwargs):
    app.logger.info("dataSampleRankListingFunction------------------->start")
    # 判断哪个页面的数据需要对入参进行判空
    isNeedEmpty = PublicCommonJudgeEmptySevice().needJudgeEmpty(platform, searchType,kwargs)
    if isNeedEmpty == True:
        country = parseRequestDatas("country", kwargs)  # 站点判空
        if country == "" or searchType == "":
            app.logger.error("dataSampleRankListingFunction--------->InputParam:country or searchType is null")
            return "请求参数country或searchType为空"
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
