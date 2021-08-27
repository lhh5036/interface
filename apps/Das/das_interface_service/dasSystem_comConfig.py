'''
@File: dasSystem_comConfig.py
@time:2021/8/5
@Author:quanliu 181324
@Desc:数据管理页面涉及ES索引，SQL语句等
'''


class Das_Common_Config:
    # ES索引
    # 数据管理（所有页面）
    amazon_account_product_info = "amazon_account_product_info"  # 我的数据-亚马逊
    smt_account_product_info = "smt_account_product_info"  # 我的数据-smt
    ali_account_product_info = "ali_account_product_info"  # 我的数据-1688
    ebay_account_product_info = "ebay_account_product_info"  # 我的数据-ebay
    shopee_account_product_info = "shopee_account_product_info"  # 我的数据-shopee


    # 数据采集（所有页面）
    amazon_base_listing = "amazon_base_listing"
    smt_base_listing = "smt_base_listing"
    ali_base_listing = "ali_base_listing"
    ebay_base_listing = "ebay_base_listing"
    shopee_base_listing = "shopee_base_listing"