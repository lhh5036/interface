'''
@File: productGetTongkuanApi.py
@time:2021/8/23
@Author:quanliu
@Desc:产品同款接口服务
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.get_page_content_by_requests import get_page_content_by_requests
from apps.logger import MyLog

# 实例化日志类
logger = MyLog("ProductGetTongkuanApi").getlog() # 初始化

# 数据管理-同款接口服务
class ProductGetTongkuanApi():
    def productGetTongkuan(self,paramStr):
        logger.info("productGetTongkuan ---->start!")
        if paramStr == "":
            logger.error("productGetTongkuan --> ReqParam:paramStr is null!")
            return "请求入参不能为空!"

        # 接口请求地址
        url = DasApiUrl.productGenTongkuan_url

        # 拼接接口请求入参
        paramSelect = DasApiInputParam.productGenTongkuan_select
        paramSelect["asinUrlStr"] = paramStr
        reqParam = DasApiInputParam.productGenTongkuan_param
        reqParam["args"] = str(paramSelect)  # 替换最外层参数

        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")

        self.header = header
        self.formData = reqParam
        self.url = url

        respResult = get_page_content_by_requests(self.url, self.header,self.formData)
        if respResult.json()["success"] == True:
            logger.info("productGetTongkuan ---->end!")
            return "接口响应成功,响应结果:{0}".format(respResult.json()["result"])
        else:
            logger.error("productGetTongkuan -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(respResult.json()["errorMsg"], url,reqParam)


