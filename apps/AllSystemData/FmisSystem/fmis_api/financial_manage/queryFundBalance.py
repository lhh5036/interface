'''
@File: queryFundBalance
@time:2021/9/25
@Author:majiaqin 170479
@Desc:财务报表-查询资金余额日报表列表数据接口
'''
from apps.AllSystemData.FmisSystem.fmis_api.fmisSystem_interface_param import FmisApiInputParam
from apps.AllSystemData.FmisSystem.fmis_api.fmisSystem_interface_url import FmisApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from loggerUtils import MyLog
import requests
import json

# 实例化日志类
logger = MyLog("QueryFundBalance").getlog()

# 查询资金余额日报表列表数据接口
class QueryFundBalance():
    def __init__(self, url=FmisApiUrl.fundReport_query_url,
                 header=Common_TokenHeader.common_header):
        self.url =url
        self.header = header

    def queryfundbalance(self, keyList, paramList):
        self.keyList = keyList
        self.paramList = paramList

        logger.info("queryfundbalance ---->start!")
        # 拼接接口请求入参
        if len(self.paramList) == 0:
            logger.error("queryfundbalance --> request parameters is wrong!")
            return "请求参数为空"
        paramDict = FmisApiInputParam.fund_balance03.copy()
        form03 = FmisApiInputParam.fund_balance03.copy()
        i = 0
        for k in paramDict.keys():
            paramDict[k] = self.paramList[i]
            i += 1
        for kl in self.keyList:
            form03[kl] = paramDict[kl]
        # print(form03)
        form02 = FmisApiInputParam.fund_balance02
        form02["search"] = form03
        form01 = FmisApiInputParam.fund_balance01
        form01["args"] = json.dumps(form02, ensure_ascii=False)
        self.form = json.dumps(form01, ensure_ascii=False)
        # self.form = self.form.encode("utf-8").decode("latin1")
        print(self.form)
        resp = requests.post(self.url, headers=self.header, data=self.form.encode())
        print(resp.json())
        try:
            if resp.json()["success"] == True:
                logger.info("queryfundbalance ---->end!")
                return "查询资金余额日报表列表数据--接口响应成功"
            else:
                logger.error("queryfundbalance ----> response Data is wrong!")
                return "接口响应失败,失败原因:{0},\n接口地址:{1},\n请求参数:{2}".format(resp.json(),
                                                                      self.url, self.form)
        except KeyError:
            logger.error("queryfundbalance ----> {0}".format(resp.json()))
            return resp.json()