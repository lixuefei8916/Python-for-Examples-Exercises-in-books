#-*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select,text
from sqlalchemy import func, or_, not_,and_

'''
注：前70行是sqlalchemy基础定义 + 1个简单insert功能；之后全部为 select查询功能
参考：http://www.jb51.net/article/49789.htm   SQLAlchemy基本操作和常用技巧（包含大量实例,非常好）
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

	def insert_(self,id=None,mac=None,time_start=None,time_end=None,details=None):		#把默认值 = None,只需要传需要的参数即可
		sql_table = Table_lxf_test2(id=id,mac=mac,time_start=time_start,time_end=time_end,details=details)
		self.session.add(sql_table)
		self.session.commit()	

	# and 组合查询 + 全部结果均显示	
	def select_id(self,time_start,mac):		#利用time_start和mac组合 去查询出id
		sql_all = self.session.query(Table_lxf_test2).filter(and_(Table_lxf_test2.time_start==time_start,Table_lxf_test2.mac==mac)).all()
		return sql_all


	# and 组合查询 + 只要 id字段
	def select_id(self,time_start,mac):		#利用time_start和mac组合条件， .first()是提取第1行（因为该机器在x分x秒最快也只会运行1个工具，所以暂定查询结果只有1行）
		sql_id = self.session.query(Table_lxf_test2).filter(and_(Table_lxf_test2.time_start==time_start,Table_lxf_test2.mac==mac)).first().id #.id是只要 id结果，其他不显示
		return sql_id
# ==============================================================================================
# select查询实例

from sqlalchemy import func, or_, not_

user = User(name='a')
session.add(user)
user = User(name='b')
session.add(user)
user = User(name='a')
session.add(user)
user = User()
session.add(user)
session.commit()
query = session.query(User)


print query # 显示SQL 语句
print query.statement # 同上

for user in query: # 遍历时查询
    print user.name

print query.all() # 返回的是一个类似列表的对象
print query.first().name # 记录不存在时，first() 会返回 None
# print query.one().name # 不存在，或有多行记录时会抛出异常
print query.filter(User.id == 2).first().name
print query.get(2).name # 以主键获取，等效于上句
print query.filter('id = 2').first().name # 支持字符串
query2 = session.query(User.name)
print query2.all() # 每行是个元组
print query2.limit(1).all() # 最多返回 1 条记录
print query2.offset(1).all() # 从第 2 条记录开始返回
print query2.order_by(User.name).all()
print query2.order_by('name').all()
print query2.order_by(User.name.desc()).all()
print query2.order_by('name desc').all()
print session.query(User.id).order_by(User.name.desc(), User.id).all()
print query2.filter(User.id == 1).scalar() # 如果有记录，返回第一条记录的第一个元素
print session.query('id').select_from(User).filter('id = 1').scalar()
print query2.filter(User.id > 1, User.name != 'a').scalar() # and
query3 = query2.filter(User.id > 1) # 多次拼接的 filter 也是 and
query3 = query3.filter(User.name != 'a')
print query3.scalar()
print query2.filter(or_(User.id == 1, User.id == 2)).all() # or
print query2.filter(User.id.in_((1, 2))).all() # in
query4 = session.query(User.id)
print query4.filter(User.name == None).scalar()
print query4.filter('name is null').scalar()
print query4.filter(not_(User.name == None)).all() # not
print query4.filter(User.name != None).all()
print query4.count()
print session.query(func.count('*')).select_from(User).scalar()
print session.query(func.count('1')).select_from(User).scalar()
print session.query(func.count(User.id)).scalar()
print session.query(func.count('*')).filter(User.id > 0).scalar() # filter() 中包含 User，因此不需要指定表
print session.query(func.count('*')).filter(User.name == 'a').limit(1).scalar() == 1 # 可以用 limit() 限制 count() 的返回数
print session.query(func.sum(User.id)).scalar()
print session.query(func.now()).scalar() # func 后可以跟任意函数名，只要该数据库支持
print session.query(func.current_timestamp()).scalar()
print session.query(func.md5(User.name)).filter(User.id == 1).scalar()
query.filter(User.id == 1).update({User.name: 'c'})
user = query.get(1)
print user.name
user.name = 'd'
session.flush() # 写数据库，但并不提交
print query.get(1).name
session.delete(user)
session.flush()
print query.get(1)
session.rollback()
print query.get(1).name
query.filter(User.id == 1).delete()
session.commit()
print query.get(1)


