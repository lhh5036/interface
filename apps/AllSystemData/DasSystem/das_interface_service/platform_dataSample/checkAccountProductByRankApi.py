'''
@File: checkAccountProductByRankApi.py
@time:2021/8/26
@Author:quanliu
@Desc:校验哪些产品已经被认领过接口类
'''
from apps.AllSystemData.DasSystem.das_interface_service.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.logger import MyLog
import json
import requests


# 实例化日志类
logger = MyLog("CheckAccountProductByRankApi").getlog() # 初始化
# 校验哪些产品已经被认领过接口类
class CheckAccountProductByRankApi():
    def checkProductByRankFunction(self,platform,searchType,salechannelname,idsList):
        logger.info("checkProductByRankFunction------>start")
        if salechannelname == "" or len(idsList) == 0:
            logger.error("checkProductByRankFunction --> request parameters is wrong!")
            return "请求参数为空"

        # 拼接内层参数
        checkAccountProductByRank02 = DasApiInputParam.checkAccountProductByRank02
        checkAccountProductByRank02["saleChannel"] = salechannelname
        checkAccountProductByRank02["baseIdList"] = idsList
        # 拼接外层参数
        checkAccountProductByRank01 = DasApiInputParam.checkAccountProductByRank01
        checkAccountProductByRank01["args"] = json.dumps(checkAccountProductByRank02)
        # 获取请求头
        header = Common_TokenHeader().token_header("new","181324")
        url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
        # 拼接请求地址
        self.url = url
        self.fromData = checkAccountProductByRank01
        self.header = header

        responseResult = requests.post(url=self.url,headers=self.header,data=json.dumps(self.fromData))
        if responseResult.json()["success"] == True:
            logger.info("checkProductByRankFunction------>end")
            return "接口响应成功,响应结果:{0}".format(responseResult.json()["result"])
        else:
            logger.error("checkProductByRankFunction -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(responseResult.json()["errorMsg"],url,checkAccountProductByRank01)



