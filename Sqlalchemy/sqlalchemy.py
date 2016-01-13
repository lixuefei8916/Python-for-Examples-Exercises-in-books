	
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
| age   | tinyint(1)  | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+

metadata = MetaData(db)
users = Table('example0',metadata,						# example0是表名；
		Column('id',Integer),							# 创建字段 id，整形
		Column('name',VARCHAR(40)),						# 创建字段 name，字符串
		Column('age',Integer),	# tinyint				# 创建字段 age，整形
	)
users.create()											# 执行创建

#---------------------------------------------------------------------------
【3】 连接mysql -- use database lxfpy -- use table example0 -- insert N多条数据；
#-*- coding: utf-8 -*-
from sqlalchemy import *
db = create_engine("mysql://root:123456@127.0.0.1")
db.execute("use lxfpy")
db.echo = True

metadata = MetaData(db)
example0 = Table('example0',metadata,					# example0是表名；
		Column('id',Integer),							# 创建字段 id，整形
		Column('name',VARCHAR(40)),						# 创建字段 name，字符串
		Column('age',Integer),	# tinyint				# 创建字段 age，整形
	)
#example0.create()										# 创建表结构，之前已建	
i = example0.insert()
i.execute(id=1,name='lxf1',age=True)					# 插入1条
i.execute({'id':2,'name':'John', 'age': False},			# 插入N多条
         {'id':3, 'name':'Susan', 'age': False},
        {'id':4, 'name':'Carl', 'age': True})


#---------------------------------------------------------------------------

【4】 select 查表example0
#-*- conding: utf-8 -*-
from sqlalchemy import *

db = create_engine("mysql://root:123456@127.0.0.1")
db.execute("use lxfpy")
db.echo = True

metadata = MetaData(db)
example0 = Table('example0',metadata,
	Column('id',Integer),
	Column('name',VARCHAR(40)),
	Column('age',Integer),
	)

s = example0.select()	
#SELECT example0.id, example0.name, example0.age FROM example0

rs = s.execute()		# <0x26db390>
row = rs.fetchone()		

print row				#回显(1L, 'lxf1', 26L)
print 'Id:', row[0]		#回显 1
print 'name:', row[1]	#回显 lxf1
print 'age:', row[2]	#回显 26
print 'Name:', row['name']		#回显 lxf1
print 'Age:', row.age 			#回显 26

for row in rs:			# 等同 select * from example0
        print row


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
#【11】 在原有lxfpy插入3条数据
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

s = users.select()
rs = s.execute()
row = rs.fetchone()
print 'Id:', row[0]

print 'Name:', row['name']
print 'Age:', row.age
print 'Password:', row[users.c.password]

for row in rs:
        print row.name, 'is', row.age, 'years old'


#=====================================================

# -*- coding: utf-8 -*-
import os
import re
import sys
import requests
from sqlalchemy import *
from sqlalchemy.dialects.mysql import *
# ----------------------------------------------------
web_url = r'http://www.nationalgeographic.com.cn/'	
html_pwd = r'/home/lxf/'							
html_name = '1.html'								
pic_pwd = r'/home/lxf/'								

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


	def set_weburl(self,x):					
		self.__weburl = x

	def set_html_file(self,x,y):
		self.__html_pwd = x
		self.__html_name = y

	def set_pic_file(self,x):
		self.__pic_pwd = x

	def requests_weburl(self):				
		conn = requests.get(self.__weburl)
		conn.url
		html_code = conn.text
		self.__html_code = html_code 		

	def download_htmlcode(self):			
		reload(sys)							
		sys.setdefaultencoding( "utf-8" )	
		f = file(self.__html_file,'w') 		
		f.write(self.__html_code)			
		f.close								

	def search_pic_url(self):
		pattern = re.compile(r'http://\S+\.\jpg|http://\S+\.\png')
		x = pattern.findall(self.__html_code)
		self.__pic_url_list = x

	def download_pic_to_mysql(self):
		print 'lxf_sql_mysql start'
		db = create_engine("mysql://root:123456@127.0.0.1")	
		db.execute("use lxfpy")
		db.execute('drop table pic0')
		db.echo = True

		metadata = MetaData(db)
		pic0 = Table('pic0',metadata,				
				Column('url',VARCHAR(250)),	
				Column('img',VARCHAR(2500)),		
				)		
		pic0.create()	
		i = pic0.insert()	

		for pic_url in self.__pic_url_list:
			i.execute(url=pic_url)				# 把图片的url写入 masql


#=====================================================
【1】【Sqlalchemy - ORM - 声明式映射】
     【连接数据库 - 创建database + 创建table】
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

db = create_engine('mysql://root:123456@127.0.0.1')   		# 连接mysql
db.execute('CREATE DATABASE lxfpy')							# 创建 database lxfpy
db.execute('USE lxfpy')										# 使用 database lxfpy
Base = declarative_base()									# 创建对象的基类:

class Example1(Base):										# 定义example1对象=example1表
	__tablename__ = 'example1'

	user_id = Column(Integer,primary_key=True)
	name = Column(String(49))
	fullname = Column(String(40))
	password = Column(String(40))
	def __repr__(self):										# 方便打印，不用def print()了
		return "<example1(name='%s',fullname='%s',password='%s')>"%(self.name,self.fullname,self.password)

class Example2(Base):										# 定义example2对象=example2表
	__tablename__ = 'example2'

	user_id = Column(Integer,primary_key=True)
	name = Column(String(49))
	age = Column(Integer)
	def __repr__(self):
		return "<example1(name='%s',age='%s')>"%(self.name,self.age)

#Base.metadata.create_all(db)		#若已创建，就不用再执行
example1 = Example1(name='lxf',fullname='lixuefei',password='123456')
session = sessionmaker(bind=db)
session = session()
session.add(example1)
session.commit()

#=====================================================
【2】【Sqlalchemy - ORM - 声明式映射】
     【insert 一条数据】
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

db = create_engine('mysql://root:123456@127.0.0.1')   		# 连接mysql
db.execute('USE lxfpy')										# 使用 database lxfpy
Base = declarative_base()									# 创建对象的基类:

class Example1(Base):										# 定义example1对象=example1表
	__tablename__ = 'example1'
	user_id = Column(Integer,primary_key=True)
	name = Column(String(49))
	fullname = Column(String(40))
	password = Column(String(40))
	def __repr__(self):										# 方便打印，不用def print()了
		return "<example1(name='%s',fullname='%s',password='%s')>"%(self.name,self.fullname,self.password)
class Example2(Base):										# 定义example2对象=example2表
	__tablename__ = 'example2'
	user_id = Column(Integer,primary_key=True)
	name = Column(String(49))
	age = Column(Integer)
	def __repr__(self):
		return "<example1(name='%s',age='%s')>"%(self.name,self.age)

Base.metadata.create_all(db)		
example1 = Example1(name='lxf',fullname='lixuefei',password='123456') # 创建新对象=插入的数据
session = sessionmaker(bind=db)
session = session()
session.add(example1)										# 添加到session:
session.commit()											# 提交即保存到数据库:


#s = users.select()
s = session.query(Example1).select()
rs = s.exectue()
row = rs.fetchone()
for row in rs:			# 等同 select * from example0
        print row

s = users.select()
rs = s.execute()
row = rs.fetchone()
print 'Id:', row[0]
