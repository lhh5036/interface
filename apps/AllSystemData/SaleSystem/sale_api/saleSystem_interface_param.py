'''
@File: saleSystem_interface_param.py
@time:2022/1/18
@Author:quanliu 181324
@Desc:订单系统接口入参
'''

class SaleApiInputParam:
    # 系统订单接口入参
    systemOrder_query_param01 = {"args": "{0}", "method": "listCustomerOrder"}
    systemOrder_query_param02 = {"search": {0}, "offset": 0, "limit": 200}
    systemOrder_query_param03 = {"salesSubsectorLeaderSet":[],"salesTeamLeaderSet":[],"salesmanSet":[],"salesJuniorSupervisorSet":[],"saleChannel":"","history":"false","orderStatus":"0","withoutProfitInfo":0}

