#-*- coding:utf-8 -*-

socket.getaddrinfo(host, port[, family[, socktype[, proto[, flags]]]])
>>> socket.getaddrinfo("www.python.org", 80, 0, 0, socket.SOL_TCP)

# ipv4 和 ipv6
# pass

#network sniffer with raw sockets on Windows
# pass

#Ipv4的代码
# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()

# Echo client program
import socket

HOST = 'daring.cwi.nl'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)


# =======================================================================

import socket

# 创建一个socket
# AF_INET = IPv4	AF_INET6 = IPv6
# SOCK_STREAM = TCP协议
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 建立连接，把目标地址及目标端口
# 常用端口： SMTP - 25端口，FTP - 21端口
# (参数是个tunple，元组)
s.connect(('www.sina.com.cn',80))
s.send('GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收新浪服务器返回的数据
buffer = []
while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = ''.join(buffer)
s.close


#把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件
header,html = data.split('\r\n\r\n',1)
print header
with open('sina.html','wb') as f:
	f.write(html)

# 最后，直接在浏览器中打开


----------------------------------------------

【服务端】
import socket
import threading
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定端口， 用本机的 9999 作为服务端口
s.bind(('127.0.0.1',9999))

# 监听端口
s.listen(5)
print u'正在接收数据：...'

# 必须多线程处理，否则只能处理1个客户端请求
def tcplink(sock,addr):
	print(u'允许来自 %s:%s...'%addr)
	sock.send(b'welcome')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello,%s!' %data).encode('utf-8'))
	sock.close()
	print(u'来自%s:%s的连接被中断' %addr)


#用循环接收 来自客户端的数据
while True:
	#接受一个新连接
	sock,addr = s.accept()
	# 创建新县城来处理 TCP 连接
	t = threading.Thread(target=tcplink,args=(sock,addr))
	t.start()



【客户端】
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))

print(s.recv(1024).decode('utf-8'))

for data in ['lxf','lixuefei','lee']:
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
