'''
@File: addCategoryTaskListApi.py
@time:2021/9/15
@Author:quanliu 181324
@Desc:任务中心-分类监控-新增分类接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from flask import current_app as app
import json


@api_assemble_new()
def addCategoryTaskListFunction(kwargs):
    app.logger.info("addCategoryTaskListFunction------------------->start")
    country = parseRequestDatas("country", kwargs)
    saleChannel = parseRequestDatas("saleChannel", kwargs)
    listNodes = parseRequestDatas("listNodes",kwargs)
    categoryUrl = parseRequestDatas("categoryUrl", kwargs)
    categoryName = parseRequestDatas("categoryName", kwargs)
    listNodeName = parseRequestDatas("listNodeName", kwargs)

    if country == "" or saleChannel == "" or categoryUrl == "" or categoryName == "":
        app.logger.error("addCategoryTaskListFunction---------->Input Params is null")
        return "请求参数为空!"
    # 获取请求参数
    addCategoryTask_param02 = DasApiInputParam.addCategoryTask_param02
    addCategoryTask_param01 = DasApiInputParam.addCategoryTask_param01
    # 获取请求地址
    addTask_url = DasApiUrl.addTask_url
    addCategoryTask_param02["listNodes"] = listNodes
    addCategoryTask_param02["country"] = country
    addCategoryTask_param02["saleChannel"] = saleChannel
    addCategoryTask_param02["categoryUrl"] = categoryUrl
    addCategoryTask_param02["categoryName"] = categoryName
    addCategoryTask_param02["listNodeName"] = listNodeName
    addCategoryTask_param01["args"] = json.dumps(addCategoryTask_param02)
    return addTask_url,addCategoryTask_param01

if __name__ == '__main__':
    print(addCategoryTaskListFunction({"listNodes":["7141123011","7147440011","1040660","1045024","2346728011"],"categoryUrl":"https://www.amazon.com/s?k=clothing%2C+shoes+%26+jewelry&i=fashion&bbn=1045024&rh=n%3A7141123011%2Cn%3A%217141124011%2Cn%3A7147440011%2Cn%3A1040660%2Cn%3A1045024%2Cn%3A2346728011&dc&language=en_US&qid=1567610518&rnid=1045024&ref=sr_nr_n_5&language=en_US","categoryName":"Work","country":"US","taskType":1,"listNodeName":["Clothing, Shoes & Jewelry","Women","Clothing","Dresses","Work"],"saleChannel":"Amazon"}))
