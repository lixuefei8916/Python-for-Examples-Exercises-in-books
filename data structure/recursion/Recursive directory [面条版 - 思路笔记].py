#-*- coding: utf-8 -*-
# FTP里 进入某个目录， 下载该文件夹下所有文件 和 目录中的文件
# 连接FTP - 进入Office_Professional...目录 -- 下载所有程序
# 难点：递归 - 目录里的目录
# 参考http://blog.chinaunix.net/uid-21516619-id-1825037.html

from ftplib import FTP 
import os
import sys
import re

ftp = FTP() 									#绑定实例， ftp = FTP这个对象

ftp_timeout = 30
ftp_port = 21
ftp_server = '192.168.xx.xx'

ftp.connect(ftp_server,ftp_port,ftp_timeout)	# 连接FTP
ftp.login('xxxxx','xxxxxxx')			# 登录FTP

# ----------------------------------------------------------
#print ftp.getwelcome()							# 回显 FTP登录的欢迎信息

now_ftp_dir_list = '/'							
# 这里代表 FTP登录后的根目录，也是主目录，无论进入任何一个文件夹，都从根开始
ftp_download_dir_name = 'SW_DVD5_Office_Professional_Plus_2013_64Bit_ChnSimp_MLF_X18-55285'
# 我想下载 office


# ----------------------------------------------------------

now_local_dir_list = r'c:\xxxxx\ '	
#创建本地目录（用于下载的文件存放）	
#os.mkdir(file_dir)
#在本地创建该文件夹

'''
===================================================================================================================================================
想法 + 难点

难点1：  遍历整个目录 （目录里的目录，多层目录）
难点2：  ftp的cwd进入目录必须用绝对路径， 即从根开始： 根 + 第1次递归的目录 + ... + 第N次递归的目录
难点3：  客户端本地目录， 同步 ftp目录（同难点2）

# 递归的实现（感谢魏忠指导 2015.12.23 11：30）
# 递归目录，自己调用自己，当发现是文件夹，就再次return回给自己(dir列表)；
# 直至最里层目录，不再有目录后，再回外层目录，然后再次递归
'''

def dir_recursion(ftp_download_dir_name,now_ftp_pwd = '/',now_local_dir_list=now_local_dir_list):
	# ftp_download_dir_name是递归的next级目录， ， now_ftp_pwd是当前目录的绝对目录（从/根开始的绝对路径）
	# now_local_dir_list=now_local_dir_list	：客户端当前绝对路径，随着递归的深入，目录层数也会增加；默认是c:\ops1905\ （只有第1次递归用到根）
	
	now_ftp_pwd = '%s/%s' %(now_ftp_pwd,ftp_download_dir_name)	
	# 等号左边的now_ftp_pwd是绝对路径，一层一层加的，（/xx/xx/ + next目录）； 即：第1次是根'/想下载的主目录', 第二次'/主目录/xx',第三次'/xx/xx/xx'

	#print '\n\n %s' %now_dir_list 								# 自己测试用

	ftp.cwd(now_ftp_pwd)										# cd进ftp的绝对路径 now_dir_list（/xx/xx/xx）
	files_list = []												# 用于存放 这个目录下， 所有的文件和文件夹的列表
	ftp.dir('.',files_list.append)								# ftp.dir是查询这个目录下， 所有的文件和文件夹， 然后，用列表方式赋值给files_list
	files = [f.split(None, 8)[-1] for f in files_list if f.startswith('-')]			#提取 所有 files的文件  -r--r--r--
	dirs = [f.split(None, 8)[-1] for f in files_list if f.startswith('d')]			#提取 所有 dir文件夹	drwxr-xr-x


	now_local_dir_list = '%s%s\ ' %(now_local_dir_list,ftp_download_dir_name)		# 客户端 本地目录，当前目录+next目录（c:\xx\ + next目录）
	os.mkdir(now_local_dir_list)													# 在本地创建这个目录 （本地目录 = ftp的目录，每当ftp要进入下一级目录，就先在本地创建这个目录）


	for name in dirs:																# 将 列表dirs 逐个列出来								
		dir_recursion(name,now_ftp_pwd,now_local_dir_list)							# ★★ 带着next目录，调用自己！！

'''
===================================================================================================================================================
'''
dir_recursion(ftp_download_dir_name)
ftp.quit()



'''
笔记 + 思路猜想 + 尝试

 【 判断是目录还是文件夹 】
# ftp.dir 显示目录下所有目录信息 | 用列表类型存在dir_res
dir_res = []	
ftp.dir('.', dir_res.append)				用列表类型存在dir_res
for file_name in dir_res:
	pattern = re.compile(r'^-')				判断是否为 文件
	x = pattern.match(file_name)
	if x:
		print 'File : %s' %file_name
	else:									如果不是 文件
		pattern = re.compile(r'^d')			判断是否为 目录
		x = pattern.match(file_name)
		if x:
			print 'DDDD : %s' %file_name





local_path = file_dir+download_file
f = open(local_path,'wb')

filename = 'RETR '+download_file
ftp.retrbinary(filename,f.write)
ftp.quit()
'''
