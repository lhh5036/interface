'''
@File: queryWipoPageListApi.py
@time:2021/9/16
@Author:quanliu 181324
@Desc:工具助手-WIPO商标词
'''

from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("QueryWipoPageListApi").getlog()  # 初始化
class QueryWipoPageListApi():
    def queryWipoPageListFunciton(self,kwargs):# 参数为dict格式
        logger.info("queryWipoPageListFunciton------------------->start")
        url = DasApiUrl.queryWipoPage_url  # 请求地址
        # 请求参数
        queryWipoPage_param03 = DasApiInputParam.queryWipoPage_param03
        queryWipoPage_param02 = DasApiInputParam.queryWipoPage_param02
        queryWipoPage_param01 = DasApiInputParam.queryWipoPage_param01
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i],kwargs)
                queryWipoPage_param03[keyList[i]] = value
        queryWipoPage_param02["search"] = queryWipoPage_param03
        queryWipoPage_param01["args"] = json.dumps(queryWipoPage_param02)
        # 请求头信息
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url
        self.header = header
        self.formData = queryWipoPage_param01
        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("queryWipoPageListFunciton------------------->end")
            return "接口响应成功,接口返回值:{0}".format(resp.json()["rows"])
        else:
            logger.error("queryWipoPageListFunciton------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], url,queryWipoPage_param01)

if __name__ == '__main__':
    print(QueryWipoPageListApi().queryWipoPageListFunciton({"source":"AETM","startCrawlTime":"2021-03-26 00:00:00","endCrawlTime":"2021-03-27 00:00:00"}))