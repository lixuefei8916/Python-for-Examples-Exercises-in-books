# -*- coding: utf-8 -*-
print u"元组 转换为 列表"

tunple1 = ('lee1','tom','tony','ann')
print tunple1 , type(tunple1)

list1 = []
for i in tunple1:
	list1.append(i)

print list1 , type(list1)