'''
@File: associateSystemSkuApi.py
@time:2021/8/20
@Author:quanliu 181324
@Desc:我的数据-Amazon关联系统SKU接口
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.get_page_content_by_requests import get_page_content_by_requests
from logger import MyLog


# 实例化日志类
logger = MyLog("AssociateSystemSkuApi").getlog() # 初始化

# 关联系统SKU接口
class AssociateSystemSkuApi():
    def associateSystemSku(self,platform,searchType,paramList,systemSkuStr): # 调用该接口使用入参为list和字符串类型
        logger.info("associateSystemSku ---->start!")
        if len(paramList) == 0 or systemSkuStr == "" or searchType == "" or platform == "":
            logger.error("associateSystemSku --> request parameters is wrong!")
            return "请求参数为空"
        # 将入参list转为string类型
        paramStr = ""
        for i in range(len(paramList)):
            paramStr += "'"+paramList[i]+"',"
        # 拼接接口请求入参
        reqSelect = DasApiInputParam.associateSySku_select
        reqSelect["ids"] = paramList
        reqSelect["systemSku"] = systemSkuStr
        reqParam = DasApiInputParam.associateSySku_param
        reqParam["args"] = str(reqSelect)
        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")
        url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
        # 组装接口所需要的参数
        self.url = url
        self.formData = reqParam
        self.header = header
        resp = get_page_content_by_requests(self.url,self.header,self.formData)
        if resp.json()["success"] == True:
            logger.info("associateSystemSku ---->end!")
            return "关联系统SKU--接口响应成功"
        else:
            logger.error("associateSystemSku -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,reqParam)
