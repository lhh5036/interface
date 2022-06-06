'''
@File: dataManageProductListingApi.py
@time:2021/8/24
@Author:quanliu
@Desc:我的数据-查询接口服务类（amazon/smt/1688/ebay/shopee共用）
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonParamService import PublicCommonParamServiceClass
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from flask import current_app as app
from apps.Common_Config.operate_api_data import api_assemble_new
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json

@api_assemble_new()
def dataManageProductListingInfo(platform,searchType,kwargs):
    app.logger.info("dataManageProductListingInfo ---->start!")
    # 接口地址
    url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType) # 获取请求地址
    # 拼接接口入参
    productInfoSelect03,productInfoSelect02,productInfoSelect01 = PublicCommonParamServiceClass().getApiInputParam(platform,searchType)
    keyList = []
    if kwargs != "":
        for key in kwargs.keys():
            keyList.append(key)
        for i in range(len(keyList)):
            value = parseRequestDatas(keyList[i],kwargs)
            productInfoSelect03[keyList[i]] = value
    # 替换中间层
    productInfoSelect02["search"] = productInfoSelect03
    # 替换外层
    productInfoSelect01["args"] = json.dumps(productInfoSelect02)
    return url,productInfoSelect01