'''
@File: parameterConfigSaveApi.py
@time:2021/8/23
@Author:quanliu
@Desc:数据分析-参数配置页面接口服务
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.get_page_content_by_requests import get_page_content_by_requests
from apps.logger import MyLog

# 实例化日志类
logger = MyLog("ParameterConfigApi").getlog() # 初始化
# 参数配置页面接口服务
class ParameterConfigApi():
    def paramConfigFunction(self,paramStr):
        logger.info("paramConfigFunction ---->start!")
        if paramStr == "":
            logger.error("paramConfigFunction --> request parameters is wrong!")
            return "请求参数为空"

        # 接口地址
        url = DasApiUrl.paramConfigSave_url
        # 拼接接口请求入参
        reqSelect = DasApiInputParam.paramConfig_select
        reqSelectStr = reqSelect.replace("{notesInfoList}", paramStr)  # 替换参数
        reqParam = DasApiInputParam.paramConfig_param
        reqParam["args"] = reqSelectStr

        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")
        # 组装接口所需要的参数
        self.url = url
        self.formData = reqParam
        self.header = header
        resp = get_page_content_by_requests(self.url, self.header, self.formData)
        if resp.status_code == 200:
            logger.info("paramConfigFunction ---->end!")
            return "取消开发备注---保存接口响应成功"
        else:
            logger.error("paramConfigFunction -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,reqParam)

