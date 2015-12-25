
Windows下,将一个py转为单个exe文件

参考：http://blog.csdn.net/hmy1106/article/details/45151409


1. 下载并解压 F:\pyinstaller-develop


2. 安装，cmd下执行
		cd F:\pyinstaller-develop
		python setup.py install   [成功后最后一行返回 Finished]

3. 转exe文件，cmd下执行
		python PyInstaller.py  0lxf\lxfstudy-office.py

4. exe文件默认位置
		F:\pyinstaller-develop\lxfstudy-office\dist\xxx[文件名]


5. -F 打成一个exe文件
	F:\pyinstaller-develop>python pyinstaller.py -F 0lxf\Office2013_automatically_installed.py
	-F 是打包成一个文件 ，如果不加参数-F，就会生成1个目录，里面N个文件