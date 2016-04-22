'''
==================================================
修改windows regedit注册表
==================================================
'''

'''
使用原因：
2015.12.30， 修改打印机IP端口时，发现只有用regedit才能修改，用powershell太繁琐
而 用python写一个.reg文件后运行时，提示不是二进制文件
还好，有标准库来解决
'''

KEY 键
Value 值
函数和作用:
CloseKey() – 关闭一个Key
ConnectRegistry() – 链接到其他机器的注册表
CreateKey() – 创建一个Key
DeleteKey() – 删除一个Key
DeleteValue() – 删除一个Key里面的值（value）
EnumKey() – 为已经打开的Key里面的子键建立索引
EnumValue() – 为打开的键中的值建立索引
FlushKey() – 回写所有的键属性改变到注册表
LoadKey() – 从指定文件读入键信息
OpenKey() – 打开一个键
OpenKeyEx()
QueryValue() – 在注册表中检索一个键的路径
QueryValueEx() – 注册表中检索一个键的路径
QueryInfoKey() – 返回关于键的信息
SaveKey() – 保存键到文件
SetValue() – 设置一个键
SetValueEx() – 设置一个值
FAQ:
python操作注册表出现“WindowsError: (5, ”)”
其实解决的办法很简单，通过阅读文档发现，问题在于
_winreg.OpenKey()中的sam参数
sam参数用来定义key的存取类型
查询的设置成READ 写入的设置成WRITE就不会出现WINDOWS 5的错误了



#=====================================================================================
#[读取键值]
#=====================================================================================
# 参考http://blog.sina.com.cn/s/blog_4b5039210100gmsb.html
#读取用的方法是OpenKey方法：打开特定的key
#_winreg.OpenKey(key,sub_key,res=0,sam=KEY_READ)

key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Control\Print\Monitors\HP Standard TCP/IP Port\Ports\HPLaserJetM1536dnfMFP")
try:
	i=0
	while 1:
		#EnumValue方法用来枚举键值，EnumKey用来枚举子键
		name,value,type = _winreg.EnumValue(key,i)
		print repr(name),value,type
		i+=1
except WindowsError:
	print


#假如知道键名，也可以直接取值
value,type = _winreg.QueryValueEx(key,"IPAddress")
print "当前打印机IP：",value,type




#=====================================================================================
#创建子文件夹,名称为：IPAddressss
#=====================================================================================
#_winreg.CreateKey(key, sub_key)
#_winreg.CreateKey(key,"IPAddressssssssssssssss")




#=====================================================================================
#在HPLaserJetM1536dnfMFP下，创建新建值，键名字：xf111    值=testtest22222
#=====================================================================================
# 参考http://www.jb51.net/article/56165.htm   ython修改注册表终止360进程实例

key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Control\Print\Monitors\HP Standard TCP/IP Port\Ports\HPLaserJetM1536dnfMFP",0,_winreg.KEY_WRITE)
_winreg.SetValueEx(key,"lxf111",0,_winreg.REG_SZ,r"testtest22222")


 
#=====================================================================================
#创建REG_DWORD 键值，_winreg.SetValueEx(newkey,"*",None,_winreg.REG_DWORD,0x00000002)
#=====================================================================================
 
# IE信任站点： HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains
key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains")
 
#创建子项（文件夹）名称为：1905.com   代码:_winreg.CreateKey(key, sub_key)
_winreg.CreateKey(key,"lxflxflxf.com")
 
newkey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\lxflxflxf.com",0,_winreg.KEY_WRITE)
_winreg.SetValueEx(newkey,"*",None,_winreg.REG_DWORD,0x00000002)


