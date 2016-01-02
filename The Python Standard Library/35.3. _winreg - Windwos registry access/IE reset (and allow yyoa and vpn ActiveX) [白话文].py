#-*-coding: utf-8 -*-

'''
重置浏览器 （解决浏览器故障，无法访问网页等）
'''

import os
import sys
import time
import _winreg

print u'lixuefei辅助工具'
print u'程序正在执行中...（注：程序若遇到问题，请联系xuefei.li）\n'

#==========================================================================
print u'[删除] 上网产生的垃圾、记录、临时文件(需要有inetcpl.cpl)\n'  
#==========================================================================
#参考http://www.itjsxx.com/windows/InetCpl_cpl_ClearMyTracksByProcess.html
cmd_commond1 = 'RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 255'
# RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 255
cmd_commond2 = 'RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 4351' 

#os.system(cmd_commond1)
#os.system(cmd_commond2)

'''
IE重置
RunDLL32.EXE IEdkcs32.dll,Clear

重置Internet Explore ， 但无法静默，需弹窗手工处理；
rundll32 inetcpl.cpl ResetIEtoDefaults
'''
#==========================================================================
print u'[取消] 对"信任站点"区域中的所有站点要求服务器验证 https\n'
#==========================================================================
#[hkey_current_user\software\microsoft\windows\currentversion\internet settings\Zones\2] "flags"=dword:00000043将00000043是关闭，47是开启
newkey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"software\microsoft\windows\currentversion\internet settings\Zones\2",0,_winreg.KEY_WRITE)
_winreg.SetValueEx(newkey,"flags",None,_winreg.REG_DWORD,0x00000043)




#==========================================================================
print u'[添加] *.lixuefei.com.com 到 ie信任站点'
#==========================================================================
# 注册表： HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains
key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains")

#创建子项（文件夹）名称为：1905.com   代码:_winreg.CreateKey(key, sub_key)
_winreg.CreateKey(key,"lixuefei.com")
newkey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\lixuefei.com",0,_winreg.KEY_WRITE)
_winreg.SetValueEx(newkey,"*",None,_winreg.REG_DWORD,0x00000002)



#==========================================================================
print u'[添加] vpn.lixuefei.com 到 ie信任站点'
#==========================================================================
key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\lixuefei.com")
_winreg.CreateKey(key,"vpn")
newkey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\lixuefei.com\vpn",0,_winreg.KEY_WRITE)
_winreg.SetValueEx(newkey,"*",None,_winreg.REG_DWORD,0x00000002)



#==========================================================================
print u'[添加] 关闭信任站点的弹窗阻止 '
#==========================================================================
key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Internet Explorer\New Windows",0,_winreg.KEY_WRITE)
_winreg.SetValueEx(key,"PopupMgr",0,_winreg.REG_SZ,r"no")

#==========================================================================
print u'[添加] 混合内容 *'
#==========================================================================
key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\0",0,_winreg.KEY_WRITE)
_winreg.SetValueEx(key,"1609",None,_winreg.REG_DWORD,0x00000000)

key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\1",0,_winreg.KEY_WRITE)
_winreg.SetValueEx(key,"1609",None,_winreg.REG_DWORD,0x00000000)

#==========================================================================
print u'[添加] 信任站点的 1609:混合内容'
print u'[添加] 信任站点的 1001:下载已签名的ActiveX控件 '
print u'[添加] 信任站点的 1200:运行ActiveX控件和插件 '
print u'[添加] 信任站点的 1405:Script ActiveX controls marked safe for scripting '
print u'[添加] 信任站点的 1201:对没有标记为可安全执行脚本的 ActiveX 控件进行初始化和脚本运行 '
#==========================================================================

key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2",0,_winreg.KEY_WRITE)
_winreg.SetValueEx(key,"1609",None,_winreg.REG_DWORD,0x00000000)
_winreg.SetValueEx(key,"1001",None,_winreg.REG_DWORD,0x00000001)
_winreg.SetValueEx(key,"1200",None,_winreg.REG_DWORD,0x00000000)
_winreg.SetValueEx(key,"1405",None,_winreg.REG_DWORD,0x00000000)
_winreg.SetValueEx(key,"1201",None,_winreg.REG_DWORD,0x00000000)

key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3",0,_winreg.KEY_WRITE)
_winreg.SetValueEx(key,"1609",None,_winreg.REG_DWORD,0x00000000)

key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4",0,_winreg.KEY_WRITE)
_winreg.SetValueEx(key,"1609",None,_winreg.REG_DWORD,0x00000000)



#未来成功 _winreg.REG_BINARY
key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_WINDOW_RESTRICTIONS",0,_winreg.KEY_WRITE)
_winreg.SetValueEx(newkey,"iexplore.exe",None,_winreg.REG_DWORD,0x00000000)
_winreg.SetValueEx(newkey,"explore.exe",None,_winreg.REG_DWORD,0x00000000)


#==========================================================================
print u'[添加] OA环境'
#==========================================================================

key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Ranges")
_winreg.CreateKey(key,"192.168.xx.xx")
newkey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Ranges\192.168.xx.xx",0,_winreg.KEY_WRITE)
_winreg.SetValueEx(newkey,"http",None,_winreg.REG_DWORD,0x00000002)
_winreg.SetValueEx(newkey,":Range",0,_winreg.REG_SZ,r"192.168.xx.xx")
_winreg.SetValueEx(newkey,"https",None,_winreg.REG_DWORD,0x00000002)
_winreg.SetValueEx(newkey,":Range",0,_winreg.REG_SZ,r"192.168.xx.xx")


#==========================================================================
print u'[添加] 绿盟web VPN环境'
#==========================================================================

key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Ranges")
_winreg.CreateKey(key,"8.8.8.8888")
newkey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Ranges\8.8.8.8888",0,_winreg.KEY_WRITE)
_winreg.SetValueEx(newkey,"http",None,_winreg.REG_DWORD,0x00000002)
_winreg.SetValueEx(newkey,":Range",0,_winreg.REG_SZ,r"8.8.8.8888")
_winreg.SetValueEx(newkey,"https",None,_winreg.REG_DWORD,0x00000002)
_winreg.SetValueEx(newkey,":Range",0,_winreg.REG_SZ,r"8.8.8.8888")


print u'已修复完成，10秒后自动退出，【请再次尝试网页】'
time.sleep(10)

