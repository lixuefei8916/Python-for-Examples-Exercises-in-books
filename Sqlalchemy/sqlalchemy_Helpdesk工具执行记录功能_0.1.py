#-*- coding: utf-8 -*-
import time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select,text


'''
helpdesk工具记录 第一版
2016.01.12

该方法是程序运行完后再执行 mysql
但如果程序中途退出，则无法 insert
'''



#初始化数据库
sql_name = 'mysql'
sql_user = 'lixuefei'
sql_passwd = '******'
sql_host = '192.168.*.*'

database_name = 'helpdesk' 

#Start
Base = declarative_base()

class Table_lxf_test2(Base):
	__tablename__ = 'lxf_test2'		#mysql Talbe名称，1个exe文件对应1个表
	#表结构
	#CREATE TABLE lxf_test2(id INT PRIMARY KEY AUTO_INCREMENT,mac VARCHAR(17),time_start VARCHAR(255),time_end VARCHAR(255),details VARCHAR(255));
	id = Column(Integer,primary_key=True)
	mac = Column(String(17))
	time_start = Column(String(255))
	time_end = Column(String(255))
	details = Column(String(255))

def __repr__(self):
	return "<lxf_test2(id='%s',mac='%s',time_start='%s',time_end='%s',details='%s')>" %(id,mac,time_start,time_end,details)

class Sql_Statement(object):
	def __init__(self):
		# db = create_engine('mysql://root:*****@192.168.*.*')
		self.__database_login_commond = '%s://%s:%s@%s' %(sql_name,sql_user,sql_passwd,sql_host)
		self.__database_name = 'USE %s' %(database_name)

		db = create_engine(self.__database_login_commond)
		db.execute(self.__database_name)
		Session = sessionmaker(bind=db)
		self.session = Session()

	def insert_(self,mac,time_start,time_end,details):
		sql_table = Table_lxf_test2(mac=mac,time_start=time_start,time_end=time_end,details=details)
		self.session.add(sql_table)
		self.session.commit()	


#获取本机mac
import uuid
def get_mac_address(): 
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
    return ":".join([mac[e:e+2] for e in range(0,11,2)])
mac = get_mac_address()



#获取当前时间
time_start = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

#执行过程的记录
detail_log = ['']
detail_log.append('1')
detail_log.append('2')
detail_log.append('3')
detail_log.append('4')
details = ' '.join(detail_log)


lxf = Sql_Statement()
lxf.insert_(mac,time_start,time_start,details)
=================================================================
【结果如下】
mysql> select * from lxf_test2;
+----+-------------------+---------------------+---------------------+---------+
| id | mac               | time_start          | time_end            | details |
+----+-------------------+---------------------+---------------------+---------+
|  1 | 52:ed:25:03:7a:56 | 2016-01-11 20:11:12 | 2016-01-11 20:11:12 | 1 2 3 4 |
+----+-------------------+---------------------+---------------------+---------+
3 rows in set (0.00 sec)
