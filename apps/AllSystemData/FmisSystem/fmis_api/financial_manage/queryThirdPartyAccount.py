# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: queryThirdPartyAccount
@time:2021/10/6
@Author:majiaqin 170479
@Desc:第三方收款-Payoneer收款列表数据接口
'''
from apps.AllSystemData.FmisSystem.fmis_api.fmisSystem_interface_param import FmisApiInputParam
from apps.AllSystemData.FmisSystem.fmis_api.fmisSystem_interface_url import FmisApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from loggerUtils import MyLog
from apps.AllSystemData.FmisSystem.assert_fmis.assert_file import Fmis_Unit_Assert
from apps.utils.get_api_responinfo import Get_Api_Responsize
import requests
import json

# 实例化日志类
logger = MyLog("QueryThirdPartyAccount").getlog()

# 查询Payoneer收款列表数据接口
class QueryThirdPartyAccount():
    def __init__(self, url=FmisApiUrl.payoneer_query_url,
                 header=Common_TokenHeader().common_header):
        # 初始化url和header
        self.url = url
        self.header = header

    def querythirdpartyaccount(self, paramDict):
        self.paramDict = paramDict

        logger.info("querythirdpartyaccount ---->start!")
        # 拼接接口请求入参
        if len(self.paramDict) == 0:
            logger.error("querythirdpartyaccount --> request parameters is wrong!")
            return "请求参数为空"
        form03 = FmisApiInputParam.thirdPartyAccount03
        i = 0
        try:
            for k in self.paramDict.keys():
                form03[k] = self.paramDict[k]
        except AttributeError:
            logger.error("The passed parameter is not in dictionary format!")
        form02 = FmisApiInputParam.thirdPartyAccount02
        form02["search"] = form03
        form01 = FmisApiInputParam.thirdPartyAccount01
        form01["args"] = json.dumps(form02, ensure_ascii=False)
        self.form = json.dumps(form01, ensure_ascii=False)
        print(self.form)
        resp = requests.post(self.url, headers=self.header, data=self.form.encode())
        print(resp.json())
        if Fmis_Unit_Assert(resp).fmis_unit_assert() == "False":
            msg = "接口响应失败,失败原因:{0},\n接口地址:{1},\n请求参数:{2}".format(resp.json(),
                                                                      self.url, self.form)
            logger.error(msg)
            return msg
        else:
            if int(Get_Api_Responsize(resp).get_api_responsize()[:-1]) > 2*1024*1024:
                msg = "api the response data is too large, Greater than 2MB!"
                logger.error(msg)
                return msg
            return "True"

if __name__ == '__main__':
    pass