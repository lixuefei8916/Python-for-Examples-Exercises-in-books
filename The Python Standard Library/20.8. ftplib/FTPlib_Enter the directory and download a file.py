#-*- coding: utf-8 -*-
# FTP里 进入xxx目录下载
# 连接FTP - 进入Office_Professional...目录 -- 下载setup.exe程序

from ftplib import FTP 
import os
import sys

ftp = FTP() 		#绑定实例， ftp = FTP这个对象

ftp_timeout = 30
ftp_port = 21
ftp_server = '192.168.xxx.xxx'

ftp.connect(ftp_server,ftp_port,ftp_timeout)	# 连接FTP
ftp.login('username','lpassword')			# 登录FTP

# ----------------------------------------------------------
#print ftp.getwelcome()							# 回显 FTP登录的欢迎信息


#创建本地目录（用于下载的文件存放）
file_dir = 'c:\mypwd\SW_DVD5_Office_Professional_Plus_2013_64Bit_ChnSimp_MLF_X18-55285\\'	
#os.mkdir(file_dir)

#要下载的文件名
download_file = 'setup.exe'

#FTP里的文件夹名
download_pwd = 'SW_DVD5_Office_Professional_Plus_2013_64Bit_ChnSimp_MLF_X18-55285'
#在FTP里进入该文件夹
ftp.cwd(download_pwd)

#本地目录和文件名
local_path = file_dir+download_file
f = open(local_path,'wb')

#执行下载
filename = 'RETR '+download_file
ftp.retrbinary(filename,f.write)

#退出ftp连接
ftp.quit()