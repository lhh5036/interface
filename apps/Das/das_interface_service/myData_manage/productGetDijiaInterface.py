'''
@File: productGetDijiaInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:低价接口服务
'''
import requests

from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.myDataManage_inter_body import MyDataManageInterParam
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl

from apps.Das.logger import MyLog
import json

# 实例化日志类
logger = MyLog("ProductGetDijiaInterface").getlog() # 初始化

# 数据管理-低价接口
class ProductGetDijiaInterface():
    def productDetDiJia(self,paramStr): # 请求入参为用例名称，string类型的参数
        logger.info("productGenDijia ---->start!")
        if paramStr == "":
            logger.error("productGenDijia --> ReqParam:paramStr is null!")
            return "请求入参不能为空!"
        # 接口请求地址
        url = MyDataManageInterUrl.productGenDijia_url
        # 拼接接口请求入参
        paramSelect = MyDataManageInterParam.productGenDijia_select
        replaceRepSelect = paramSelect.replace("{asinUrlStr}",paramStr) #替换接口里面的参数
        reqParam = MyDataManageInterParam.productGenDijia_param
        reqParam["args"] = replaceRepSelect # 替换最外层参数
        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")
        self.header = header
        self.formData = reqParam
        self.url = url
        respResult = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if respResult.json()["success"] == True:
            return "接口响应成功,响应结果:{0}".format(respResult.json()["result"])
        else:
            logger.error("productGenDijia -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(respResult.json()["errorMsg"], url,reqParam)

        logger.info("productGenDijia ---->end!")


