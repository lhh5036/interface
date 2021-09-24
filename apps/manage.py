'''
@File: manage.py
@time:2021/8/19
@Author:quanliu 181324
@Desc: 总入口
'''

from apps import create_app
from flask import render_template

app = create_app("dev")

# 接口调用入口
@app.route("/interfaceEntry")
def estoneInterfaceEntry():
    return render_template('system_entry.html')


if __name__ == '__main__':
    app.run(debug=True)