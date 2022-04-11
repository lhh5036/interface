'''
@File: addJSKwCategoryListApi.py
@time:2021/9/16
@Author:quanliu 181324
@Desc:工具助手-Jungle Scout规则配置新增规则接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam

from apps.logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("AddJSKwCategoryListApi").getlog()  # 初始化

class AddJSKwCategoryListApi():
    def addJSKwCategoryListFunction(self,kwargs):
        logger.info("addJSKwCategoryListFunction------------------->start")
        ruleName = parseRequestDatas("ruleName",kwargs) # 规则名
        category = parseRequestDatas("category",kwargs) # 类目
        country = parseRequestDatas("country",kwargs) # 国家
        if ruleName == "" or country == "" or category == "":
            logger.error("addJSKwCategoryListFunction------>ruleName or country or category is null")
            return "规则名或国家或类目为空!"
        url = DasApiUrl.addJsKwRule_url  # 请求地址
        # 请求参数
        addJsKwRule_param02 = DasApiInputParam.addJsKwRule_param02
        addJsKwRule_param01 = DasApiInputParam.addJsKwRule_param01
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i], kwargs)
                addJsKwRule_param02[keyList[i]] = value
        addJsKwRule_param01["args"] = json.dumps(addJsKwRule_param02)
        # 请求头信息
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url
        self.header = header
        self.formData = addJsKwRule_param01
        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("addJSKwCategoryListFunction------------------->end")
            return "规则创建成功"
        else:
            logger.error("addJSKwCategoryListFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,addJsKwRule_param01)

if __name__ == '__main__':
    print(AddJSKwCategoryListApi().addJSKwCategoryListFunction({"ruleName":"fsdfsdf01","country":"United States","category":"Arts; Crafts & Sewing"}))