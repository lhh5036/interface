'''
@File: releaseProductApi.py
@time:2021/8/7
@Author:quanliu 181324
@Desc:我的数据Amazon-释放产品接口
'''
from apps.AllSystemData.DasSystem.das_interface_service.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.logger import MyLog
import requests
import json


# 实例化日志类
logger = MyLog("releaseProductInfoApi").getlog() # 初始化
# 我的数据Amazon-释放产品接口
class releaseProductInfoApi():
    def releaseProductInfo(self,platform,searchType,paramList): # 调用该接口使用入参为list
        paramStr = ""
        logger.info("releaseProductInfo ---->start!")
        if len(paramList) == 0:
            logger.error("releaseProductInfo --> request parameters is wrong!")
            return "请求参数为空"

        # 将入参list转为string类型
        for i in range(len(paramList)):
            paramStr += "'"+paramList[i]+"',"
        # 拼接接口请求入参
        reqSelect = DasApiInputParam.releaseProductInfo_select
        reqSelectStr = reqSelect.replace("{ids}",paramStr) # 替换参数
        reqParam = DasApiInputParam.releaseProductInfo_param
        reqParam["args"] = reqSelectStr
        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")
        # 组装接口所需要的参数
        url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
        self.url = url
        self.formData = reqParam
        self.header = header
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("releaseProductInfo ---->end!")
            return "释放产品---接口响应成功"
        else:
            logger.error("releaseProductInfo -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,reqParam)



