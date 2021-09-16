'''
@File: brandWordsListApi.py
@time:2021/9/16
@Author:quanliu 181324
@Desc:工具助手-USpto商标词查询接口服务类
'''

from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("BrandWordsListAPi").getlog()  # 初始化

class BrandWordsListAPi():
    def brandWordsListFunction(self,paramStr):
        logger.info("brandWordsListFunction------------------->start")
        url = DasApiUrl.listNewUsTradeMark_url  # 请求地址
        # 请求参数
        listNewUsTradeMark_param03 = DasApiInputParam.listNewUsTradeMark_param03
        listNewUsTradeMark_param02 = DasApiInputParam.listNewUsTradeMark_param02
        listNewUsTradeMark_param01 = DasApiInputParam.listNewUsTradeMark_param01
        listNewUsTradeMark_param03["wordMark"] = paramStr
        listNewUsTradeMark_param02["search"] = listNewUsTradeMark_param03
        listNewUsTradeMark_param01["args"] = json.dumps(listNewUsTradeMark_param02)
        # 请求头信息
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url
        self.header = header
        self.formData = listNewUsTradeMark_param01
        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("brandWordsListFunction------------------->end")
            return "接口响应成功,接口返回值:{0}".format(resp.json()["rows"])
        else:
            logger.error("brandWordsListFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},接口类型:{2},请求参数:{3}".format(resp.json()["errorMsg"], url,listNewUsTradeMark_param01)


if __name__ == '__main__':
    print(BrandWordsListAPi().brandWordsListFunction("PODVUKZ"))