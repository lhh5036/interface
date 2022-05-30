'''
@File: queryJsKwRuleListApi.py
@time:2021/9/16
@Author:quanliu 181324
@Desc:工具助手-Jungle Scout规则配置查询接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("QueryJsKwRuleListApi").getlog()  # 初始化
class QueryJsKwRuleListApi():
    def queryJsKwRuleListFunction(self,kwargs):# 参数为dict格式
        logger.info("queryJsKwRuleListFunction------------------->start")
        url = DasApiUrl.queryJsKwRule_url  # 请求地址
        # 请求参数
        queryJsKwRule_param03 = DasApiInputParam.queryJsKwRule_param03
        queryJsKwRule_param02 = DasApiInputParam.queryJsKwRule_param02
        queryJsKwRule_param01 = DasApiInputParam.queryJsKwRule_param01
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i],kwargs)
                queryJsKwRule_param03[keyList[i]] = value
        queryJsKwRule_param02["search"] = queryJsKwRule_param03
        queryJsKwRule_param01["args"] = json.dumps(queryJsKwRule_param02)
        # 请求头信息
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url
        self.header = header
        self.formData = queryJsKwRule_param01
        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("queryJsKwRuleListFunction------------------->end")
            return "接口响应成功,接口返回值:{0}".format(resp.json()["rows"])
        else:
            logger.error("queryJsKwRuleListFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], url,queryJsKwRule_param01)

if __name__ == '__main__':
    print(QueryJsKwRuleListApi().queryJsKwRuleListFunction({}))