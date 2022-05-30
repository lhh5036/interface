'''
@File: addStoreTaskListApi.py
@time:2021/9/15
@Author:quanliu 181324
@Desc:任务中心-店铺监控-新增店铺接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.get_page_content_by_requests import get_page_content_by_requests
from apps.logger import MyLog
import json


# 实例化日志类
logger = MyLog("AddStoresTaskListApi").getlog() # 初始化
class AddStoresTaskListApi():
    def addStoresTaskListFunction(self,kwargs):
        logger.info("addStoresTaskListFunction------------------->start")
        country = parseRequestDatas("country", kwargs)
        saleChannel = parseRequestDatas("saleChannel",kwargs)
        sellerUrl = parseRequestDatas("sellerUrl",kwargs)
        sellerName = parseRequestDatas("sellerName",kwargs)
        notesInfo = parseRequestDatas("notesInfo",kwargs)
        if country == "" or saleChannel == "" or sellerUrl == "" or sellerName == "":
            logger.error("addStoresTaskListFunction---------->Input Params is null")
            return "请求参数为空!"
        # 获取请求参数
        addStoreTask_param02 = DasApiInputParam.addStoreTask_param02
        addStoreTask_param01 = DasApiInputParam.addStoreTask_param01
        # 获取请求地址
        addTask_url = DasApiUrl.addTask_url
        # 获取请求头信息
        header = Common_TokenHeader().token_header("new", "181324")
        addStoreTask_param02["country"] = country
        addStoreTask_param02["saleChannel"] = saleChannel
        addStoreTask_param02["sellerUrl"] = sellerUrl
        addStoreTask_param02["sellerName"] = sellerName
        addStoreTask_param02["notesInfo"] = notesInfo

        addStoreTask_param01["args"] = json.dumps(addStoreTask_param02)
        self.url = addTask_url
        self.header = header
        self.formData = addStoreTask_param01
        resp = get_page_content_by_requests(self.url,self.header,addStoreTask_param01)
        if resp.json()["success"] == True:
            logger.info("addStoresTaskListFunction------------------->end")
            return "任务添加成功"
        else:
            logger.error("addStoresTaskListFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], addTask_url,addStoreTask_param01)

if __name__ == '__main__':
    print(AddStoresTaskListApi().addStoresTaskListFunction({}))