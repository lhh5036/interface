'''
@File: ebayProductSelectInterface.py
@time:2021/8/24
@Author:quanliu
@Desc:我的数据-ebay页面查询接口服务类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.myDataManage_inter_body import MyDataManageInterParam
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl
from apps.Das.logger import MyLog
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json
import requests

# 实例化日志类
logger = MyLog("EbayProductSelectInterface").getlog() # 初始化
class EbayProductSelectInterface():
    def ebayProductListingInfo(self,kwargs):
        logger.info("ebayProductListingInfo ---->start!")
        # 接口地址
        url = MyDataManageInterUrl.ebay_queryListing_url
        # 拼接接口入参
        ebayProductInfoSelect = MyDataManageInterParam.ebay_productInfo03
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)

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
        header = Common_TokenHeader().token_header("new","181324")
        self.url = url
        self.formData = ebayProductInfoParam
        self.header = header
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            return "接口响应成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("ebayProductListingInfo -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], url, kwargs)

        logger.info("ebayProductListingInfo---->end!")


if __name__ == '__main__':
    print(EbayProductSelectInterface().ebayProductListingInfo("第一个用例",{"productId":"223609848242","mainSku":"9SD400151"}))