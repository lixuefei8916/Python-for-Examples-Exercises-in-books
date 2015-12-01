# -*- coding: utf-8 -*-
#u'2.	Alist = [a1,a2… an] 求一个列表中最大的元素。'

def func(*x):
	s = 0
	for i in x:
		if i>=s :
			s = i
	return s
f = [23,4,35,255,1,23,56,2,6,12]
print func(*f)