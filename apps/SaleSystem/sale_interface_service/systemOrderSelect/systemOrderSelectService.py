'''
@File: systemOrderSelectService.py
@time:2022/1/18
@Author:quanliu 181324
@Desc:系统订单查询接口
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.SaleSystem.sale_interface_service.sale_publicCommonParamService import SalePublicCommonParamServiceClass
from apps.SaleSystem.sale_interface_service.sale_publicCommonUrlService import SalePublicCommonUrlServiceClass
from apps.logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("SystemOrderQueryApi").getlog()  # 初始化

# 系统订单查询接口
class SystemOrderQueryApi():
    def systemOrderQueryFun(self,platform,searchType,paramMap=None):
        logger.info("systemOrderQueryFun  ----->start!")
        if platform == "" or searchType == "":
            logger.error("systemOrderQueryFun ------>request parameter(platform or searchType) is wrong!")
            return "请求参数为空"

        # 获取url
        url = SalePublicCommonUrlServiceClass().getApiUrl("SMT","listCustomerOrder")
        # 获取参数
        param03,param02,param01 = SalePublicCommonParamServiceClass().getApiInputParam("SMT","listCustomerOrder")
        param03["saleChannel"] = platform
        param02["search"] = param03
        param01["args"] = json.dumps(param02)
        # 获取接口请求头
        header = Common_TokenHeader().token_header("old", "181324")
        # 组装接口所需要的参数
        self.url = url
        self.headers = header
        self.formData = json.dumps(param01)
        resp = requests.post(url=self.url,headers=self.headers,data=self.formData)
        if resp.json()["success"] == True:
            logger.info("systemOrderQueryFun---->end!")
            return "接口响应成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("systemOrderQueryFun -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], url, param01)


if __name__ == '__main__':
    SystemOrderQueryApi().systemOrderQueryFun("SMT","listCustomerOrder")