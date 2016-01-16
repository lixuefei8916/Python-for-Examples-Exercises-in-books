#-*- coding: utf-8 -*-
import os
import sys
import uuid
import time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select,text
from sqlalchemy import func, or_, not_,and_

'''
第二版
2016.01.13

执行一步，记录一次step code，
第一次insert后，还要select到该id，然后主程序每执行一步，都update到这个id记录中的 detail字段（日志详细 字段）
【解决第一版问题： 当程序完成时再执行sql的insert，但若程序中途故障，导致不会执行到mysql insert，也就看不到日志了】

================================================================================
程序步骤：
class pc_ (记录 mac，程序开始时间、程序结束时间)
class sql_ 

lxf1 = pc_()
lxf1.get_mac()
lxf1.get_time_start()

lxf2 = sql_()
lxf.insert(mac=xx,time_start=xx)  	【注：这里id不指定，按照mysql字段要求，自增且唯一】
lxf.select(time_start=xx)			【查询到 id，以便之后往这条sql中insert】

helpdesk1905__主程序(第一步)
lxf.update(,detail_log = 1 ) where id=xx

helpdesk1905__主程序(第二步)
lxf.update(detail_log = 2 ) where id=xx

helpdesk1905__主程序(第n步)
lxf.update(detail_log = n ) where id=xx

lxf.update(time_end = xx ) where id=xx
【time_end 记录该程序完成时间，若有该记录，则表示程序执行成功(至于响应者问题是否解决另议)】

'''


#初始化数据库
sql_name = 'mysql'
sql_user = 'lixuefei'
sql_passwd = '********'
sql_host = '192.168.*.*'

database_name = 'helpdesk' 

#Start
Base = declarative_base()



class pc_(object):
	def __init__(self):
		self.detail_log = []

	def get_mac(self): 
		mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
		return ":".join([mac[e:e+2] for e in range(0,11,2)])

	def get_start_time(self):
		time_start = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
		return time_start

	def get_end_time(self):
		time_end = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
		return time_end


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
		return "<lxf_test2(id='%s',mac='%s',time_start='%s',time_end='%s',details='%s')>" %(self.id,self.mac,self.time_start,self.time_end,self.details)

class Sql_Statement(object):
	def __init__(self):
		# db = create_engine('mysql://root:*****@192.168.*.*')
		self.__database_login_commond = '%s://%s:%s@%s' %(sql_name,sql_user,sql_passwd,sql_host)
		self.__database_name = 'USE %s' %(database_name)

		db = create_engine(self.__database_login_commond)
		db.execute(self.__database_name)
		Session = sessionmaker(bind=db)
		self.session = Session()

	#只填写某字段,未填写部分 “NULL”  : INSERT INTO example2(id,course)VALUES(4,44); 
	#INSERT INTO lxf_test2(time_start)VALUES('2016.01.13 14:33:20');
	def insert_(self,id=None,mac=None,time_start=None,time_end=None,details=None):		#把默认值 = None,只需要传需要的参数即可
		sql_table = Table_lxf_test2(id=id,mac=mac,time_start=time_start,time_end=time_end,details=details)
		self.session.add(sql_table)
		self.session.commit()	

	def select_id(self,time_start,mac):		#利用time_start和mac组合条件， .first()是提取第1行（因为该机器在x分x秒最快也只会运行1个工具，所以暂定查询结果只有1行）
		sql_id = self.session.query(Table_lxf_test2).filter(and_(Table_lxf_test2.time_start==time_start,Table_lxf_test2.mac==mac)).first().id #.id是只要 id结果，其他不显示
		return sql_id

	def update_details(self,id=None,mac=None,time_start=None,time_end=None,details=None):
		id = sql_id
		#self.session.query(Table_lxf_test2).filter(Table_lxf_test2.id == sql_id).update({Table_lxf_test2.details:details}or{Table_lxf_test2.time_end:time_end})
		#上面那种方式是错误的， 因为 detail和time_end 两个字段不会同时更新，只能1个1个更新，所以当更新time_end时，会吧details原值抹去，改为null
		# 还是拆开更新吧
		self.session.query(Table_lxf_test2).filter(Table_lxf_test2.id == sql_id).update({Table_lxf_test2.details:details})

	def update_tiem_end(self,id=None,mac=None,time_start=None,time_end=None,details=None):
		id = sql_id
		self.session.query(Table_lxf_test2).filter(Table_lxf_test2.id == sql_id).update({Table_lxf_test2.time_end:time_end})

# 程序即将开始执行， 记录使用者机器的 mac 和 时间（精确到秒）
lxf1 = pc_()
mac = lxf1.get_mac()
start_time = lxf1.get_start_time()

# 启动sql_insert  mac 和 开始时间
lxf2 = Sql_Statement()
lxf2.insert_(mac=mac,time_start=start_time)

# 查询到 id，以便之后往这条sql中insert
sql_id = lxf2.select_id(start_time,mac)
#print 'id = %s' %sql_id


# =================================================================================
# helpdesk主程序开始 步骤1 例如： 停止打印服务
class Step_1(object):
	def __init__(self):
		self.sql__ = Sql_Statement()

	def stop_spooler(self):
		cmd_commond1 = 'net stop spooler'
		os.system(cmd_commond1)
		# 注意：此时是更新sql记录  update lxf_test2 set details ='1' where id='XX';
		self.sql__.update_details(id=sql_id,details=1)

	def start_spooler(self):
		cmd_commond2 = 'net start spooler'
		os.system(cmd_commond2)
		# 注意：此时是更新sql记录的details字段  update lxf_test2 set details='2' where id='XX';
		# 第一次更新： details = 1
		# 第二次更新： details = 2 （把1抹去了， 换成了2）
		self.sql__.update_details(id=sql_id,details=2)


lxf3 = Step_1()
lxf3.stop_spooler()
lxf3.start_spooler()


#最后，helpdesk主程序结束， 更新sql的“结束时间”
lxf1 = pc_()
end_time = lxf1.get_end_time()
lxf2 = Sql_Statement()
lxf2.update_tiem_end(id=sql_id,time_end=end_time)


=================================================================
【结果如下】
mysql> select * from lxf_test2;
+----+-------------------+---------------------+---------------------+---------+
| id | mac               | time_start          | time_end            | details |
+----+-------------------+---------------------+---------------------+---------+
|  1 | 52:ed:25:03:7a:56 | 2016-01-11 20:11:12 | 2016-01-11 20:11:12 |  4 	   |
+----+-------------------+---------------------+---------------------+---------+
3 rows in set (0.00 sec)
