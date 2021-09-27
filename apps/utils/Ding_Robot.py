'''
@File: Ding_Robot
@time:2021/9/27
@Author:majiaqin 170479
@Desc:钉钉机器人工具类
'''

# -*- coding:utf-8 -*-
#!/usr/bin/python3

import requests
import json

# 调试用url
url_test = "https://oapi.dingtalk.com/robot/send?access_token=112b226a43ef532c7456a5c262ddac21a7ee21d05229052aaf140c8bd3c6b90c"

# 调用钉钉机器人(钉钉机器人调用需要白名单，需要到测试服务器上进行调试)
class DingHelp():
    """python无法处理false，因此需要先给false赋值并设置为全局变量"""
    global false
    false = ''
    def __init__(self, url, message, mobile=[], isAtAll=false):
        """设置钉钉机器人的webhook"""
        self.url = url
        self.message = message
        self.mobile = mobile            # mobile为列表格式
        self.isAtAll = isAtAll

        self.header = {'Content-Type': 'application/json'}
        self.form = {"msgtype": "text",
                    "text": {"content": ""},
                    "at": {"atMobiles": self.mobile,
                    "isAtAll": self.isAtAll}}

        """修改请求参数中的消息(context)和手机号(atMobiles)"""
        self.form["text"]["content"] = self.message
        self.form["at"]["atMobiles"] = self.mobile

    def dinghelp(self):

        """根据url，headers&data调用接口并返回数据"""
        r = requests.post(self.url, headers=self.header, data=json.dumps(self.form))
        return r.json()