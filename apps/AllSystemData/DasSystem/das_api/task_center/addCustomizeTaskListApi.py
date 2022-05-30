'''
@File: addCustomizeTaskListApi.py
@time:2021/9/2
@Author:quanliu
@Desc:任务中心-自定义采集-新增采集接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.get_page_content_by_requests import get_page_content_by_requests
from logger import MyLog
import json



# 实例化日志类
logger = MyLog("AddCustomizeTaskListingApi").getlog() # 初始化
class AddCustomizeTaskListingApi():
    def addCustomizeTaskListingFunction(self,itemUrlList,saleChannel,country):
        logger.info("addCustomizeTaskListingFunction------------------->start")
        if len(itemUrlList) == 0 or saleChannel == "" or country == "":
            logger.error("addCustomizeTaskListingFunction------>InputParam is null")
            return "请求参数为空!"
        # 获取请求地址
        url = DasApiUrl.addCustomizeTask_url
        # 获取请求参数
        addCustomizeTask02 = DasApiInputParam.addCustomizeTask02
        addCustomizeTask02["itemUrlList"] = itemUrlList
        addCustomizeTask02["saleChannel"] = saleChannel
        addCustomizeTask02["country"] = country
        addCustomizeTask01 = DasApiInputParam.addCustomizeTask01
        addCustomizeTask01["args"] = json.dumps(addCustomizeTask02)
        # 请求头
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url
        self.formData = addCustomizeTask01
        self.header = header
        resp = get_page_content_by_requests(self.url,self.header,self.formData)
        if resp.json()["success"] == True:
            logger.info("addCustomizeTaskListingFunction------------------->end")
            return "接口响应成功,响应结果:{0}".format(resp.json()["result"])
        else:
            logger.error("addCustomizeTaskListingFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},接口类型:{2},请求参数:{3}".format(resp.json()["errorMsg"], url,addCustomizeTask01)


if __name__ == '__main__':
    print(AddCustomizeTaskListingApi().addCustomizeTaskListingFunction(["https://www.aliexpress.com/item/1005002065663912.html?spm=a2g0o.store_pc_groupList.8148356.3.17136ae1hUFRSF"],"SMT","US"))
