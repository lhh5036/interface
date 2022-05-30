'''
@File: queryJsKwPageListApi.py
@time:2021/9/16
@Author:quanliu 181324
@Desc:工具助手-Amazon关键词库查询接口
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam

from logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("QueryJsKwPageListApi").getlog()  # 初始化
class QueryJsKwPageListApi():
    def queryJsKwPageListFunction(self,kwargs):# 参数为dict格式
        logger.info("queryJsKwPageListFunction------------------->start")
        url = DasApiUrl.queryJsKw_url  # 请求地址
        # 请求参数
        queryJsKw_param03 = DasApiInputParam.queryJsKw_param03
        queryJsKw_param02 = DasApiInputParam.queryJsKw_param02
        queryJsKw_param01 = DasApiInputParam.queryJsKw_param01
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i],kwargs)
                queryJsKw_param03[keyList[i]] = value
        queryJsKw_param02["search"] = queryJsKw_param03
        queryJsKw_param01["args"] = json.dumps(queryJsKw_param02)
        # 请求头信息
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url
        self.header = header
        self.formData = queryJsKw_param01
        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("queryJsKwPageListFunction------------------->end")
            return "接口响应成功,接口返回值:{0}".format(resp.json()["rows"])
        else:
            logger.error("queryJsKwPageListFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], url,queryJsKw_param01)

if __name__ == '__main__':
    print(QueryJsKwPageListApi().queryJsKwPageListFunction({}))
