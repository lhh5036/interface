'''
@File: addKeywordsTaskListApi.py
@time:2021/9/15
@Author:quanliu 181324
@Desc:任务中心-关键词监控-新增关键词接口服务类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.logger import MyLog
import requests
import json

# 实例化日志类
logger = MyLog("AddKeywordsTaskListApi").getlog() # 初始化
class AddKeywordsTaskListApi():
    def addKeywordsTaskListFunction(self,kwargs):
        logger.info("addKeywordsTaskListFunction------------------->start")
        country = parseRequestDatas("country", kwargs)
        saleChannel = parseRequestDatas("saleChannel",kwargs)
        keyword = parseRequestDatas("keyword",kwargs)
        if country == "" or saleChannel == "" or keyword == "":
            logger.error("addKeywordsTaskListFunction---------->Input Params is null")
            return "请求参数为空!"
        # 获取请求参数
        addKeywordsTask_param02 = DasApiInputParam.addKeywordsTask_param02
        addKeywordsTask_param01 = DasApiInputParam.addKeywordsTask_param01
        # 获取请求地址
        addTask_url = DasApiUrl.addTask_url
        # 获取请求头信息
        header = Common_TokenHeader().token_header("new", "181324")
        addKeywordsTask_param02["country"] = country
        addKeywordsTask_param02["saleChannel"] = saleChannel
        addKeywordsTask_param02["keyword"] = keyword

        addKeywordsTask_param01["args"] = json.dumps(addKeywordsTask_param02)
        self.url = addTask_url
        self.header = header
        self.formData = addKeywordsTask_param01
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData,ensure_ascii=False))
        if resp.json()["success"] == True:
            logger.info("addKeywordsTaskListFunction------------------->end")
            return "任务添加成功"
        else:
            logger.error("addKeywordsTaskListFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], addTask_url,addKeywordsTask_param01)

if __name__ == '__main__':
    print(AddKeywordsTaskListApi().addKeywordsTaskListFunction({"taskType":2,"country":"US","keyword":"椅子","saleChannel":"Amazon"}))