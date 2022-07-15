# -*- coding: utf-8 -*-
#!/usr/bin/python3

'''
@File:pmsSystem_interface_param.py
@time:2022/6/7
@Author:quanliu 181324
@Desc:采购系统接口请求入参
'''

class PmsApiInputParam:
    true = True
    null = None
    # 需求管理-采购建议
    purchaseSuggestion_param01 = {"method": "getPageList","args": "{0}"}
    purchaseSuggestion_param02 = {"search": {0}, "pageReqired": "true", "limit": 20,"offset": 0, "order": "desc"}
    purchaseSuggestion_param03 = {"status": "true", "articleNumber": "", "warehouseAttr": "", "stockUpFlag": "",
                                  "minAverageSaleQuantity": "null", "maxAverageSaleQuantity": "null",
                                  "minAvailableDays": "null", "maxAvailableDays": "null",
                                  "minPrepareGoodsDays": "null", "maxPrepareGoodsDays": "null",
                                  "minMaxGoodsDays": "null", "maxMaxGoodsDays": "null", "minSpecialGoodsDays": "null",
                                  "maxSpecialGoodsDays": "null", "minEstimateQuantity": "null",
                                  "maxEstimateQuantity": "null", "minSaleFrequency": "null", "maxSaleFrequency": "null"}

    purchaseRequire_param01 = {"method": "getPurchaseRequirePageList", "args": "{0}"}
    purchaseRequire_param02 = {"search": {0}, "pageReqired": true, "limit": 20, "offset": 0, "sort": "", "order": "desc"}
    purchaseRequire_param03 = {"warehouseAttr": "", "articleNumber": "", "skuName": "", "vendorName": "", "vendorCode": "",
                               "productManagers": [], "purchaseAssistanters": [], "skuLifeCyclePhaseList": ["New", "Normal", "Pending"],
                               "status": "", "purchaseRequireFlag": "", "confirmStatusList": [], "beginDate": "", "endDate": "",
                               "startConfirmNum": null, "endConfirmNum": null, "searchConditionSettings": []}
