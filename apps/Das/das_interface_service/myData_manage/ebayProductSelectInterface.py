'''
@File: ebayProductSelectInterface.py
@time:2021/8/24
@Author:quanliu
@Desc:我的数据-ebay页面查询接口服务类
'''
from apps.Das.das_interface_service.das_common_header import DasCommonHeader
from apps.Das.das_interface_service.myDataManage_inter_body import MyDataManageInterParam
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl
from apps.Das.logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("EbayProductSelectInterface").getlog() # 初始化
class EbayProductSelectInterface():
    def ebayProductListingInfo(self,casename,kwargs):
        logger.info("ebayProductListingInfo ---->start!")
        # 接口地址
        url = MyDataManageInterUrl.ebay_queryListing_url
        # 拼接接口入参
        ebayProductInfoSelect = MyDataManageInterParam.ebay_productInfo03
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
        if len(keyList) != 0:
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i],kwargs)
                ebayProductInfoSelect[keyList[i]] = value

        # 替换中间层
        ebay_productInfo02 = MyDataManageInterParam.ebay_productInfo02
        ebay_productInfo02["search"] = ebayProductInfoSelect

        # 替换外层
        ebayProductInfoParam = MyDataManageInterParam.ebay_productInfo01
        ebayProductInfoParam["args"] = json.dumps(ebay_productInfo02)

        # 接口请求头
        header = DasCommonHeader().getDasCommonHeader("new","181324")

        self.url = url
        self.formData = ebayProductInfoParam
        self.header = header

        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            return "{0}----->success".format(casename)
        else:
            logger.error("ebayProductListingInfo -->response Data is wrong!")
            return "{0}-->响应结果有误,接口地址:{1},接口入参:{2}".format(casename, url, kwargs)

        logger.info("ebayProductListingInfo---->end!")


# 解析每一个入参
def parseRequestDatas(keyname,kwargs):
    if kwargs.get(keyname) is None:
        valueName = ""
    else:
        valueName = kwargs.get(keyname)
    return valueName

if __name__ == '__main__':
    print(EbayProductSelectInterface().ebayProductListingInfo("第一个用例",{"productId":"223609848242","mainSku":"9SD400151"}))