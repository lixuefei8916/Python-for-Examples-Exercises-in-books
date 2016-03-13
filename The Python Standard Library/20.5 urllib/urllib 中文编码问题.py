import urllib

下载 html源码.html时
	def download_html_file(self):
		reload(sys)							# 规定编码，无此行会报告
		sys.setdefaultencoding( "utf-8" )	# UnicodeEncodeError: 'ascii' codec can't encode characters
		f = file(self.__html_file,'w') 		# 要写的文件 和 赋予写权限
		f.write(self.__html_code)			# 写什么内容
		f.close								# 正常关闭文件
		# 注意，如果是中文， 这里的文件名是有问题的， 怎么转换成中文？

正则 xxx.html 或包含中文时
		reload(sys)							# 规定编码，无此行会报告
		sys.setdefaultencoding( "utf-8" )	# UnicodeEncodeError: 'ascii' codec can't encode characters
		zh_pattern = self.__html_code.decode('utf8') # 以上3行是一组，不可分开，否则 encode报错


列表、字典 想用中文，必须要 JSON
	def result_list(self):
		price_tables = dict(map(lambda x,y:[x,y], self.__items_name_list,self.__price_list))
		tmp = json.dumps(price_tables,encoding='UTF-8', ensure_ascii=False)

		today = datetime.date.today()
		time = today.strftime("%Y%m%d")

		for key,value in price_tables.items():
			print '========================'
			print 'name=',key , '\n' 'price=',value	, '\n' 'time=',time	