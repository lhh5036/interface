'''
@File: aliProductSelectInterface.py
@time:2021/8/24
@Author:quanliu
@Desc:我的数据-1688查询页面服务类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.myDataManage_inter_body import MyDataManageInterParam
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl
from apps.Das.logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("AliProductSelectInterface").getlog() # 初始化
class AliProductSelectInterface():
    def aliProductListingInfo(self,casename,kwargs):
        logger.info("aliProductListingInfo ---->start!")
        # 接口地址
        url = MyDataManageInterUrl.ali_queryListing_url

        # 拼接接口入参
        aliProductInfoSelect = MyDataManageInterParam.ali_productInfo03

        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
        if len(keyList) != 0:
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i],kwargs)
                aliProductInfoSelect[keyList[i]] = value

        # 替换中间层
        ali_productInfo02 = MyDataManageInterParam.ali_productInfo02
        ali_productInfo02["search"] = aliProductInfoSelect

        # 替换外层
        aliProductInfoParam = MyDataManageInterParam.ali_productInfo01
        aliProductInfoParam["args"] = json.dumps(ali_productInfo02)

        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")

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
    print(AliProductSelectInterface().aliProductListingInfo("第一个用例",{}))