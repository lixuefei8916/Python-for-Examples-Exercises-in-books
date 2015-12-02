#-*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)

# ie 访问 http://192.168.58.128:5000/user/lixuefei
# ie页面返回 User lixuefei

# ie 访问 http://192.168.58.128:5000/post/777
# ie页面返回 Post 777

# 该方法如同 微博、推特，豆瓣等， url可以看出变量的用意

