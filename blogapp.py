#coding:utf-8
from flask import Flask


app = Flask(__name__)
app.config.from_pyfile('config.cfg')   #导入配置文件

import blog.view
from blog.data import *
'''
@app.route("/")
def index():
    return render_template("index.html")
'''
if __name__ == '__main__':
    db.create_all()
    app.run()
