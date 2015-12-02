#-*- coding: utf-8 -*-
# render_template渲染， 展示templates文件夹中的html模板
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html',name=name)

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)

'''
目录结构
/view.py			[python文件]
/templates
    /hello.html

1. 在view.py同目录下， 创建文件夹唉 templates
2. vi hello.html 在 template【s】文件夹下    
'''

# ie 访问 http://192.168.58.128:5000/hello/
# ie 回显 templates/hello.html中内容
