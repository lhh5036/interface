'''
@File: smtInfringementAuditsPersonApi.py
@time:2021/8/30
@Author:quanliu
@Desc:SMT获取侵权审核人接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app


# 数据管理-我的数据SMT查询接口
@api_assemble_new()
def smtInfringementAuditsPersonFun():# 设置动态入参，参数类型为字典{"name":"Jack","age":18}
    app.logger.info("smtInfringementAuditsPersonFun------------------>start")
    url = DasApiUrl.smt_infringementAuditPerson_url # 获取请求地址
    formData = DasApiInputParam.infringementAduitsPerson_param # 获取请求参数
    return url,formData
