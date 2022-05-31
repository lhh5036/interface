'''
@File: queryDataSampleRankListingApi.py
@time:2021/9/1
@Author:quanliu
@Desc:数据采集-查询接口服务类(amazon/smt/1688/ebay/shopee全部页面共用)
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonJudgeEmptySevice import PublicCommonJudgeEmptySevice
from apps.AllSystemData.DasSystem.das_api.publicCommonParamService import PublicCommonParamServiceClass
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.get_page_content_by_requests import get_page_content_by_requests
from flask import current_app as app
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json


class DataSmapleRankListingQueryApi():
    def dataSampleRankListingFunction(self,platform,searchType,kwargs):
        app.logger.info("dataSampleRankListingFunction------------------->start")
        # 判断哪个页面的数据需要对入参进行判空
        isNeedEmpty = PublicCommonJudgeEmptySevice().needJudgeEmpty(platform, searchType,kwargs)
        if isNeedEmpty == True:
            country = parseRequestDatas("country", kwargs)  # 站点判空
            if country == "" or searchType == "":
                app.logger.error("dataSampleRankListingFunction--------->InputParam:country or searchType is null")
                return "请求参数country或searchType为空"
        # 获取请求参数
        rankListing03,rankListing02,rankListing01 = PublicCommonParamServiceClass().getApiInputParam(platform,searchType)
        url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType) # 获取请求地址
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i],kwargs)
                rankListing03[keyList[i]] = value
        # 替换中间层
        rankListing02["search"] = rankListing03
        # 替换最外层参数
        rankListing01["args"] = json.dumps(rankListing02)
        # 接口请求头
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url # 请求地址
        self.header = header
        self.fromData = rankListing01
        resp = get_page_content_by_requests(self.url,self.header,self.fromData)
        if resp.json()["success"] == True:
            app.logger.info("dataSampleRankListingFunction------------------->end")
            return "接口响应成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            app.logger.error("dataSampleRankListingFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},接口类型:{2},请求参数:{3}".format(resp.json()["errorMsg"], url,searchType,rankListing01)


if __name__ == '__main__':
    print(DataSmapleRankListingQueryApi().dataSampleRankListingFunction("Smt","categoryMark_query",{}))
