'''
@File: queryShopeeRankListingApi.py
@time:2021/9/1
@Author:quanliu
@Desc:数据采集-shopee查询接口服务类
'''

from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.publicCommonService import PublicCommonServiceClass
from apps.Das.logger import MyLog
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json
import requests

# 日志初始化
logger = MyLog("ShopeeRankListingQueryApi").getlog() # 初始化
# 数据采集-Shopee页面查询接口服务类
class ShopeeRankListingQueryApi():
    def shopeeRankListingFunction(self,searchType,kwargs):
        logger.info("shopeeRankListingFunction------------------->start")
        # 获取接口请求参数
        shopeeRankListing03,shopeeRankListing02,shopeeRankListing01 = PublicCommonServiceClass().getApiInputParam("Shopee", searchType)
        # 获取接口地址
        url = PublicCommonServiceClass().getApiUrl("Shopee", searchType)
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i],kwargs)
                shopeeRankListing03[keyList[i]] = value
        # 替换中间层
        shopeeRankListing02["search"] = shopeeRankListing03
        # 替换最外层
        shopeeRankListing01["args"] = json.dumps(shopeeRankListing02)
        # 获取请求头信息
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url
        self.header = header
        self.formData = shopeeRankListing01
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("shopeeRankListingFunction------------------->end")
            return "接口调用成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("shopeeRankListingFunction------------->response Data is wrong!")
            return "接口调用失败,失败原因:{0},接口地址:{1},接口类型:{2},请求参数:{3}".format(resp.json()["errorMsg"], url,searchType,shopeeRankListing01)
