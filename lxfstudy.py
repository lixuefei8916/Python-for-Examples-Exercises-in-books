# -*- coding: utf-8 -*-

'''
x
# ---------------------------------------------------------------------

def sjx(x):
	y = range(x)
	n = x*2+1           # How many space character after the first *?
	for i in y:
		tmp = n/2-i
		print ' ' * tmp,'* ' * i,' ' * tmp

sjx(10)


# ---------------------------------------------------------------------


def sjx(x):
	the_last_line = 2 * x
	y = range(x)
	for i in y:
		the_space_before_star = the_last_line / 2 - i
		the_star = i-1
		print " "*the_space_before_star + "* "*the_star 

sjx(10)

# ---------------------------------------------------------------------

try:
	print " ------------ "
	r = 10/0						#【 除数不能为 0，会被报错 】
	#r = 10/ int('a')
	#r = 2
	print 'llllllllllll: ',r

# StandardError 是 ZeroDivisionError和 ValueError的 父类，所以涵盖他们的报错内容 
except StandardError,e:							
	print 'xxxxxxxx StandardError: ',e

except ZeroDivisionError,e:
	print 'except: ',e
except ValueError, e:
	print 'ValueError: ',e

else:
	print " No Error!!!!!!!!!!!!"
finally:
	print 'finally.....'

# ---------------------------------------------------------------------

包含所有错误的 父类 BaseException

try:
	print " ---------- "
	r = 10/0
	print "r = ",r
except BaseException,e:
	print 'The Error is : ',e
else:
	print "No error!!!!"
finally:
	print " ----  End  ----"

# ---------------------------------------------------------------------


多层调用  lxf3() --调用--> lxf2() --> lxf3()是出错位置

def lxf1(x):
	return 10 / int(x)
def lxf2(x):
	return lxf1(x) * 2
def lxf3():
	return lxf2('0')
lxf3()



def lxf1(x):
	print "lxf1: = " + 100/int(x)

def lxf2(x):
	print "lxf2: = " + lxf1(x)+10

def lxf3():
	try:
		lxf2(10)
		print "lxf3"
	except BaseException,e:
		print 'Error! : ',e
	finally:
		print " End !!!!"
lxf3()

# ---------------------------------------------------------------------

【两种报错方式对比 ，后者用 logging.exception 做跟踪记录】

方法1 : 只打印出错误 ，没有 跟踪来源
def lxf1(x):
	print "lxf1: = " + 100/int(x)

def lxf2(x):
	print "lxf2: = " + lxf1(x)+10

def lxf3():
	try:
		lxf2(10)
		print "lxf3"
	except BaseException,e:
		print 'Error! : ',e
	finally:
		print " ---------------- End !!!! ----------------"
lxf3()


方法2 ：记录错误，1步，1步跟踪错误来源
import logging

def lxf1(x):
	return 10/int(x)
def lxf2(x):
	return lxf1(x) * 2
def lxf3():
	try:
		lxf2('0')
	except StandardError,e:
		logging.exception(e)	# 记录错误，1步，1步跟踪错误来源
lxf3()
print "-------------  END!!  ---------------------"

# ---------------------------------------------------------------------

抛出错误 方法一：
class FooError(StandardError):		# 自定义错误专用的class
	pass

def foo(x):
	n = int(x)
	if n == 0:
		raise FooError(u'Value::::::: : ',x)
	else:
		return 10/n

print foo(0)


抛出错误 方法二：
def lxf1(x):
	n = int(x)
	return 10/n
def lxf2(x):
	try:
		return lxf1(x) * 2
	except StandardError,e:
		print 'Error!!!!!!!!!!!!'
		raise ValueError('Input Error')
def main():
	lxf2('0')

main()

#----------------------------------------------



try:
	10/0
except ZeroDivisionError:
	raise ValueError('input error!!')



#----------------------------------------------

try:
	r = 10/''a2222'
	print 'xxxxxxxxxxx',r
except ValueError,aaaaa:
	print 'fffffff:',aaaaa
finally:
	print 'nnnnnnnnnnnnnn'

try:
	foo()
except StandarError,e:
	print 'llllllllllllll :',e
except ValueError,e:
	print 'xxxxxxxxxxxxxx: ',e




def foo(s):
	return 10 / int(s)
def bar(s):
	return foo(s) * 2
def main():
	try:
		bar("0")
	except StandardError,e:
		logging.exception('xxxxxxxxxxxxxx: ',e)

main()
print 'End'

import logging


class lxf(StandardError):
	pass

def foo(x):
	n = int(x)
	if n == 0:
		raise FooError('invalid vale: %s' %x)
	return 10/n

-------------------------------------------
print "1"
raise StopIteration
print "2"
-------------------------------------------

lxf = iter(range(3))

try:
	for i in range(9):
		print lxf.next()
except StopIteration,e:
	print "xxxxxxx:",e

print "===========   End......    =========="


re = iter(range(3))

for i in range(9):
	print re.next()

print "===========   End......    =========="

---------------------------------------------

try:
	#a = 123/0
	#b='abc'
	idx = b[5]
	print '---------- start ------------'
except IndexError:
	print '11111111111111'
except NameError:
	print '222222222222222'
except:
	print '33333333333333'
else:
	print 'else'
finally:
	print ' -- end --'




print "     *     "					#5
print "   * * *   "					#3 	3
print " * * * * * "					#1 	7
print "* * * * * *"					# 	9
print "======================"
----------------------------------------------


def lxf(x):
	y = range(x)
	n = x*2+1           # How many space character before the first *?
	for i in y:
		tmp = n/2-i
		tmp2 = i
		print ' ' * tmp,'*',' ' * tmp2,'*',' '* tmp

lxf(6)


import socket

# 创建一个socket
# AF_INET = IPv4	AF_INET6 = IPv6
# SOCK_STREAM = TCP协议
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 建立连接，把目标地址及目标端口
# 常用端口： SMTP - 25端口，FTP - 21端口
# (参数是个tunple，元组)
s.connect(('www.sina.com.cn',80))
s.send('GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收新浪服务器返回的数据
buffer = []
while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = ''.join(buffer)
s.close


#把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件
header,html = data.split('\r\n\r\n',1)
print header
with open('sina.html','wb') as f:
	f.write(html)

# 最后，直接在浏览器中打开


----------------------------------------------

【服务端】
import socket
import threading
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定端口， 用本机的 9999 作为服务端口
s.bind(('127.0.0.1',9999))

# 监听端口
s.listen(5)
print u'正在接收数据：...'

# 必须多线程处理，否则只能处理1个客户端请求
def tcplink(sock,addr):
	print(u'允许来自 %s:%s...'%addr)
	sock.send(b'welcome')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello,%s!' %data).encode('utf-8'))
	sock.close()
	print(u'来自%s:%s的连接被中断' %addr)


#用循环接收 来自客户端的数据
while True:
	#接受一个新连接
	sock,addr = s.accept()
	# 创建新县城来处理 TCP 连接
	t = threading.Thread(target=tcplink,args=(sock,addr))
	t.start()



【客户端】
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))

print(s.recv(1024).decode('utf-8'))

for data in ['lxf','lixuefei','lee']:
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()

----------------------------------------------


def sjx(x):
	the_last_line = 2 * x
	y = range(x)
	for i in y:
		the_space_before_star = the_last_line / 2 - i
		the_star = i-1
		print " "*the_space_before_star + "* "*the_star 

sjx(10)

----------------------------------------------


try:
	print " ------------ "
	#r = 10/0						#【 除数不能为 0，会被报错 】
	r = 10/ int('a')
	#r = 2
	print 'llllllllllll: ',r

# StandardError 是 ZeroDivisionError和 ValueError的 父类，所以涵盖他们的报错内容 
except BaseException,e:							
	print 'xxxxxxxx StandardError: ',e

except ZeroDivisionError,e:
	print 'except: ',e
except ValueError, e:
	print 'ValueError: ',e

else:
	print " No Error!!!!!!!!!!!!"
finally:
	print 'finally.....'


----------------------------------------------

# 包含所有错误的 父类 BaseException
try:
	print " ---------- "
	r = 10/0
	print "r = ",r
except BaseException,e:
	print 'The Error is : ',e
else:
	print "No error!!!!"
finally:
	print " ----  End  ----"

----------------------------------------------


# 多层调用  lxf3() --调用--> lxf2() --> lxf3()是出错位置

def lxf1(x):
	print "lxf1: = " + 100/int(x)

def lxf2(x):
	print "lxf2: = " + lxf1(x)+10

def lxf3():
	try:
		lxf2(10)
		print "lxf3"
	except BaseException,e:
		print 'Error! : ',e
	finally:
		print " End !!!!"

lxf3()

----------------------------------------------
# 只打印出错误 ，没有 跟踪来源
def lxf1(x):
	print "lxf1: = " + 100/int(x)

def lxf2(x):
	print "lxf2: = " + lxf1(x)+10

def lxf3():
	try:
		lxf2(10)
		print "lxf3"
	except BaseException,e:
		print 'Error! : ',e
	finally:
		print " ---------------- End !!!! ----------------"
lxf3()


#----------------------------------------------


# 记录错误，1步，1步跟踪错误来源
import logging
import lxfstudy

logger = logging.getLogger('lxfstudy')
log_file = logging.FileHandler(r'D:\app.log')
formatter = logging.Formatter('%(asctime)s%(levelname)s%(message)s')
log_file.setFormatter(formatter)
logger.addHandler(log_file)
logger.setLevel(logging.WARNING)
logger.error(u'错误 ：')
logger.info(u'xxxxxxxxxxxxxx: ')

#----------------------------------------------

抛出错误 方法一：
class LxfError(StandardError):		# 自定义错误专用的class
	pass

def foo(x):
	n = int(x)
	if n == 0:
		raise LxfError(u'Value::::::: : %s' %s)
	else:
		return 10/n

print foo(0)


抛出错误 方法二：
def lxf1(x):
	n = int(x)
	return 10/n
def lxf2(x):
	try:
		return lxf1(x) * 2
	except StandardError,e:
		print 'Error!!!!!!!!!!!!'
		raise ValueError('Input Error')
def main():
	lxf2('0')

main()

#----------------------------------------------

try:
	10/0
except ZeroDivisionError,e:
	print "ZeroDivisionError: " ,e
	raise ValueError('input error!')


#----------------------------------------------


import logging
logging.basicConfig(level=logging.INFO)


x = '0'
n = int(x)
logging.info('n = %d' %n)
print 10/n


#----------------------------------------------

class List_analysis(object):
	def __init__(self,x=10):
		self.rangeX = x

	def setrangeX(self,x):
		self.rangeX = x

	def answer(self):
		return [x*x for x in range(self.rangeX)]
		


lxf = List_analysis()
lxf.setrangeX(10)
print lxf.answer()
#----------------------------------------------

#注册邮箱用户名  lixuefei@lxf.com

 m=re.match(r"^([a-zA-Z0-9]+[-\\|.]?)+[a-zA-Z0-9]@([0-9A-Za-z]+(-[a-z0-9A-Z]+)?\.)+[a-zA-Z]{2,}$",username); 


 pwd=re.match(r"^([a-zA-Z0-9])",password)  
            if (pwd and (len(password)<9)):  
                print "密码过短,或者不符合格式" 

  password1=raw_input("请再次输入您的密码:")  
            if (password!=password1):  
                print "两次输入不一致,请重新输入"  


# 用户名： 1.前后及中间不得有空格  2.不能含有非法言论
def username():
	try:
		user = raw_input('Please enter your username: ')
		#print user
	except BaseException,e:
		print u'输入有误:',e
	except ' '.join([x for x in user if x==' ']):
		print u'不能有空格'
	else:
		print u"%s 用户名可用  √"%user
	finally:
		pass

username()

#----------------------------------------------

class Abs(object):
	def __init__(self,x):
		self.x = x

	def lxfabs(self):
		if str.isdigit(self.x) == True:
			if self.x >= 0:
				return self.x
			else:
				return -self.x
		else:
			raise TypeError('Please enter a number!')

#lxf=Abs('sss')
#print lxf.abs()

#----------------------------------------------
class Goods(object):
	def __init__(self):
		pass

	def set_price(self,price):
		self.price = price

	def get_price(self):
		print 'xxxxxxx',self.price

class Books(Goods):
	pass

class Python(Books):
	def get_price(self):
		print 'The Python book is %s' %self.price

lxf = Python()
lxf.set_price(100)
lxf.get_price()


#----------------------------------------------

class Student(object):
	pass

lxf = Student()
lxf.name = 'lixuefei'
print lxf.name

#绑定方法
def set_age(self,age):
	self.age = age
from types import MethodType
lxf.set_age = MethodType(set_age,lxf,Student)
lxf.set_age(25)
print lxf.age

# -----------------------------------------------
class Books(object):
	def __init__(self,price=200):
		self.price = price

	__slots__ = ('price','get_price')

lxf = Books()

#给实例lxf，绑定方法
def get_price(self):
	print slef.price

from types import MethodType
lxf.get_price = MethodType(get_price,lxf,Books)
temp_price = lxf.price
print temp_price
# 给实例lxf 绑定属性；
# 但是class里__slots__限定允许绑定price，所以绑定name失败
#lxf.name = 'python'
#print lxf.name

# -----------------------------------------------

# 【1 - 1】函数的装饰器 
def log(func):
	def wrapper(*args,**kw):
		print 'Log %s():' %func.__name__
		return func(*args,**kw)
	return wrapper

@log
def now():
	print 'test'


# -----------------------------------------------

#【1】 装饰器
def deco(func):
	print "--------- 1 --------"
	func()
	print " ----------- 2 ---------"
	return func

# 如果不用装饰器，
# 用函数，则等于这样实现的， 把lxffunc当做参数带进 deco函数
#def lxffunc():
#	print "myfunc() called."
#lxffunc=deco(lxffunc)

@deco
def lxffunc():
	print 'lixuefei'




#【2】 装饰器
#一件商品100元， 今日打8折，用装饰器实现
def sale(func):
	print func()
	y = func() * 0.8
	print y

@sale
def book_price():
	x = 100
	return x

#【3】 装饰器
# 该方法是 确保每次新函数都被调用，
# 即：有几次 lxf()就调用几次装饰器
def deco(func):
	def _deco():
		print "---------- 1 -----------"
		func()
		print "---------- 2 -----------"
	return _deco

@deco
def lxf():
	print "lixuefei"
	return "ok"

lxf()
lxf()
lxf()


# 该方法，只修饰了第一个lxf()，后面的无装饰器功能 
def _deco(func):
	print "-------- 1 ---------- "
	func()
	print "-------- 2 -----------"
	return func

@_deco
def lxf():
	print "lixuefei"
	return "ok"

lxf()
lxf()
lxf()


#【4】 装饰器
#一件商品100元， 现打8折，实现第1次函数被调用
def sale(func):
	y = func() * 0.8
	print y
	return sale

@sale
def book_price():
	x = float(100)
	return x

# --------------------------------------------------
#一件商品100元， 今日打8折，实现每次函数都被调用
def sale(func):
	def _sale():
		y = func() * 0.8
		print y
	return _sale

@sale
def book_price():
	x = float(100)
	return x

book_price()
book_price()
book_price()

#【5】 装饰器 - 带参数
def deco(func):
	def _deco(a,b):
		print "----------- 1 ----------"
		ret = func(a,b)
		print "----------- 2 ----------"
		return ret
	return _deco

@deco
def lxf(a,b):
	print "lixuefei a=%s , b=%s" %(a,b,)
	return a+b

print lxf(1,2)
print lxf(3,4)
# ------------------------------------------------

#【6】 装饰器 - 带参数,但事，参数不确定 

def deco(func):
	def _deco(*arg,**kw):
		print "------- 1 ---------"
		tmp = func(*arg,**kw)
		print ' %s ,,, %s ' %(func.__name__,tmp)
		return tmp
	return _deco

@deco
def lxf(a,b):
	return a+b

lxf('a','d')
lxf(1,2)


# ------------------------------------------------

#【7】 装饰器参数
一件商品100元， 今日打8折，函数是商品原价， 装饰器的参数=8折

def sale(x):
	def _sale(func):
		def __sale():
			new_price = func() * x
			return new_price
		return __sale
	return _sale

@sale(0.8)
def price():
	x = 100
	return x

print price()

# ------------------------------------------------
#周六8折
my_shopping = 0

def sale(func):
	def _sale():
		y = func() * 0.8
		return y
	return _sale


def book_price():
	x = 100
	return x	

@sale
def book_sale_price():
	x = 100
	return x	

import time
#print time.strftime("%Y-%m-%d",time.localtime())
a = time.localtime()
today = time.strftime("%A",a)

if today == 'Thursday':
	print "Today is Saturday ,so sale 80% = " ,book_sale_price()
else:
	print "Today is not Saturday,so no Sale = ",book_price()

# 满100减去20
def reduce_the_price(func):
	def _reduce_the_price():
		y = func() - 20
		return y
	return _reduce_the_price

def book_price():
	x = 106
	return x

@reduce_the_price
def book_sale_price():
	x = 106
	return x

if book_price() >= 100:
	print u"满100-20活动 ， 价格改为",book_sale_price()
else:
	print u"未满100，原价",book_sale_price()

# ------------------------------------------------


import requests
r = requests.get('http://www.jiangmin.com/d/file/p/2012-05-23/cuangai.jpg').content
with open(r'/home/lxf/1',wb) as jpg:
	jpg.write(data)

requests用法

import requests
s = requests.session()
res = s.post('http://news.baidu.com/')
s.get('http://news.baidu.com/')
r = requests.get('http://news.baidu.com/')
#print r 			#返回  Response [200] | 链接成功
r.headers
r.status_code		#返回 200
r.text				# html源文件 
r.content


# ------------------------------------------------

访问网页，并且把改网页下载为 html文件

import os
import sys
import requests

reload(sys)
sys.setdefaultencoding( "utf-8" )

r = requests.get('http://www.nationalgeographic.com.cn/')
r.url                           	# url地址

tmp = r.text            			# html源码
tmp_file = r'/home/lxf/NG.html'     # html保存的目录
f = file(tmp_file,'w') 				# 要写的文件 和 赋予写权限
f.write(tmp)						# 写什么内容
f.close								# 正常关闭文件

# ------------------------------------------------


下载图片

import os
import sys
import requests

# 图片地址
url = r'http://image.nationalgeographic.com.cn/2015/1110/thumb_340_244_20151110054246877.jpg'

# requests访问网址；
conn = requests.get(url)

# 下面的模式将文本流保存到文件:
with open(r'/home/lxf/1.jpg','wb') as x:
	x.write(conn.content)

# ------------------------------------------------

访问网页，并且把改网页下载为 html文件

import os
import sys
import requests

# 图片地址
url = r'http://www.nationalgeographic.com.cn/'

# requests访问网址；
conn = requests.get(url)

# 下面的模式将文本流保存到文件:
with open(r'/home/lxf/1.html','wb') as x:
	x.write(conn.content)

# ------------------------------------------------

#【0】 match 是否匹配,  格式: 3个数字 - 8个数字
import re
pattern = re.compile(r'\d{3}\-\d{8,8}$')
x = pattern.match('010-12345678')
if x:
	print x.group()

# ------------------------------------------------

# 【1】 split分割 为列表
import re
pattern1 = re.compile(r'\d')
print pattern1.split('one1111two2three3four4')
结果 ['one', '', '', '', 'two', 'three', 'four', '']

pattern2 = re.compile(r'\d+')
print pattern2.split('one1111two2three3four4')
结果 ['one', 'two', 'three', 'four', '']


'2015-11-11'.split('-')				# 普通用法
['2015', '11', '11']

>>> '2015-11----11'.split('-')		# 普通用法 
['2015', '11', '', '', '', '11']

re.split(r'-+','2015-11---11')		#re正则用法，+号是忽略连续个
['2015', '11', '11']

re.split(r'[-\,\;]+','2015---11,11;;;;;;12:30:17')

# ------------------------------------------------

#【2】 findall 搜索关键字，返回全部匹配项
import re
pattern = re.compile(r'\d+')
print pattern.findall('one1111two2three3four4')
结果 ['1111', '2', '3', '4']

# ------------------------------------------------

#【3】 search 查找
import re
pattern = re.compile(r'world')
x = pattern.search('hello world')
if x:
	print x.group()
结果 world

# ------------------------------------------------

import re


分隔符

pattern2 = re.compile(r'[=\com]')
x = pattern2.split('src=http://www.1905.com/index.html')
print x     
结果['sr', '', 'http://www.1905.', '', '', '/index.ht', 'l']



搜索

解释： (1)http://开始，+ . + (2)S是匹配“非空”字符,+是任意数量 + . + com
pattern1 = re.compile(r'\http://\w+\.\S+\.\com')		
x = pattern1.search('src=http://www.m1905.com/index.html')
if x:
	print x.group()		
结果：http://www.1905.com



VPN用户 ， 每登录一次，  snat出口都会改变
出口IP   192.168.10.69
		 192.168.199.112
		 192.168.97.171


1. 添加用户		system-user		lixuefei  123456

2. 远程管理		IP-Service		winbox:8291

3. 外网接口		ip-address		192.168.199.112
								192.168.97.171
								192.168.10.69

   内网接口		ip-address		10.0.0.1 
   								10.10.10.1

4. 防火墙		ip-firewall		input-any-allow
								output-any-allow
								forward-any-allow

5. snat上网		ip-nat			masquerade|snat

6. 自定义列表	ip-Pools --  vpn池子10.0.0.10
							 出口池子

7. vpn  		[秘钥： 19051905 ]
				账号：lixuefei  123456
				      test1		123456
				      test2		123456
				      test3		123456

# ------------------------------------------------

【1】
import re
import os
import sys


html_file = r'/home/lxf/1.html'
f = file(html_file,'r')
tmp = f.read()

#
pattern = re.compile(r'http://\S+\.\jpg')
x = pattern.search(tmp)
if x:
	print x.group()

f.close()

# ------------------------------------------------

#【2】 全文检索用findall， 结果自动存入列表 
import os
import sys
import re
import requests

html_file = r'/home/lxf/1.html'		# 被检索文件
f = file(html_file,'r')				# 只读权限 读文件
tmp = f.read()						# 执行（真正的去读文件）

pattern = re.compile(r'http://\S+\.\png|http://\S+\.\jpg')
#解释： (1) \ 是 and 的意思
#		(2) http://开始，
#		(3) . 
#		(4)S是匹配“非空”字符,+是任意数量 
#		(5). 
#		(6)com
#		(7) A|B  意思是 A和B都被检索出来 

# ------------------------------------------------


【3】 web爬虫 - 图片下载【面条版】
import os
import sys
import re
import requests

html_file = r'/home/lxf/1.html'		# 被检索文件
f = file(html_file,'r')				# 只读权限 读文件
tmp = f.read()						# 执行（真正的去读文件）

pattern = re.compile(r'http://\S+\.\png|http://\S+\.\jpg')
#解释： (1) \ 是 and 的意思
#		(2) http://开始，
#		(3) . 
#		(4)S是匹配“非空”字符,+是任意数量 
#		(5). 
#		(6)com
#		(7) A|B  意思是 A和B都被检索出来 
url_list = pattern.findall(tmp)

创建个目录，准备下载图片
picture_name = 0    		# 图片的名字用数字递增表示
for url in url_list:		# 把单个url从list中分离
	conn = requests.get(url)	# requests 访问rul

	picture_name = picture_name + 1  #修改图片名字，每次循环+1
	pic_pwd = r'/home/lxf/pic/%s.jpg',%picture_name #定义保存目录和文件名

	with open(pic_pwd,'wb') as lxf:   #下载图片，wb是写权限
		lxf.write(conn.content)

# ------------------------------------------------

【4】 
web爬虫 - 抓图 【纯面条式 命令教学版】
【BUG ： 图片名字不规范，很容易文件名冲突】
# -*- coding: utf-8 -*-
import os
import re
import sys
import requests
# ----------------------------------------------------
web_url = r'http://www.nationalgeographic.com.cn/'	# web_url=网页地址
web_pwd = r'/home/lxf/'								# web_pwd=网页存放目录
web_name = '1.html'									# web_name=网页文件名
web_file = web_pwd+web_name							#web_file=网页的图片+文件名
pic_pwd = r'/home/lxf/'								# pic_pwd = 图片存放路径
# pic_url=图片地址 [变量，待re正则出结果]
# pic_name = 图片文件名	 [变量，待re正则出结果]
# ----------------------------------------------------
#1  requests读取网页
connect = requests.get(web_url)
connect.url
html_code = connect.text            # html源码
# ----------------------------------------------------
#2 	将源码下载到本地
reload(sys)							# 规定编码，无此行会报告
sys.setdefaultencoding( "utf-8" )	# UnicodeEncodeError: 'ascii' codec can't encode characters
f = file(web_file,'w') 				# 要写的文件 和 赋予写权限
f.write(html_code)						# 写什么内容
f.close								# 正常关闭文件
# ----------------------------------------------------
#3 	打开文件
f = file(web_file,'r')
html_code = f.read()
# ----------------------------------------------------
#4 	检索图片url
pattern = re.compile(r'http://\S+\.\jpg|http://\S+\.\png')
url_list = pattern.findall(html_code)
# ----------------------------------------------------
#5	下载图片到本地
pic_name = 0    		# 图片的名字用数字递增表示
for pic_url in url_list:		# 把单个url从list中分离
	conn = requests.get(pic_url)	# requests 访问rul

	pic_name = pic_name + 1  #修改图片名字，每次循环+1
	pic_file = pic_pwd+str(pic_name)+'.jpg'
	with open(pic_file,'wb') as lxf:   #下载图片，wb是写权限
		lxf.write(conn.content)
	
# ------------------------------------------------
【5】 
#web爬虫 - 抓图 【纯面条式 命令教学版】
#【解决： 图片名称 = 源码图片中的文件名】
# -*- coding: utf-8 -*-
import os
import re
import sys
import requests
# ----------------------------------------------------
web_url = r'http://www.nationalgeographic.com.cn/'	# web_url=网页地址
web_pwd = r'/home/lxf/'								# web_pwd=网页存放目录
web_name = '1.html'									# web_name=网页文件名
web_file = web_pwd+web_name							#web_file=网页的图片+文件名
pic_pwd = r'/home/lxf/'								# pic_pwd = 图片存放路径
# pic_url=图片地址 [变量，待re正则出结果]
# pic_name = 图片文件名	 [变量，待re正则出结果]
# ----------------------------------------------------
#1  requests读取网页
connect = requests.get(web_url)
connect.url
html_code = connect.text            # html源码
# ----------------------------------------------------
#2 	将源码下载到本地
reload(sys)							# 规定编码，无此行会报告
sys.setdefaultencoding( "utf-8" )	# UnicodeEncodeError: 'ascii' codec can't encode characters
f = file(web_file,'w') 				# 要写的文件 和 赋予写权限
f.write(html_code)						# 写什么内容
f.close								# 正常关闭文件
# ----------------------------------------------------
#3 	打开文件
f = file(web_file,'r')
html_code = f.read()
# ----------------------------------------------------
#4 	检索图片url
pattern = re.compile(r'http://\S+\.\jpg|http://\S+\.\png')
#解释： (1) \ 是 and 的意思
#		(2) http://开始，
#		(3) . 
#		(4)S是匹配“非空”字符,+是任意数量 
#		(5). 
#		(6)com
#		(7) A|B  意思是 A和B都被检索出来 
url_list = pattern.findall(html_code)
# ----------------------------------------------------
#5	下载图片到本地

for pic_url in url_list:		# 把单个url从list中分离
	conn = requests.get(pic_url)	# requests 访问rul

	# 【提取源码中图片的文件名】
    # 预期提取图片文件名例：20151116031138474.jpg
    # w+ 代表非字符单属于单词和数字的
    # $ 代表从尾部匹配
	pattern = re.compile(r'\w+\.jpg$|\w+\.png$')
	pic_name = pattern.search(pic_url) 	# 正则url，不用正则全文
	
	if pic_name:
		name = pic_name.group()
		pic_file = pic_pwd+name 		# 图片保存目录 + 文件名
		with open(str(pic_file),'wb') as lxf:   #下载图片，wb是写权限
			lxf.write(conn.content)		#执行下载图片（写图片文件）
		
# ------------------------------------------------
# -*- coding: utf-8 -*-
#【6】# web爬虫 - 抓图【class版】
# 访问 国家地理网站抓取上面的图片，并且图片文件名与html源码中的名一致
import os
import re
import sys
import requests
# ----------------------------------------------------
web_url = r'http://www.nationalgeographic.com.cn/'	# web_url=网页地址
html_pwd = r'/home/lxf/'							# web_pwd=网页存放目录
html_name = '1.html'								# web_name=网页文件名
pic_pwd = r'/home/lxf/'								# pic_pwd = 图片存放路径
# pic_url=图片地址 [变量，待re正则出结果]
# pic_name = 图片文件名	 [变量，待re正则出结果]
# ----------------------------------------------------
class Lxf_spider_imagebot(object):
	def __init__(self):
		self.__weburl = 'blank'
		self.__html_code = 'blank'
		self.__pic_url_list = 'blank'

		self.__html_pwd = 'blank'
		self.__html_name = 'blank' 
		self.__html_file = self.__html_pwd + self.__html_name

		self.__pic_pwd = 'blank'


	# 设置网页url地址
	def set_weburl(self,x):					# 设置 url地址， 这是私有的
		self.__weburl = x

	def set_html_file(self,x,y):
		self.__html_pwd = x
		self.__html_name = y

	def set_pic_file(self,x):
		self.__pic_pwd = x

	# 打印url地址
	#def print_weburl(self):
		#print self.__weburl

	def requests_weburl(self):				# requests 网页地址
		conn = requests.get(self.__weburl)
		conn.url
		html_code = conn.text
		self.__html_code = html_code 		# 将结果传入 self.__html_code

	def download_htmlcode(self):			# 下载html源码到本地
		reload(sys)							# 规定编码，无此行会报告
		sys.setdefaultencoding( "utf-8" )	# UnicodeEncodeError: 'ascii' codec can't encode characters
		f = file(self.__html_file,'w') 		# 要写的文件 和 赋予写权限
		f.write(self.__html_code)			# 写什么内容
		f.close								# 正常关闭文件

	def search_pic_url(self):
		pattern = re.compile(r'http://\S+\.\jpg|http://\S+\.\png')
		x = pattern.findall(self.__html_code)
		self.__pic_url_list = x

			#解释： (1) \ 是 and 的意思
			#		(2) http://开始，
			#		(3) . 
			#		(4)S是匹配“非空”字符,+是任意数量 
			#		(5). 
			#		(6)com
			#		(7) A|B  意思是 A和B都被检索出来 

	def download_pic(self):
		for pic_url in self.__pic_url_list:
			conn = requests.get(pic_url)
			pattern = re.compile(r'\w+.\jpg$|\w+.\jpg$')
				# 【提取源码中图片的文件名】
    			# 预期提取图片文件名例：20151116031138474.jpg
    			# w+ 代表非字符单属于单词和数字的
    			# $ 代表从尾部匹配
			pic_name = pattern.search(pic_url)
			if pic_name:
				name = pic_name.group()
				pic_file = self.__pic_pwd + name 		# 图片保存目录 + 文件名
				with open(str(pic_file),'wb') as lxf:   #下载图片，wb是写权限
					lxf.write(conn.content)				#执行下载图片（写图片文件）

if __name__ == '__main__': 
	lxf = Lxf_spider_imagebot() 

	lxf.set_weburl(web_url) 							# 设置:访问 url
	lxf.set_html_file(html_pwd,html_name)				# 设置：html源码存放的本地目录
	lxf.set_pic_file(pic_pwd)
	#lxf.print_weburl()
	lxf.requests_weburl() 								# requests 网页地址
	#lxf.download_htmlcode()							# 下载 html到本地
	lxf.search_pic_url()
	lxf.download_pic()
	

# ------------------------------------------------
【sqlalchemy】
安装	pip install sqlalchemy    [centos 6.6 + python 2.6.6]

测试	import sqlalchemy
		sqlalchemy.__version__

# -*- coding:utf-8 -*-
【1】 连接mysql -- 创建lxfpy库 -- show databases；
from sqlalchemy import *
db = create_engine("mysql://root:123456@127.0.0.1")		# 登录mysql
db.execute("show databases")							# 错误！！ 无法回显
db.execute("create databases lxfpy")					# 创建 database lxfpy
db.execute("drop databases lxfpy")						# 删除 database lxfpy
db.echo = True

#---------------------------------------------------------------------------
【2】 连接mysql -- 创建lxfpy库 -- show databases；
# -*- coding:utf-8 -*-
from sqlalchemy import *
db = create_engine("mysql://root:123456@127.0.0.1")
db.execute("use lxfpy")
db.echo = True

 实现mysql语句： create table example0(id INT,name VARCHAR(20),sex BOOLEAN)；
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | YES  |     | NULL    |       |
| name  | varchar(20) | YES  |     | NULL    |       |
| sex   | tinyint(1)  | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+

metadata = MetaData(db)
users = Table('example0',metadata,						# example0是表名；
		Column('id',Integer),							# 创建字段 id，整形
		Column('name',VARCHAR(40)),						# 创建字段 name，字符串
		Column('sex',BOOLEAN),	# tinyint				# 创建字段 sex，布尔型
	)
users.create()											# 执行创建

#---------------------------------------------------------------------------
【4】 连接mysql -- use database lxfpy -- use table example0 -- insert N多条数据；
#-*- coding: utf-8 -*-
from sqlalchemy import *
db = create_engine("mysql://root:123456@127.0.0.1")
db.execute("use lxfpy")
db.echo = True

metadata = MetaData(db)
example0 = Table('example0',metadata,					# example0是表名；
		Column('id',Integer),							# 创建字段 id，整形
		Column('name',VARCHAR(40)),						# 创建字段 name，字符串
		Column('sex',BOOLEAN),	# tinyint				# 创建字段 sex，布尔型
	)
#example0.create()										# 创建表结构，之前已建	
i = example0.insert()
i.execute(id=1,name='lxf1',sex=True)					# 插入1条
i.execute({'id':2,'name':'John', 'sex': False},			# 插入N多条
         {'id':3, 'name':'Susan', 'sex': False},
        {'id':4, 'name':'Carl', 'sex': True})


#---------------------------------------------------------------------------

【5】 连接mysql -- 查表example0
#-*- conding: utf-8 -*-
from sqlalchemy import *

db = 

#---------------------------------------------------------------------------
# -*- coding: utf-8 -*-
【10】 创建库lxfpy -- 创建表结构 -- 插入3条数据
from sqlalchemy import *
db = create_engine("mysql://root:123456@localhost")		# 链接数据库
db.execute("create database lxfpy")
db.execute("use lxfpy")
db.echo = False  										# True回显mysql结果 
metadata = MetaData(db)
users = Table('users', metadata,						# 描述表结					
        Column('user_id', Integer, primary_key=True),
        Column('name', String(40)),
        Column('age', Integer),
        Column('password', String(40)),
        )
users.create()
i = users.insert()
i.execute(name='Mary', age=30, password='secret')
i.execute({'name': 'John', 'age': 42},
         {'name': 'Susan', 'age': 57},
        {'name': 'Carl', 'age': 33})

s = users.select()
rs = s.execute()
row = rs.fetchone()
print 'Id:', row[0]

print 'Name:', row['name']
print 'Age:', row.age
print 'Password:', row[users.c.password]

for row in rs:
        print row.name, 'is', row.age, 'years old'

db.execute("drop database lxfpy")
# 上一行是删除掉库，否则再运行改test程序时，提示已经有该数据



# -*- coding: utf-8 -*-
#【2】 在原有lxfpy插入3条数据
from sqlalchemy import *
db = create_engine("mysql://root:123456@localhost")
#db.execute("create database lxfpy")
db.execute("use lxfpy")
db.echo = True  # Try changing this to True and see what happens
metadata = MetaData(db)
users = Table('users', metadata,						
        Column('user_id', Integer, primary_key=True),
        Column('name', String(40)),
        Column('age', Integer),
        Column('password', String(40)),
        )
#users.create()		这行不要，新创建表时用！！
#插入
i = users.insert()
i.execute(name='Mary', age=30, password='secret')
i.execute({'name': 'lxf2', 'age': 42},
         {'name': 'lxf3', 'age': 57},
        {'name': 'lxf4', 'age': 33})
'''
s = users.select()
rs = s.execute()
row = rs.fetchone()
print 'Id:', row[0]

