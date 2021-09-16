'''
@File: tradeMarkListApi.py
@time:2021/9/16
@Author:quanliu 181324
@Desc:工具助手-侵权查询接口服务类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.logger import MyLog
import json
import requests


# 实例化日志类
logger = MyLog("TradeMarkListApi").getlog() # 初始化
class TradeMarkListApi():
    def tradeMarkListFunction(self,tradeMark,paramStr):
        logger.info("tradeMarkListFunction------------------->start")
        if tradeMark == "":
            logger.error("tradeMarkListFunction------------------->The query region is empty!")
            return "请选择查询地区!"
        if tradeMark == "US":
            url = DasApiUrl.listUsTradeMark_url  # 请求地址
        elif tradeMark == "EU":
            url = DasApiUrl.listEuTradeMark_url  # 请求地址
        # 请求参数
        listTradeMark_param03 = DasApiInputParam.listTradeMark_param03
        listTradeMark_param02 = DasApiInputParam.listTradeMark_param02
        listTradeMark_param01 = DasApiInputParam.listTradeMark_param01
        listTradeMark_param03["keyword"] = paramStr
        listTradeMark_param02["search"] = listTradeMark_param03
        listTradeMark_param01["args"] = json.dumps(listTradeMark_param02)
        # 请求头信息
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url
        self.header = header
        self.formData = listTradeMark_param01
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("tradeMarkListFunction------------------->end")
            return "接口响应成功,接口返回值:{0}".format(resp.json()["rows"])
        else:
            logger.error("tradeMarkListFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},接口类型:{2},请求参数:{3}".format(resp.json()["errorMsg"], url,listTradeMark_param01)

if __name__ == '__main__':
    print(TradeMarkListApi().tradeMarkListFunction("US","TSDR"))


