'''
@File: queryAmazonAttentStoreListingApi.py
@time:2021/8/31
@Author:quanliu
@Desc:数据采集-Amazon关注店铺数据查询接口服务类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.Das.logger import MyLog
import json
import requests
# 实例化日志类
logger = MyLog("AmazonAttentStoreListingQueryApi").getlog() # 初始化
class AmazonAttentStoreListingQueryApi():
    def amazonAttentStoreListingFunction(self,kwargs):
        logger.info("amazonAttentStoreListingFunction------------------->start")
        # 校验必填项
        country = parseRequestDatas("country", kwargs)
        if country == "":
            logger.error("amazonAttentStoreListingFunction------>InputParam:country is null")
            return "请求参数country为空"
        # 获取内层参数
        amazon_attentStoreListing03 = DasApiInputParam.amazon_attentStoreListing03
        keyList = []
        for key in kwargs.keys():
            keyList.append(key)
        for i in range(len(keyList)):
            value = parseRequestDatas(keyList[i],kwargs)
            amazon_attentStoreListing03[keyList[i]] = value
        # 替换中间层
        amazon_attentStoreListing02 = DasApiInputParam.amazon_attentStoreListing02
        amazon_attentStoreListing02["search"] = amazon_attentStoreListing03

        # 替换外层
        amazon_attentStoreListing01 = DasApiInputParam.amazon_attentStoreListing01
        amazon_attentStoreListing01["args"] = json.dumps(amazon_attentStoreListing02)
        # 接口请求头
        header = Common_TokenHeader().token_header("new", "181324")
        # 请求地址
        url = DasApiUrl.amazon_attentStoreListing_url
        self.url = url
        self.header = header
        self.fromData = amazon_attentStoreListing01
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.fromData))
        if resp.json()["success"] == True:
            logger.info("amazonAttentStoreListingFunction------------------->end")
            return "接口调用成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("amazonAttentStoreListingFunction------------->response Data is wrong!")
            return "接口调用失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,amazon_attentStoreListing01)





