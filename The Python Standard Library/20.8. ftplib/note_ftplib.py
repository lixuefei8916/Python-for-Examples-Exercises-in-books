#-*- coding: utf-8 -*-

#-*- coding: utf-8 -*-
from ftplib import FTP
import os
import sys

#---------------------------------
# from  The Python Standard Library » 20.8. ftplib — FTP protocol client

>>> from ftplib import FTP
>>> ftp = FTP('192.168.xx.xx')     # connect to host, default port
>>> ftp.login()
#此时返回 ftplib.error_perm: 530 Login or password incorrect!
>>> ftp.cwd('debian')               # change into "debian" directory
>>> ftp.retrlines('LIST')           # list directory contents
#---------------------------------

# from http://blog.csdn.net/linda1000/article/details/8255771

ftp = FTP()
timeout = 30
port = 21
ftp_server = '192.168.xxxxxxx.xxxxx'

ftp.connect(ftp_server,port,timeout)	# 连接ftp服务器
ftp.login('xxxxx','xxxxxxxx')	# 登录

file_dir = r'f:\1905ops\ '				# 客户端本地下载目录

print ftp.getwelcome()					# 打印欢迎信息
#此时回显
#220-FileZilla Server version 0.9.34 beta
#220-written by Tim Kosse (Tim.Kosse@gmx.de)
#220 Please visit http://sourceforge.net/projects/filezilla/

ftp_list = ftp.nlst()					# 获取目录列表
for i in ftp_list:
	name = i

os.mkdir(file_dir)						# 创建 本地下载文件夹
path = file_dir+name					# f:\1905ops\xxxxxx.exe
f = open(path,'wb')						# 读写权限，打开该目录和文件

filename = 'RETR '+name					# 保存ftp文件
ftp.retrbinary(filename,f.write)		# 从FTP下载文件
ftp.quit()								# 退出FTP

#=======================================================================

from ftplib import FTP
import os
import sys
import time

#想下载的文件
download_file = 'rtxclient2011formal.exe'

ftp = FTP()

ftp_server = '192.168.xxx.xxx'
ftp_port = 2100
ftp_timeout = 30

ftp_user = 'xxxxx'
ftp_passwd = 'xxxxxxxxxxx'

file_dir = 'c:\Myinstall\\'			# 客户端本地下载目录


class Local_dir(object):
	def __init__(self):
		self.__file_dir = file_dir

	def mkdir(self):
		os.mkdir(self.__file_dir)

class FTP(object):
	def __init__(self):
		self.ftp_server = ftp_server
		self.ftp_port = ftp_port
		self.ftp_timeout = ftp_timeout

		self.ftp_user = ftp_user
		self.ftp_passwd = ftp_passwd

		self.path = file_dir + download_file

	def ftp_connect(self):
		ftp.connect(self.ftp_server,self.ftp_port,self.ftp_timeout)	# 连接ftp服务器
		return self.ftp_login()

	def ftp_login(self):
		ftp.login(self.ftp_user,self.ftp_passwd)	# 登录
		return self.download()

	def download(self):
		f = open(self.path,'wb')				# 读写权限，打开该目录和文件
		filename = 'RETR '+download_file		# 保存ftp文件
		ftp.retrbinary(filename,f.write)		# 从FTP下载文件
		ftp.quit()		


lxf=Local_dir()
lxf.mkdir()
lxf = FTP()
lxf.ftp_connect()
lxf = rtx_software()


