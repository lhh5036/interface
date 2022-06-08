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