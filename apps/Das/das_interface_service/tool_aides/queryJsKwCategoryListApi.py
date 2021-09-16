'''
@File: queryJsKwCategoryListApi.py
@time:2021/9/16
@Author:quanliu 181324
@Desc:工具助手-Jungle Scout规则配置国家类目查询接口服务类
'''

from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("QueryJsKwCategoryListApi").getlog()  # 初始化

class QueryJsKwCategoryListApi():
    def queryJsKwCategoryListFunction(self,countryStr):
        logger.info("queryJsKwCategoryListFunction------------------->start")
        if countryStr == "":
            logger.error("queryJsKwCategoryListFunction------------------->country is empty!")
            return "国家字段为空!"
        url = DasApiUrl.queryJsKeywordCategoryList_url  # 请求地址
        # 请求参数
        queryJsKeywordCategoryList_param02 = DasApiInputParam.queryJsKeywordCategoryList_param02
        queryJsKeywordCategoryList_param01 = DasApiInputParam.queryJsKeywordCategoryList_param01
        queryJsKeywordCategoryList_param02["country"] = countryStr
        queryJsKeywordCategoryList_param01["args"] = json.dumps(queryJsKeywordCategoryList_param02)
        # 请求头信息
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url
        self.header = header
        self.formData = queryJsKeywordCategoryList_param01
        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("queryJsKwCategoryListFunction------------------->end")
            return "接口响应成功,接口返回值:{0}".format(resp.json()["result"])
        else:
            logger.error("queryJsKwCategoryListFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], url,queryJsKeywordCategoryList_param01)

if __name__ == '__main__':
    print(QueryJsKwCategoryListApi().queryJsKwCategoryListFunction("United Kingdom"))


