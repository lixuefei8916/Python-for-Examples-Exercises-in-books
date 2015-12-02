#-*- coding: utf-8 -*-
# 两个对象 共享参数(非继承)

class Lxf1(object):
	session = 200
	def __init__(self):
		self.__x = r'This is "class lxf1 -- def __init__" '

	def lxf1_print(self):
		lxf = 100
		lxf1 = 200
		return lxf #,lxf1

class Lxf2(object):
	def __init__(self):
		self.lxf1 = Lxf1()

	def print_anying(self):
		print self.lxf1.lxf1_print()		# print Lxf1对象 lxf1_print函数的 lxf和lxf1
		print self.lxf1.session				# print Lxf1对象 session

		a = self.lxf1.lxf1_print()
		b = a+1000
		print b

lxf = Lxf2()
lxf.print_anying()