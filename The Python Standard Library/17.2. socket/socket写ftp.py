#-*- coding:utf-8 -*-
# Python:从socket开始，搭建一个最基本功能的FTP服务器

import socket

HOST = '127.0.0.1'		# the remote host
PORT = 21
myencoding = 'Latin1'	# ISO-8859-1

CRLF = '/r/n'			# 发送 FTP命令中必须包含
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))


fiLe = s.makefile('r',AF_INET,SOCKET.STREAM)
print (repr(fiLe.readline()))

s.sendall(('USER 123456' + CRLF ).encode(myencoding)) 
#'USER 123456'与 CRLF中间必须有空格，否则FTP服务器不识别
print(repr(fiLe.readline()))
s.sendall(('PASS 654321' + CRLF ).encode(myencoding))
print(repr(fiLe.readline()))
s.sendall(('PWD' + CRLF ).encode(myencoding))
print(repr(fiLe.readline()))

#print(repr(s.recv(1024)))
s.sendall(b'QUIT /r/n')		#刚方式直接发送字节串，send返回发送的字节串长度
s.sendall(('QUIT ' + CRLF ).encode(myencoding))	 #发送编码之后的字节串，发送成功则返回None

print(repr(fiLe.readline()))
print(repr(fiLe.readline()))
print(repr(fiLe.readline()))
print(repr(fiLe.readline()))
fiLe.close()
s.close()

# ==================================================================

PORT模式约定，由客户端打开一个端口，然后在控制连接上告知服务器该端口号，服务器连接上。
 
PASV模式，也就是本文中所实现的模式。
 
1、控制连接上，客户端发送PASV命令给服务器
 
2、服务器开启一个端口，监听，并把该端口号返回给客户端
 
3、客户端连接该端口
 
一次完整的流程，以LIST命令为例
 
客户端
 
服务端
 
21号端口监听
 
发起连接请求，输入用户名
 
——》
 
《——
 
返回331，用户名正确
 
输入密码
 
——》
 
《——
 
返回230，密码正确
 
PASV命令
 
——》
 
《——
 
227，开启新端口，并返回端口号K
 
此时客户端与服务器的端口K建立了数据连接
 
LSIT命令
 
——》
 
《——
 
125，数据连接已经开启
 
《——
 
从K端口，返回对应目录文件列表
 
《——
 
226，数据传输完毕
 
.......
 
...............
 
....................
 
Socket、thread、os、time简单介绍和使用
 
Socket:
 
本程序中用到的socket功能很简单，包括创建socket，监听，接受连接，连接文件化，发送接收数据，关闭连接。详看主要部件的介绍部分，或参考其他资料，这里不多说。
 
Thread:
 
本程序中只用到start_new_thread(func,(args))，就像看到的，该函数接收两个参数，一个是希望新线程中执行的函数，还有就是希望给该函数传入的参数。
 
这是一个轻量级的开启线程的方法，更好的做法是继承线程类，把一个类做成线程，有自己的资源可以访问。
 
Os:
 
本文中主要涉及到的是，os.chdir(),os.getcwd(),os.mkdir()等等，这些关于变更目录的操作
 
Time:
 
参考了pyftpdlib中对时间的处理，不多，建议参考介绍时间库的文章详看。
 
实现思路
 
首先创建一个主socket绑定到21端口。
 
然后以一个while循环接受用户的连接，每接受一个连接就开启一个新线程与该用户交互。
 
在线程中又以一个while循环来接收用户命令，每接到一条命令，就对用户的命令和传递参数进行解析，并调用对应的handler函数处理。
 
如遇到pasv操作，则在handler_pas中建立新的socket并返回给客户端。
 
大致思路如此。详看代码部分。