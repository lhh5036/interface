'''
@File: Ding_Webhook
@time:2021/9/27
@Author:majiaqin 170479
@Desc:钉钉群机器人webhook汇总(供调用)
'''

# -*- coding:utf-8 -*-
#!/usr/bin/python3

'''
钉钉群机器人webhook汇总(供调用)
'''

class WebHook:
    '''广告系统'''
    advert_url = "https://oapi.dingtalk.com/robot/send?access_token=43880a7313920fdce476d06c06032d499b4d5f27bacc28be7637904154efbb56"

    '''销售订单系统'''
    sale_url = "https://oapi.dingtalk.com/robot/send?access_token=2a62f9a1415ffd5d50f4d49b690102a4be09d0f6850b2bdb95f04b18308bd083"

    '''产品系统'''
    product_url = "https://oapi.dingtalk.com/robot/send?access_token=85dfd5c7abf0a9498c32f00f6afb544d6a0dd3c25ca76d98809535b10ab21a7e"

    '''财务系统'''
    fmis_url = "https://oapi.dingtalk.com/robot/send?access_token=fb387426c8a1b021ea13068a9e8c462945d47065be35b487564eea88c31e1933"

    '''刊登系统'''
    espublish_url = "https://oapi.dingtalk.com/robot/send?access_token=48ef05bac65da22fe78e165ffa5197575a3478654d51ddfff143b126dccc435f"

    '''物流系统'''
    wl_url = "https://oapi.dingtalk.com/robot/send?access_token=2e0f11bb005bfbf67797c738f7455ad9a696e43c693229a2603aba2b35a72eb8"

    '''数据分析系统'''
    das_url = "https://oapi.dingtalk.com/robot/send?access_token=407400cf80d86ebd3737142b35b7002783a5d494a44b4940da7600a24e1931aa"

    '''采购系统'''
    pms_url = "https://oapi.dingtalk.com/robot/send?access_token=b5f057042c7fcfb580c8a78b183baa083d51c83e1662c4c21fd646c02441d8b5"

    '''客服系统'''
    custom_url = "https://oapi.dingtalk.com/robot/send?access_token=da2f463c047e3edb982d849cfd698f317ada5cd667b2400291353bb6f5bc002f"

    '''脚本测试群'''
    test_url = "https://oapi.dingtalk.com/robot/send?access_token=112b226a43ef532c7456a5c262ddac21a7ee21d05229052aaf140c8bd3c6b90c"