'''
@File: aliProductSelectInterface.py
@time:2021/8/24
@Author:quanliu
@Desc:我的数据-1688查询页面服务类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl

from apps.Das.logger import MyLog
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json
import requests

# 实例化日志类
logger = MyLog("AliProductSelectInterface").getlog() # 初始化
class AliProductSelectInterface():
    def aliProductListingInfo(self,kwargs):
        logger.info("aliProductListingInfo ---->start!")
        # 接口地址
        url = DasApiUrl.ali_queryListing_url
        # 拼接接口入参
        aliProductInfoSelect = DasApiInputParam.ali_productInfo03
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i],kwargs)
                aliProductInfoSelect[keyList[i]] = value
        # 替换中间层
        ali_productInfo02 = DasApiInputParam.ali_productInfo02
        ali_productInfo02["search"] = aliProductInfoSelect
        # 替换外层
        aliProductInfoParam = DasApiInputParam.ali_productInfo01
        aliProductInfoParam["args"] = json.dumps(ali_productInfo02)
        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")

        self.url = url
        self.formData = aliProductInfoParam
        self.header = header

        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("aliProductListingInfo---->end!")
            return "接口响应成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("aliProductListingInfo -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,aliProductInfoParam)




if __name__ == '__main__':
    print(AliProductSelectInterface().aliProductListingInfo({}))