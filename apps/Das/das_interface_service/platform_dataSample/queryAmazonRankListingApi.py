'''
@File: queryAmazonOtherListingApi.py
@time:2021/8/31
@Author:quanliu
@Desc:数据采集-Amazon关注关键词数据页面接口服务类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.logger import MyLog
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json
import requests

# 实例化日志类
from apps.Das.publicCommonService import PublicCommonServiceClass

logger = MyLog("AmazonOtherListingQueryApi").getlog() # 初始化
class AmazonOtherListingQueryApi():
    def amazonOtherListingFunction(self,searchType,kwargs):
        logger.info("amazonOtherListingFunction------------------->start")
        # 判断哪个页面的数据需要对入参进行判空
        isNeedEmpty = PublicCommonServiceClass().needJudgeEmpty(searchType)
        if isNeedEmpty == True:
            country = parseRequestDatas("country",kwargs)
            if country == "" or searchType == "":
                logger.error("amazonOtherListingFunction--------->InputParam:country or searchType is null")
                return "请求参数country或searchType为空"
        amazon_otherTypeListing03,amazon_otherTypeListing02,amazon_otherTypeListing01,url = PublicCommonServiceClass().getApiInputParam(searchType)
        keyList = []
        for key in kwargs.keys():
            keyList.append(key)
        for i in range(len(keyList)):
            value = parseRequestDatas(keyList[i],kwargs)
            amazon_otherTypeListing03[keyList[i]] = value
        # 替换中间层
        amazon_otherTypeListing02["search"] = amazon_otherTypeListing03
        # 替换最外层参数
        amazon_otherTypeListing01["args"] = json.dumps(amazon_otherTypeListing02)
        # 接口请求头
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url # 请求地址
        self.header = header
        self.fromData = amazon_otherTypeListing01
        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.fromData))
        if resp.json()["success"] == True:
            logger.info("amazonOtherListingFunction------------------->end")
            return "接口调用成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("amazonOtherListingFunction------------->response Data is wrong!")
            return "接口调用失败,失败原因:{0},接口地址:{1},接口类型:{2},请求参数:{3}".format(resp.json()["errorMsg"], url,searchType,amazon_otherTypeListing01)


