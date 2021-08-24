'''
@File: smtProductSelectInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:我的数据SMT页面查询接口
'''
from apps.Das.das_interface_service.das_common_header import DasCommonHeader
from apps.Das.das_interface_service.myDataManage_inter_body import MyDataManageInterParam
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl

from apps.Das.logger import MyLog
import requests
import json

# 实例化日志类
logger = MyLog("SmtProductSelectInterface").getlog() # 初始化
# 数据管理-我的数据SMT查询接口
class SmtProductSelectInterface():
    def smtQueryProductListing(self,casename,kwargs):# 设置动态入参，参数类型为字典{"name":"Jack","age":18}
        logger.info("smtQueryProductListing ---->start!")
        # 接口地址
        url = MyDataManageInterUrl.querySmtListing_url
        # 请求入参
        mainSku = parseRequestDatas("mainSku", kwargs) # 主SKU
        associatedSystemSku = parseRequestDatas("associatedSystemSku", kwargs) # 关联系统SKU
        skuMapStr = parseRequestDatas("skuMapStr", kwargs) # 试卖SKU
        brand = parseRequestDatas("brand", kwargs) # 品牌
        keywords = parseRequestDatas("keywords", kwargs) # 关键词
        startPrice = parseRequestDatas("startPrice", kwargs) # 价格最小值
        endPrice = parseRequestDatas("endPrice", kwargs)# 价格
        dataStatus = parseRequestDatas("dataStatus", kwargs)
        infringementReviewer = parseRequestDatas("infringementReviewer", kwargs) # 侵权审核人
        productId = parseRequestDatas("productId", kwargs) # itemID
        endOrders = parseRequestDatas("endOrders", kwargs) # 结束orders
        developmentStatus = parseRequestDatas("developmentStatus", kwargs) # 开发状态
        startOrders = parseRequestDatas("startOrders", kwargs) # 开始orders
        Reviews = parseRequestDatas("Reviews", kwargs) # 累计评论数
        rating = parseRequestDatas("rating", kwargs) # 评论星级
        merchantName = parseRequestDatas("merchantName",kwargs) # 店铺
        startCrawlTime = parseRequestDatas("startCrawlTime",kwargs) # 爬取开始时间
        endCrawlTime = parseRequestDatas("endCrawlTime",kwargs) # 爬取结束时间
        systemSku = parseRequestDatas("systemSku",kwargs)# 系统SKU
        distributor = parseRequestDatas("distributor",kwargs) # 分配人
        startDistributionTime = parseRequestDatas("startDistributionTime",kwargs) # 分配时间
        endDistributionTime = parseRequestDatas("endDistributionTime",kwargs) # 分配时间
        startInfringementReviewTime = parseRequestDatas("startInfringementReviewTime",kwargs)  # 侵权审核开始时间
        endInfringementReviewTime = parseRequestDatas("endInfringementReviewTime",kwargs) # 侵权审核结束时间
        auditStatus = parseRequestDatas("auditStatus",kwargs) # 审核状态


        # 获取请求参数的基本格式
        repSelect = MyDataManageInterParam.smtProductInfo_select
        # 替换字符串里面的参数
        replaceRepSelect = repSelect.replace("{mainSku}", mainSku).replace("{associatedSystemSku}", associatedSystemSku).replace("{skuMapStr}", skuMapStr).replace("{brand}", brand).replace("{keywords}", keywords).replace("{startPrice}", startPrice).replace("{endPrice}", endPrice).replace("{dataStatus}",dataStatus).replace(
            "{infringementReviewer}", infringementReviewer).replace("{productId}", productId).replace("{endOrders}", endOrders).replace("{developmentStatus}",developmentStatus).replace("{startOrders}",startOrders).replace("{Reviews}", Reviews).replace("{rating}", rating).replace("{merchantName}", merchantName).\
            replace("{startCrawlTime}",startCrawlTime).replace("{endCrawlTime}",endCrawlTime).replace("{systemSku}",systemSku).replace("{distributor}",distributor).replace("{startDistributionTime}",startDistributionTime).replace("{endDistributionTime}",endDistributionTime).replace("{startInfringementReviewTime}",startInfringementReviewTime)\
            .replace("{endInfringementReviewTime}",endInfringementReviewTime).replace("{auditStatus}",auditStatus)
        # 替换最外层参数
        reqParam = MyDataManageInterParam.smtProductInfo_param
        reqParam["args"] = replaceRepSelect  # 确保最后一层是dict格式

        # 接口请求头
        header = DasCommonHeader().getDasCommonHeader("new","181324")
        self.url = url
        self.formData = reqParam
        self.header = header

        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            return "{0}-->success".format(casename)
        else:
            logger.error("smtQueryProductListing -->response Data is wrong!")
            return "{0}-->响应结果有误,接口地址:{1},接口入参:{2}".format(casename, url, kwargs)

        logger.info("smtQueryProductListing ---->end!")

# 解析每一个入参
def parseRequestDatas(keyname, kwargs):
    if kwargs.get(keyname) is None:
        valueName = ""
    else:
        valueName = kwargs.get(keyname)
    return valueName

