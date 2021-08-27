'''
@File: parameterConfigSave.py
@time:2021/8/23
@Author:quanliu
@Desc:数据分析-参数配置页面接口服务
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.myDataManage_inter_body import MyDataManageInterParam
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl
from apps.Das.logger import MyLog
import requests
import json

# 实例化日志类
logger = MyLog("ParameterConfigInterface").getlog() # 初始化
# 参数配置页面接口服务
class ParameterConfigInterface():
    def paramConfigFunction(self,paramStr):
        logger.info("paramConfigFunction ---->start!")
        if paramStr == "":
            logger.error("paramConfigFunction --> request parameters is wrong!")
            return "请求参数为空"

        # 接口地址
        url = MyDataManageInterUrl.paramConfigSave_url
        # 拼接接口请求入参
        reqSelect = MyDataManageInterParam.paramConfig_select
        reqSelectStr = reqSelect.replace("{notesInfoList}", paramStr)  # 替换参数
        reqParam = MyDataManageInterParam.paramConfig_param
        reqParam["args"] = reqSelectStr

        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")
        # 组装接口所需要的参数
        self.url = url
        self.formData = reqParam
        self.header = header

        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.formData))
        if resp.status_code == 200:
            logger.info("paramConfigFunction ---->end!")
            return "取消开发备注---保存接口响应成功"
        else:
            logger.error("paramConfigFunction -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,reqParam)