print 'Name:', row['name']
print 'Age:', row.age
print 'Password:', row[users.c.password]

for row in rs:
        print row.name, 'is', row.age, 'years old'

def getfactors(number): 					#假设 number=10
    factorList = [] 
    for i in range(1, number + 1): 			# for i in range(1,11) 即,i = 1,2,3,4,5,6,7,8,9,10
        if number % i == 0:  # 10 分别除以 （1-10）找出能够整出的数（1，2，5） and 去掉非素数1
            factorList.append(i) 			# factorList = [2，5]
    return factorList 



def getfactors(number): 
    fList = [1,number] 						#假设 number=10
    for i in range(1,number + 1): 			# for i in range(1,11) 即,i = 1,2,3,4,5,6,7,8,9,10
        if number % 2 == 0: 				# 第1次循环中 number =10   10除以2==0，那么 fList=[1,10,] , 然后 10/2 = 5
            fList.append(2) 				# 第2次循环中 number =5   5除以2不=0，那么 fList列表中加5
            number = number / 2 			# 一共循环  number=10 次循环
        else: 
            fList.append(number) 
            break 
    return fList 


print getfactors(10)


# 排列组合  -- 多个list
import itertools
list1 = ['a','b','c','d','e','f','e','g','h','i','j','k']
list2 = ['apple','pear']
list3 = ['cat','moto']
list_final = (list(itertools.product(list1,list2,list3)))
#结果不好： a1,a2,a3,......,c2,c3 ; 不能 a123, abc123;
#而且，当原始list>3时，就变为  (a,apple,cat),不能(a,apple)


