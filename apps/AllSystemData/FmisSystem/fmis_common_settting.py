# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: fmis_common_settting
@time:2021/10/6
@Author:majiaqin 170479
@Desc:财务系统全局配置
'''

from apps.Common_Config.db_config import Mysql_Db_Config

class Fmis_Common_Setting:
    # 测试环境MySQL数据库配置
    fmis_mysql = Mysql_Db_Config("erp_fmis_test")

    # 生产环境MySQL数据库配置
    # fmis_mysql = Mysql_Db_Config("erp_fmis_release")

if __name__ == '__main__':
    s = Fmis_Common_Setting.fmis_mysql
    print(s)