'''
@File: dataManageProductListingApi.py
@time:2021/8/24
@Author:quanliu
@Desc:我的数据-查询接口服务类（amazon/smt/1688/ebay/shopee共用）
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonParamService import PublicCommonParamServiceClass
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.operate_api_data import api_assemble_new, Splicing_Params
from loggerUtils import MyLog

logger = MyLog("dataManageProductListingInfo").getlog()
@api_assemble_new()
def dataManageProductListingInfo(platform,searchType,kwargs):
    logger.info("dataManageProductListingInfo ---->start!")
    # 接口地址
    url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType) # 获取请求地址
    # 接口入参
    productInfoSelect03,productInfoSelect02,productInfoSelect01 = PublicCommonParamServiceClass().getApiInputParam(platform,searchType)
    paramList = []
    paramList.append(productInfoSelect01)
    paramList.append(productInfoSelect02)
    paramList.append(productInfoSelect03)
    requestJson = Splicing_Params(paramList,kwargs).splicing_params() # 拼接接口参数
    return url,requestJson