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


