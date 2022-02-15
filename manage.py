'''
@File: manage.py
@time:2021/8/19
@Author:quanliu 181324
@Desc: 总入口
'''

from apps import create_app
from flask import render_template,request,redirect,url_for
app = create_app("dev")

# 接口调用入口
@app.route("/projectEntry/<name>")
def estoneInterfaceEntry(name):
    return render_template("system_entry.html",username = name)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user = request.form['name']
        return redirect(url_for('estoneInterfaceEntry',name = user))
    else:
        user = request.args.get("name")
        return redirect(url_for('estoneInterfaceEntry',name = user))

if __name__ == '__main__':
    app.run(debug=True)