#-*- coding: utf-8 -*-

'''
db_opreation  数据库方面操作
db_config 	  数据库配置文件
 
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select,text

import db_config

Base = declarative_base()

class Table_account(Base):
	__tablename__ = 'account'
	#CREATE TABLE account(user_id INT PRIMARY KEY AUTO_INCREMENT,user_name VARCHAR(250),user_password VARCHAR(250),user_mail VARCHAR(250));
	user_id = Column(Integer,primary_key=True)
	user_name = Column(String(250))
	user_password = Column(String(250))
	user_mail = Column(String(250))
	
	def __repr__(self):
		return "<account(user_id='%s',user_name='%s',user_password='%s',user_mail='%s')>"%(self.user_id,self.user_name,self.user_password,self.user_mail)

class Sql_Statement(object):
	def __init__(self):
		#db = create_engine('mysql://lixuefei:123456@127.0.0.1')
		self.__database_login_command = '%s://%s:%s@%s' %(db_config.sql_name,db_config.user,db_config.passwd,db_config.host)
		self.__database_name = 'USE %s' %(db_config.database_name)

		db = create_engine(self.__database_login_command)
		db.execute(self.__database_name)
		Session = sessionmaker(bind=db)
		self.session = Session()

	def select_account_detail(self,user_name):		# select user_id==13 from account
		#account = Account_model(user_name=self.__user_name,user_password=self.__user_password,user_mail=self.__user_mail)
		account_detail = self.session.query(Table_account).filter(Table_account.user_name==user_name).all()
		return account_detail

lxf = Sql_Statement()
print lxf.select_account_detail('example14')