# 排列组合  -- N个list 加进1个list，每次组合3个元素 【会内存不足】
import time  #由于排列组合太多，所以需要暂停几秒，释放内存
import itertools
list1 = ['a','b','c','d','e','f','e']
list2 = ['apple','pear']
list3 = ['cat','moto']
list4 = ['g','h','i','j','k']
list5 = ['1','2','3','4','5']
list6 = ['aa','bb','cc','dd','ee','ff','ee']
list7 = ['qq','xx']
list8 = ['ww','ee']
list9 = ['zz','xx','cc','vv','bb']
list10 = ['**','((','))','mm','nn']
list11 = ['gg','hh','ii','jj','kk','ll','mm']
list12 = ['nn','oo']
list13 = ['pp','qq']
list14 = ['rr','ss','tt','uu','vv']
list15 = ['zz','aaa','bbb','ccc','ddd']
list16 = ['eee','fff','ggg','hhh','iii','jjj','kkk']
list17 = ['lll','mmm']
list18 = ['nnn','ooo']
list19 = ['ppp','qqq','rrr','sss','ttt']
list20 = ['uuu','vvv','www','xxx','yyy']
list21 = ['zzz','aaaa','…']

 # 原始数据 将所有 list 加入list_all1中  
list_all1 = list2+list3
list_all2 = []                  # itertools函数，变成len(list1)个数量个list
list_final = []                  # 把所有list拆开，统一放进一个list中

for i in range(1,len(list_all1)+1):
    iter = itertools.permutations(list_all1,2)  #最后的3， 代表每次从'abcd'中挑选两个元素，比如ab, bc, ...
    list_all2.append(list(iter))

for x in list_all2:
    for y in x:
        list_final.append(y)
# 结果很理想 :  a, b,c,ab,ac,abc,ba,...,cba
# 缺点：abc, 和 cba；也许这是好事儿，因为筛选规则中，先滤掉a和先滤掉c的结果可能不一样的；
for mm in list_final:
    print " --- %s  %s "%(mm[0],mm[1])
# 5秒出len(list_final)  ， 但如果print全部数据的话很慢-N分钟
s



