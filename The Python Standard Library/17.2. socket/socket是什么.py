#-*- coding:utf-8 -*-


socket是什么
from http://bbs.51cto.com/thread-1166008-1.html

使用socket时需要指定Socket Family（地址簇），包括以下几种：
socket.AF_UNIX       只能够用于单一的Unix系统进程间通信
socket.AF_INET      用于主机之间的网络通信
socket.AF_INET6    IPv6通信
若想实现主机之间的通信，我们就得使用socket.AF_INET

确认地址簇后，还需要指定socket 数据类型
socket.SOCK_STREAM     流式socket, for TCP
socket.SOCK_DGRAM       数据报式socket, for UDP
socket.SOCK_RAW    原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；其次，SOCK_RAW也可以处理特殊的IPv4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头。
socket.SOCK_RDM   是一种可靠的UDP形式，即保证交付数据报但不保证顺序。SOCK_RAM用来提供对原始协议的低级访问，在需要执行某些特殊操作时使用，如发送ICMP报文。SOCK_RAM通常仅限于高级用户或管理员运行的程序使用。
socket.SOCK_SEQPACKET      可靠的连续数据包服务

我们主要用的一般是SOCK_STREAM (for TCP)和SOCK_DGRAM（for UDP）.


进行socket调用时可能会用到的函数：
s = socket(family,type[,protocal])       使用给定的地址族、套接字类型、协议编号（默认为0）来创建套接字。

套接字的实例具有以下方法：
s.bind(address) 将套接字绑定到地址。address地址的格式取决于地址族。在AF_INET下，以元组（host,port）的形式表示地址。
s.listen(backlog)   开始监听传入连接。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
s.connect(address)  连接到address处的套接字。一般，address的格式为元组（hostname,port），如果连接同一台机器上的服务器，可以将hostname设为‘localhost’。如果连接出错，返回socket.error错误。
s.connect_ex(adddress)  功能与connect(address)相同，但是成功返回0，失败返回errno的值。
s.accept() 接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
s.close()  关闭套接字。
s.fileno()  返回套接字的文件描述符。
s.getpeername() 返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。
s.getsockname()  返回套接字自己的地址。通常是一个元组(ipaddr,port)
s.getsockopt(level,optname[.buflen]) 返回套接字选项的值。
s.gettimeout() 返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。
s.recv(bufsize[,flag])  接受套接字的数据。数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。
s.recvfrom(bufsize[.flag])  与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
s.send(string[,flag])  将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。
s.sendall(string[,flag])  将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。
s.sendto(string[,flag],address)  将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。该函数主要用于UDP协议。
s.setblocking(flag)  如果flag为0，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用recv()没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常。
s.setsockopt(level,optname,value)   设置给定套接字选项的值。
s.settimeout(timeout)   设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如connect()）普通的非套接字实例的函数
getdefaulttimeout()返回默认的套接字超时时间（以秒为单位）。None表示不设置任何超时时间。
gethostbyname(hostname)   将主机名（如“www.baidu.com”）转换为IPv4地址，IP地址将以字符串的形式返回，如“8.8.8.8”。不支持IPv6
gethostname() 返回本地机器的主机名。


