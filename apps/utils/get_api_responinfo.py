'''
@File: get_api_respontime
@time:2021/9/25
@Author:majiaqin 170479
@Desc:获取接口返回数据信息的工具类
'''

import requests
import json

'''获取接口各种格式的响应时间'''
class Get_Api_Respontime():
    def __init__(self, resp):   # resp为接口返回数据
        self.resp = resp

    def get_api_respontime(self, index):
        self.index = index

        # 获取时分秒毫秒
        if self.index == 'hmsms':
            result = self.resp.elapsed
        # 获取毫秒
        elif self.index == 'ms':
            result = self.resp.elapsed.total_seconds()
        # 四舍五入到秒
        elif self.index == 's':
            result = self.resp.elapsed.seconds

        return result

'''获取接口返回数据大小'''
class Get_Api_Responsize():
    def __init__(self, resp):   # resp为接口返回数据
        self.resp = resp

    def get_api_responsize(self, pattern='B'):
        self.pattern = pattern
        size = len(self.resp.text)
        if self.pattern == 'B':
            return str(size)+'B'
        elif self.pattern == 'KB':
            return str(size/1024)+'KB'
        elif self.pattern == 'MB':
            return str(size/1024/1024) + 'MB'

if __name__ == '__main__':
    def getRDPEmployees():
        url = 'http://192.168.3.165:8018/fmis/wishPlatformRefund/selectWishRefundDetail'
        header = {'Content-Type': 'application/json',
                  'Authorization': '5df26666b185fbf0b3437482125d340e'}
        form = {"model":{"syncTime":"2021-09","accounts":["Bit by bit"],"sellers":[],"dataSource":2,"ids":[]},"current":1,"size":10}

        r = requests.post(url, headers=header, data=json.dumps(form))
        return r
    response = getRDPEmployees()
    print(Get_Api_Responsize(response).get_api_responsize())
    pass