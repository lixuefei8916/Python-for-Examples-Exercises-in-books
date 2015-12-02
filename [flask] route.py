#-*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '******** index ********'

@app.route('/hello')
def hello():
	return 'Hello World'

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)

# ie 访问 http://192.168.58.128:5000/
# ie 访问 http://192.168.58.128:5000/hello