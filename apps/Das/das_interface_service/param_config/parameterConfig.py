'''
@File: parameterConfig.py
@time:2021/8/23
@Author:quanliu
@Desc:数据分析-参数配置页面接口服务
'''
from apps.Das.das_interface_service.das_common_header import DasCommonHeader
from apps.Das.das_interface_service.myDataManage_inter_body import MyDataManageInterParam
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl
from apps.Das.logger import MyLog
import requests
import json

# 实例化日志类
logger = MyLog("ParameterConfigInterface").getlog() # 初始化
# 参数配置页面接口服务
class ParameterConfigInterface():
    def paramConfigFunction(self,casename,paramStr):
        logger.info("paramConfigFunction ---->start!")
        if paramStr == "":
            logger.error("paramConfigFunction --> request parameters is wrong!")
            return "请求参数为空"

        # 接口地址
        url = MyDataManageInterUrl.paramConfig_url
        # 拼接接口请求入参
        reqSelect = MyDataManageInterParam.paramConfig_select
        reqSelectStr = reqSelect.replace("{notesInfoList}", paramStr)  # 替换参数
        reqParam = MyDataManageInterParam.paramConfig_param
        reqParam["args"] = reqSelectStr

        # 接口请求头
        header = DasCommonHeader().getDasCommonHeader()

        # 组装接口所需要的参数
        self.url = url
        self.formData = reqParam
        self.header = header

        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.formData))
        if resp.status_code == 200:
            return "{0}-->success".format(casename)
        else:
            logger.error("paramConfigFunction -->response Data is wrong!")
            return "{0}-->响应结果有误,接口地址:{1},接口入参:{2}".format(casename, url, paramStr)

        logger.info("paramConfigFunction ---->end!")