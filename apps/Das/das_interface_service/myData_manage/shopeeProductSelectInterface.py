'''
@File: shopeeProductSelectInterface.py
@time:2021/8/24
@Author:quanliu
@Desc:我的数据-shopee页面查询接口服务类
'''
import json
import requests
from apps.Das.das_interface_service.das_common_header import DasCommonHeader
from apps.Das.das_interface_service.myDataManage_inter_body import MyDataManageInterParam
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl
from apps.Das.logger import MyLog

# 实例化日志类
logger = MyLog("ShopeeProductSelectInterface").getlog() # 初始化
class ShopeeProductSelectInterface():
    def shopeeProductListingInfo(self,casename,kwargs):
        logger.info("shopeeProductListingInfo ---->start!")
        # 接口地址
        url = MyDataManageInterUrl.shopee_queryListing_url
        # 拼接接口入参
        shopeeProductInfoSelect = MyDataManageInterParam.shopee_productInfo03
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
        if len(keyList) != 0:
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i],kwargs)
                shopeeProductInfoSelect[keyList[i]] = value

        # 替换中间层
        shopee_productInfo02 = MyDataManageInterParam.shopee_productInfo02
        shopee_productInfo02["search"] = shopeeProductInfoSelect

        # 替换外层
        shopeeProductInfoParam = MyDataManageInterParam.shopee_productInfo03
        shopeeProductInfoParam["args"] = json.dumps(shopee_productInfo02)

        # 接口请求头
        header = DasCommonHeader().getDasCommonHeader("new","181324")

        self.url = url
        self.formData = shopeeProductInfoParam
        self.header = header

        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            return "{0}----->success".format(casename)
        else:
            logger.error("shopeeProductListingInfo -->response Data is wrong!")
            return "{0}-->响应结果有误,接口地址:{1},接口入参:{2}".format(casename, url, kwargs)

        logger.info("shopeeProductListingInfo---->end!")


# 解析每一个入参
def parseRequestDatas(keyname,kwargs):
    if kwargs.get(keyname) is None:
        valueName = ""
    else:
        valueName = kwargs.get(keyname)
    return valueName

if __name__ == '__main__':
    print(ShopeeProductSelectInterface().shopeeProductListingInfo("第一个用例",{"productId":"7567527309","mainSku":"9SD400200"}))