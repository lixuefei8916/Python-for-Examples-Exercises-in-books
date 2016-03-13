
# 如果只正则 中文 [\u4e00-\u9fa5]
re.compile(u'title="[\u4e00-\u9fa5]')


# 实际例子
# <a target="_blank" title="暴风魔镜4代 黄金版 金版" href="//item.jd.com/10057427339.html"
		zh_pattern = html_code.decode('utf8')
		#pattern3 = re.compile(u'[\u4e00-\u9fa5]+') 
		#pattern3 = re.compile(r'<a target="_blank" title=".+') 
		#pattern3 = re.compile(u'title="[\u4e00-\u9fa5]+.+"\s\href')    【OK ，但有纰漏，例如前两行】
		#pattern3 = re.compile(u'title="[\u4e00-\u9fa5]+\s[\u4e00-\u9fa5]+.+"\s\href')  【完全正确的方式，干净、完整】

		pattern3 = re.compile(u'title="[\u4e00-\u9fa5]+\s[\u4e00-\u9fa5]+.+"\s\href')  
		x = pattern3.findall(zh_pattern)

#打印中文
		for i in x:
			pattern4 = re.compile(u'[\u4e00-\u9fa5]+.+"')
			y = pattern4.findall(i)
			for t in y:
				tmp = t.decode('utf-8')
				#print tmp


#如果正则  中文 or 英文 or 特殊字符
		pattern3 = re.compile(u'title=".+\s[\u4e00-\u9fa5]+.+"\s\href')  
		x = pattern3.findall(zh_pattern)
