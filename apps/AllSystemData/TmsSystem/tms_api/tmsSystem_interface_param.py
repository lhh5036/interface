'''
@File: tmsSystem_interface_param.py
@time:2022/6/8
@Author:quanliu 181324
@Desc:物流系统接口参数
'''

class TmsApiInputParam:
    # 物流配置-管理开发者账号
    developerAccountSelect_param01 = {"method":"searchDeveloperAccounts","args":"{0}"}
    developerAccountSelect_param02 = {"search":{0},"pageReqired":"true","limit":10,"offset":0,"sort":"id","order":"desc"}
    developerAccountSelect_param03 = {"shippingCompanyId":"","developerAccount":"","saleAccounts":""}


    # 物流规则-物流自定义规则-查询物流规则列表
    shippingruleSelect_param01 = {"method":"searchShippingRule","args":"{0}"}
    shippingruleSelect_param02 = {"search":{0},"pageReqired":"true","limit":10,"offset":0,"sort":"id","order":"desc"}
    shippingruleSelect_param03 = {"ruleNo":"","ruleName":"","statusList":[]}