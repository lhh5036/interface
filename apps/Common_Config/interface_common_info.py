'''
@File: interface_common_info.py
@time:2021/8/4
@Author:quanliu 181324
@Desc:公共接口配置文件
'''

class InterfaceCommonInfo:

    # 测试环境接口地址
    common_url = "http://192.168.3.162:80"

    # 预生产环境接口地址
    # common_url = "http://10.100.1.1:32100"

    # 生产环境接口地址
    # common_url = "http://10.100.1.1:31100"

    # 公共请求头参数
    common_header = {"Content-Type":"application/json","Authorization":"5df26666b185fbf0b3437482125d340e"}
