'''
@File: parameterConfigSelectApi.py
@time:2021/8/23
@Author:quanliu
@Desc:参数配置-取消开发备注查询接口服务
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.get_page_content_by_requests import get_page_content_by_requests
from logger import MyLog


# 实例化日志类
logger = MyLog("ParameterConfigQueryApi").getlog() # 初始化

class ParameterConfigQueryApi():
    def paramConfigQuery(self):
        logger.info("paramConfigQuery ---->start!")
        # 接口地址
        url = DasApiUrl.paramConfigSelect_url
        # 接口请求参数
        formData = DasApiInputParam.paramConfigQuery
        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")
        self.url = url
        self.formData = formData
        self.header = header
        # 响应值
        respResult = get_page_content_by_requests(self.url,self.header,self.formData)
        responseData = respResult.json()["result"]["cancelDevNotesInfoList"]
        if respResult.status_code == 200:
            logger.info("paramConfigQuery ---->end!")
            return "接口响应成功,接口返回值:{0}".format(responseData)
        else:
            logger.error("paramConfigQuery -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(respResult.json()["errorMsg"], url, formData)

