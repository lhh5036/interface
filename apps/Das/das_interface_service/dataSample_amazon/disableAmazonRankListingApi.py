'''
@File: disableAmazonRankListingApi.py
@time:2021/8/27
@Author:quanliu
@Desc:数据采集-Amazon禁用接口类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import MyDataManageInterParam
from apps.Das.das_interface_service.dasSystem_interface_url import MyDataManageInterUrl
from apps.Das.logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("AmazonDisableRankListingApi").getlog() # 初始化
class AmazonDisableRankListingApi():
    def disableRankListingFunction(self,paramList): # 请求参数为List
        logger.info("disableRankListingFunction--------->start")
        if len(paramList) == 0:
            logger.error("disableRankListingFunction----->InputParameter is null")
            return "请求参数为空!"
        # 对入参进行参数化
        amazon_disableProduct02 = MyDataManageInterParam.amazon_disableProduct02
        amazon_disableProduct02["ids"] = paramList
        amazon_disableProduct01 = MyDataManageInterParam.amazon_disableProduct01
        amazon_disableProduct01["args"] = json.dumps(amazon_disableProduct02)
        # 请求地址
        url = MyDataManageInterUrl.amazon_disableProduct_url
        # 获取请求头信息
        header = Common_TokenHeader().token_header("new","181324")
        self.header = header
        self.formData = amazon_disableProduct01
        self.url = url
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.status_code == 200:
            logger.info("disableRankListingFunction-------->end")
            return "禁用接口响应成功"
        else:
            logger.error("disableRankListingFunction--------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,amazon_disableProduct01)


if __name__ == '__main__':
    print(AmazonDisableRankListingApi().disableRankListingFunction(["3fcb5478-06d4-11ec-9b70-0000000001ca","6deea63a-06b6-11ec-b2a0-0000000003ca"]))