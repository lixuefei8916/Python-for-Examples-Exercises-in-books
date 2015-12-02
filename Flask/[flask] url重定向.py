#-*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)

# ie 访问 http://192.168.58.128:5000/projects
# 自动跳转到 http://192.168.58.128:5000/projects/
# ie 访问 http://192.168.58.128:5000/projects/
# ie回显 The project page

# ie 访问 http://192.168.58.128:5000/about
# ie回显 The about page
# ie 访问 http://192.168.58.128:5000/about/
# ie回显 Not Found
