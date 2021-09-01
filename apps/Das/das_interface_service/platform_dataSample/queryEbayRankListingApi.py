'''
@File: queryEbayRankListingApi.py
@time:2021/9/1
@Author:quanliu
@Desc:数据采集-ebay查询接口服务类
'''

from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.publicCommonService import PublicCommonServiceClass
from apps.Das.logger import MyLog
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json
import requests

# 日志初始化
logger = MyLog("EbayRankListingQueryApi").getlog() # 初始化
# 数据采集-SMT页面查询接口服务类
class EbayRankListingQueryApi():
    def ebayRankListingFunction(self,searchType,kwargs):
        logger.info("ebayRankListingFunction------------------->start")
        # 获取接口请求参数
        ebayRankListing03,ebayRankListing02,ebayRankListing01 = PublicCommonServiceClass().getApiInputParam("ebay", searchType)
        # 获取接口地址
        url = PublicCommonServiceClass().getApiUrl("ebay", searchType)
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i],kwargs)
                ebayRankListing03[keyList[i]] = value
        # 替换中间层
        ebayRankListing02["search"] = ebayRankListing03
        # 替换最外层
        ebayRankListing01["args"] = json.dumps(ebayRankListing02)
        # 获取请求头信息
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url
        self.header = header
        self.formData = ebayRankListing01
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("ebayRankListingFunction------------------->end")
            return "接口调用成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("ebayRankListingFunction------------->response Data is wrong!")
            return "接口调用失败,失败原因:{0},接口地址:{1},接口类型:{2},请求参数:{3}".format(resp.json()["errorMsg"], url,searchType,ebayRankListing01)
