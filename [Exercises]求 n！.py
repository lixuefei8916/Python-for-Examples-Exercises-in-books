# -*- coding: utf-8 -*-
#u'1.	求 n！ 也就是 1*2 * 3 * 4.. *n 这个式子的值。'

def func(*x):
	s = 1
	for i in x:
		s = s * i
	return s

x = (1,2,3)
print func(*x)