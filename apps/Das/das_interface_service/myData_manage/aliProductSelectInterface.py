'''
@File: aliProductSelectInterface.py
@time:2021/8/24
@Author:quanliu
@Desc:我的数据-1688查询页面服务类
'''
from apps.Das.das_interface_service.das_common_header import DasCommonHeader
from apps.Das.das_interface_service.myDataManage_inter_body import MyDataManageInterParam
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl
from apps.Das.logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("MyDataAmazonSelectInterface").getlog() # 初始化
class AliProductSelectInterface():
    def aliProductListingInfo(self,casename,kwargs):
        logger.info("aliProductListingInfo ---->start!")
        # 接口地址
        url = MyDataManageInterUrl.ali_queryListing_url
        # 解析参数
        brand = parseRequestDatas("brand",kwargs)
        keywords = parseRequestDatas("keywords",kwargs)
        startPrice = parseRequestDatas("startPrice",kwargs)
        endPrice = parseRequestDatas("endPrice",kwargs)
        dataStatus = parseRequestDatas("dataStatus",kwargs)
        mainSku = parseRequestDatas("mainSku",kwargs)
        associatedSystemSku = parseRequestDatas("associatedSystemSku",kwargs)
        skuMapStr = parseRequestDatas("skuMapStr",kwargs)
        productId = parseRequestDatas("productId",kwargs)
        endOrders = parseRequestDatas("endOrders",kwargs)
        startOrders = parseRequestDatas("startOrders",kwargs)
        Reviews = parseRequestDatas("Reviews",kwargs)
        rating = parseRequestDatas("rating",kwargs)
        merchantName = parseRequestDatas("merchantName",kwargs)
        startCrawlTime = parseRequestDatas("startCrawlTime",kwargs)
        endCrawlTime = parseRequestDatas("endCrawlTime",kwargs)
        startDistributionTime = parseRequestDatas("startDistributionTime",kwargs)
        endDistributionTime = parseRequestDatas("endDistributionTime",kwargs)
        developmentStatus = parseRequestDatas("developmentStatus",kwargs)

        # 拼接接口入参
        aliProductInfoSelect = MyDataManageInterParam.ali_productInfo03
        aliProductInfoSelect["brand"] = brand
        aliProductInfoSelect["keywords"] = keywords
        aliProductInfoSelect["startPrice"] = startPrice
        aliProductInfoSelect["endPrice"] = endPrice
        aliProductInfoSelect["dataStatus"] = dataStatus
        aliProductInfoSelect["mainSku"] = mainSku
        aliProductInfoSelect["associatedSystemSku"] = associatedSystemSku
        aliProductInfoSelect["skuMapStr"] = skuMapStr
        aliProductInfoSelect["productId"] = productId
        aliProductInfoSelect["endOrders"] = endOrders
        aliProductInfoSelect["startOrders"] = startOrders
        aliProductInfoSelect["Reviews"] = Reviews
        aliProductInfoSelect["rating"] = rating
        aliProductInfoSelect["merchantName"] = merchantName
        aliProductInfoSelect["startCrawlTime"] = startCrawlTime
        aliProductInfoSelect["endCrawlTime"] = endCrawlTime
        aliProductInfoSelect["startDistributionTime"] = startDistributionTime
        aliProductInfoSelect["endDistributionTime"] = endDistributionTime
        aliProductInfoSelect["developmentStatus"]= developmentStatus

        # 替换中间层
        ali_productInfo02 = MyDataManageInterParam.ali_productInfo02
        ali_productInfo02["search"] = aliProductInfoSelect

        # 替换外层
        aliProductInfoParam = MyDataManageInterParam.ali_productInfo01
        aliProductInfoParam["args"] = json.dumps(ali_productInfo02)

        # 接口请求头
        header = DasCommonHeader().getDasCommonHeader("new","181324")

        self.url = url
        self.formData = aliProductInfoParam
        self.header = header

        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            return "{0}----->success".format(casename)
        else:
            logger.error("aliProductListingInfo -->response Data is wrong!")
            return "{0}-->响应结果有误,接口地址:{1},接口入参:{2}".format(casename, url, kwargs)

        logger.info("aliProductListingInfo---->end!")


# 解析每一个入参
def parseRequestDatas(keyname,kwargs):
    if kwargs.get(keyname) is None:
        valueName = ""
    else:
        valueName = kwargs.get(keyname)
    return valueName

if __name__ == '__main__':
    print(AliProductSelectInterface().aliProductListingInfo("第一个用例",{"productId":"642127417745"}))