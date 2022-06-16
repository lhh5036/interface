'''
@File: queryCapitalCost
@time:2021/9/25
@Author:majiaqin 170479
@Desc:财务报表-查询资金支出日报表列表数据接口
'''
from apps.AllSystemData.FmisSystem.fmis_api.fmisSystem_interface_param import FmisApiInputParam
from apps.AllSystemData.FmisSystem.fmis_api.fmisSystem_interface_url import FmisApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader

from loggerUtils import MyLog


import requests
import json

# 实例化日志类
logger = MyLog("QueryCapitalCost").getlog()

# 查询资金支出日报表列表数据接口
class QueryCapitalCost():
    def __init__(self, url=FmisApiUrl.fundReport_query_url,
                 header=Common_TokenHeader().common_header):
        # 初始化url和header
        self.url = url
        self.header = header

    def querycapitalcost(self, paramList):
        self.paramList = paramList

        logger.info("querycapitalcost ---->start!")
        # 拼接接口请求入参
        if len(self.paramList) == 0:
            logger.error("querycapitalcost --> request parameters is wrong!")
            return "请求参数为空"
        form03 = FmisApiInputParam.capital_cost03
        i = 0
        for k in form03.keys():
            form03[k] = self.paramList[i]
            i += 1
        form02 = FmisApiInputParam.capital_cost02
        form02["search"] = form03
        form01 = FmisApiInputParam.capital_cost01
        form01["args"] = json.dumps(form02, ensure_ascii=False)
        self.form = json.dumps(form01, ensure_ascii=False)
        print(self.form)
        resp = requests.post(self.url, headers=self.header, data=self.form.encode())
        print(resp.json())
        print(Get_Api_Respontime(resp).get_api_respontime('ms'))
        try:
            if resp.json()["success"] == True:
                logger.info("querycapitalcost ---->end!")
                return "查询资金支出日报表列表数据--接口响应成功"
            else:
                logger.error("querycapitalcost ----> response Data is wrong!")
                return "接口响应失败,失败原因:{0},\n接口地址:{1},\n请求参数:{2}".format(resp.json(),
                                                                      self.url, self.form)
        except KeyError:
            logger.error("querycapitalcost ----> {0}".format(resp.json()))
            return resp.json()

