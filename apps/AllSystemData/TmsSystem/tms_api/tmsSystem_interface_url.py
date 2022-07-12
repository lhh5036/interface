'''
@File: tmsSystem_interface_url.py
@time:2022/6/8
@Author:quanliu 181324
@Desc: 物流系统接口地址
'''


from apps.Common_Config.interface_common_info import InterfaceCommonInfo


class TmsApiUrl:
    # 物流配置-管理开发者账号查询
    developerAccountSelect_url = InterfaceCommonInfo.common_url + "/logistics-engine-service/developeraccount"


    # 物流规则-物流自定义规则-查询物流规则列表
    shippingruleSelect_url = InterfaceCommonInfo.common_url + "/logistics-engine-service/shippingrule"