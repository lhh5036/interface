'''
@File: smtProductSelectInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:我的数据SMT页面查询接口
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.myDataManage_inter_body import MyDataManageInterParam
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl

from apps.Das.logger import MyLog
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import requests
import json

# 实例化日志类
logger = MyLog("SmtProductSelectInterface").getlog() # 初始化
# 数据管理-我的数据SMT查询接口
class SmtProductSelectInterface():
    def smtQueryProductListing(self,kwargs):# 设置动态入参，参数类型为字典{"name":"Jack","age":18}
        logger.info("smtQueryProductListing ---->start!")
        # 接口地址
        url = MyDataManageInterUrl.smt_queryListing_url

        # 最内层参数
        smtProductInfoSelect = MyDataManageInterParam.smt_ProductInfo03

        keyList = [] #获取当前请求参数的keylist
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
        if len(keyList) != 0:
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i], kwargs)
                smtProductInfoSelect[keyList[i]] = value
        # 替换中间层
        smt_ProductInfo02 = MyDataManageInterParam.smt_ProductInfo02
        smt_ProductInfo02["search"] = smtProductInfoSelect

        # 替换外层
        smtProductInfoParam = MyDataManageInterParam.smt_ProductInfo01
        smtProductInfoParam["args"] = json.dumps(smt_ProductInfo02)

        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")
        self.url = url
        self.formData = smtProductInfoParam
        self.header = header

        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            return "接口响应成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("smtQueryProductListing -->response Data is wrong!")
            return "接口响应失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,smtProductInfoParam)

        logger.info("smtQueryProductListing ---->end!")


if __name__ == '__main__':
    print(SmtProductSelectInterface().smtQueryProductListing({}))