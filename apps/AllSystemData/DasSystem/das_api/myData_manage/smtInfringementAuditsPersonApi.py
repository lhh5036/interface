'''
@File: smtInfringementAuditsPersonApi.py
@time:2021/8/30
@Author:quanliu
@Desc:SMT获取侵权审核人接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.logger import MyLog
import requests
import json


# 实例化日志类
logger = MyLog("SmtInfringementAuditsPersonApi").getlog() # 初始化
# 数据管理-我的数据SMT查询接口
class SmtInfringementAuditsPersonApi():
    def smtInfringementAuditsPersonFun(self):# 设置动态入参，参数类型为字典{"name":"Jack","age":18}
        logger.info("smtInfringementAuditsPersonFun------------------>start")
        url = DasApiUrl.smt_infringementAuditPerson_url # 获取请求地址
        formData = DasApiInputParam.infringementAduitsPerson_param # 获取请求参数
        header = Common_TokenHeader().token_header("new","181324") # 获取请求头信息
        self.url = url
        self.formData = formData
        self.header = header
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.status_code == 200:
            logger.info("smtInfringementAuditsPersonFun------------------>end")
            return "接口响应成功,响应结果:{0}".format(resp.json()["result"])
        else:
            logger.error("smtInfringementAuditsPersonFun -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,formData)


if __name__ == '__main__':
    print(SmtInfringementAuditsPersonApi().smtInfringementAuditsPersonFun())