#-*- coding: utf-8 -*-
# 两个对象 共享函数 
# 封装session避免重复链接   def session_keeping
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select,text

class Mysql_(object):
	def __init__(self):
		pass
	def session_keeping(self):
		db = create_engine('mysql:liuefei:123456@127.0.0.1')
		db.execute('USE conference')
		Session = sessionmaker(bind=bd)
		session = Session() 
		【【【 return session 】】】 重点地方

Base = declarative_base()
class Account_model(Base):						# Account_model = account表名(mysql)
	pass

class Lxf2(object):
	def __init__(self):
		self.model = Account_model()			# 表 account
		【【【【 self.mysql = Mysql_() 】】】】					# session封装之后的 调用
		【【【【 self.session = self.mysql.session_keeping() 】】】】
	def select_account_detail(self):
		account = Account_model(user_name=self.__user_name,user_password=self.__user_password,user_mail=self.__user_mail)
		account_detail = 【【【【self.session】】】】】.query(Account_model).filter(Account_model.user_id==13).one()
		
lxf = Lxf2()
lxf.select_account_detail()