# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: usermgt_common_setting
@time:2022/3/25
@Author:majiaqin 170479
@Desc:用户系统全局配置
'''

from apps.Common_Config.db_config import Mysql_Db_Config

class Usermgt_Common_Setting:
    # 测试环境MySQL数据库配置
    usermgt_mysql = Mysql_Db_Config("erp_usermgt_new_test")

    # 生产环境MySQL数据库配置
    # usermgt_mysql = Mysql_Db_Config("erp_usermgt_new_release")


if __name__ == '__main__':
    print(Usermgt_Common_Setting.usermgt_mysql)