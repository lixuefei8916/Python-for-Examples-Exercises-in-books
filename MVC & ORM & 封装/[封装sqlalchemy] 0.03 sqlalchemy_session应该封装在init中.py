#-*- coding: utf-8 -*-

'''
# from Python08.docx (no web view)
# Learn to walk before you run.

学习目的：简单的MVC及ORM实现，希望代码思路正确 (Model使用sqlalchemy / View 暂时print / Controller从model取值，传递给view打印)
程序介绍：账户注册，insert用户名、密码和邮箱(假设用户输入的符合规范，更成熟功能后期完善)，
          print出查询结果
学习日期：2015.12.01

修改记录
【当前】registe_0.031[session应该封装在init中]
registe_0.030[错误：session应该封装在init里-不应该在def session_keeping中]
registe_0.02[增加view(print), 无web view]
registe_0.01[无view,无select]
'''



from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select,text

#	account = Account_model(user_name=self.__user_name,user_password=self.__user_password,user_mail=self.__user_mail)

class Mysql_(object):
	def __init__(self):
		db = create_engine('mysql://lixuefei:123456@127.0.0.1')
		db.execute('USE conference')
		Session = sessionmaker(bind=db)
		self.session = Session()

	def insert_new_account(self,table_name,user_name,user_password,user_mail):
	
		account = Table_account_model(user_name=user_name,user_password=user_password,user_mail=user_mail)
		self.session.add(account)
		self.session.commit()

	def select_account_detail(self,user_name):		# select user_id==13 from account
		#account = Account_model(user_name=self.__user_name,user_password=self.__user_password,user_mail=self.__user_mail)
		account_detail = self.session.query(Table_account_model).filter(Table_account_model.user_name==user_name).all()
		return account_detail


Base = declarative_base()	# 声明ORM父类 Base

class Table_account_model(Base):						# Account_model = account表名(mysql)
	__tablename__ = 'account'
	#原mysql语句
	#CREATE TABLE account(user_id INT PRIMARY KEY AUTO_INCREMENT,user_name VARCHAR(250),user_password VARCHAR(250),user_mail VARCHAR(250));
	user_id = Column(Integer,primary_key=True)	# id自增id=id+1 AUTO_INCREMENT ; PRIMARY KEY 拥有自动定义的 UNIQUE 约束。
	user_name = Column(String(250))				# user_name 唯一性 UNIQUE
	user_password = Column(String(250))
	user_mail = Column(String(250))

	def __repr__(self):
		return "<account(user_id='%s',user_name='%s',user_password='%s',user_mail='%s')>"%(self.user_id,self.user_name,self.user_password,self.user_mail)

class View(object):
	def __init__(self):
		pass

	def print_account_detail(self,account_detail):		#接收 class Account_Controller.(def)get_account_detail的查询结果，然后print出来
		print account_detail

class Account_Controller(object):
	def __init__(self):
		#self.model = Table_account_model()
		self.view = View()
		self.mysql = Mysql_()
		#self.session = self.mysql.session_keeping()	# 把 class Mysql_operation()中session带进来

		self.__user_name = ''
		self.__user_password = ''
		self.__user_mail = ''

	def registe_user_name(self,user_name):					# 接收用户的 username (暂且 先假设用户输入的符合规范，更成熟功能后期完善)
		self.__user_name = user_name

	def registe_user_password(self,user_password):			# 接收用户的 password(暂且 先假设用户输入的符合规范，更成熟功能后期完善)
		self.__user_password = user_password

	def registe_user_mail(self,user_mail):					# 接收用户的 邮箱(暂且 先假设用户输入的符合规范，更成熟功能后期完善)
		self.__user_mail = user_mail

	def insert_account_detail(self):						# insert 进mysql
		#Insert数据
		table_name = Table_account_model
		self.mysql.insert_new_account(table_name,self.__user_name,self.__user_password,self.__user_mail)

	def get_account_detail(self,user_name):							# select user_id==13 from account
		account_detail = self.mysql.select_account_detail(user_name)
		self.view.print_account_detail(account_detail)



username = 'example15'
userpassword = '151515151515'
usermail = 'example15@lixuefei.com'

if __name__ == '__main__':
	lxf = Account_Controller()
	lxf.registe_user_name(username)
	lxf.registe_user_password(userpassword)
	lxf.registe_user_mail(usermail)
	lxf.insert_account_detail()
	lxf.get_account_detail('example15')




