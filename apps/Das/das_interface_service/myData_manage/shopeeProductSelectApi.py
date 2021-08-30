'''
@File: shopeeProductSelectApi.py
@time:2021/8/24
@Author:quanliu
@Desc:我的数据-shopee页面查询接口服务类
'''
import json
import requests

from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.Das.logger import MyLog
from apps.Common_Config.parseRequestDatas import parseRequestDatas

# 实例化日志类
logger = MyLog("ShopeeProductSelectApi").getlog() # 初始化
class ShopeeProductSelectApi():
    def shopeeProductListingInfo(self,kwargs):
        logger.info("shopeeProductListingInfo ---->start!")
        # 接口地址
        url = DasApiUrl.shopee_queryListing_url
        # 拼接接口入参
        shopeeProductInfoSelect = DasApiInputParam.shopee_productInfo03
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
        if len(keyList) != 0:
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i],kwargs)
                shopeeProductInfoSelect[keyList[i]] = value

        # 替换中间层
        shopee_productInfo02 = DasApiInputParam.shopee_productInfo02
        shopee_productInfo02["search"] = shopeeProductInfoSelect
        # 替换外层
        shopeeProductInfoParam = DasApiInputParam.shopee_productInfo03
        shopeeProductInfoParam["args"] = json.dumps(shopee_productInfo02)
        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")
        self.url = url
        self.formData = shopeeProductInfoParam
        self.header = header
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("shopeeProductListingInfo---->end!")
            return "接口响应成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("shopeeProductListingInfo -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,shopeeProductInfoParam)




if __name__ == '__main__':
    print(ShopeeProductSelectApi().shopeeProductListingInfo("第一个用例",{"productId":"7567527309","mainSku":"9SD400200"}))