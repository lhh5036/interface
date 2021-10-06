'''
@File: mysql_handleOperator.py
@time:2021/8/19
@Author:quanliu 181324
@Desc:MySQL数据库操作工具类
'''


from apps.Common_Config.db_config import ReadConfig
from apps.Fmis.fmis_common_settting import Fmis_Common_Setting
import pymysql
import pprint

# mysql数据库具体操作实现类
class Mysql_handleOperator():
    def __init__(self, sqlinfo):    # sqlinfo为各系统通过db_config全局配置解析出来的数据库信息元组
        self.sqlinfo = sqlinfo
        self.host = self.sqlinfo[1]
        self.user = self.sqlinfo[2]
        self.password = self.sqlinfo[3]
        self.database = self.sqlinfo[0]
        self.port = 3306
        self.charset = "utf8"

        # # 连接数据库
        self.con = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port,
            charset=self.charset)

    def data_sql(self, methods, sql):
        self.methods = methods      # 声明增删改查哪种操作(insert/delete/update/select)
        self.sql = sql              # sql语句

        # 一次性查询数据库数据
        if self.methods == 'select':
            cursor = self.con.cursor() # 创建一个游标
            cursor.execute(self.sql)
            results = cursor.fetchall() # 返回全部结果
            cursor.close()
            self.con.close() # 关闭数据库连接
            return results

        # 新增修改删除数据库数据
        elif self.methods == 'insert' or self.methods == 'update' or self.methods == 'delete':
            cursor = self.con.cursor()
            try:
                cursor.execute(self.sql)
                self.con.commit()
            except:
                self.con.rollback() # 出现异常回滚
            cursor.close()
            self.con.close() # 关闭数据库连接

    # 使用流式游标分批次查询数据表数据
    def data_cursor_sql(self, sql):
        self.sql = sql  # sql语句

        cursor = pymysql.cursors.SSCursor(self.con)
        cursor.execute(self.sql)
        results = []
        while True:
            result = cursor.fetchone()
            results.append(result)
            # print(result)
            if not result:
                break
        results = [i for i in results if i != None]
        cursor.close()
        self.con.close()
        return results


if __name__ == '__main__':
    sql = "SELECT deposit_balance_cny, deposit_balance_usd FROM wish_platform_bill \
WHERE sync_time = '2021-07';"
    s = Mysql_handleOperator(Fmis_Common_Setting.fmis_mysql).data_sql("select", sql)
    pprint.pprint(s)