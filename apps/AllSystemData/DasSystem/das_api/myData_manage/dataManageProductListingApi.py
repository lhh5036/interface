'''
@File: dataManageProductListingApi.py
@time:2021/8/24
@Author:quanliu
@Desc:我的数据-查询接口服务类（amazon/smt/1688/ebay/shopee共用）
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonParamService import PublicCommonParamServiceClass
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.get_page_content_by_requests import get_page_content_by_requests
from flask import current_app as app
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json

class DataManageProductListingApi():
    def dataManageProductListingInfo(self,platform,searchType,kwargs):
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
        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")
        self.url = url
        self.formData = productInfoSelect01
        self.header = header
        resp = get_page_content_by_requests(self.url,self.header,self.formData)
        if resp.json()["success"] == True:
            app.logger.info("dataManageProductListingInfo---->end!")
            return "接口响应成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            app.logger.error("dataManageProductListingInfo -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,productInfoSelect01)


if __name__ == '__main__':
    print(DataManageProductListingApi().dataManageProductListingInfo("Amazon","bestsellerMark_query",{"country":"US"}))