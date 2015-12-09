#-*- coding: utf-8 -*-
'''
class Myclass(object):
	def __init__(self):
		pass
	def sum(self,x,y):
		return x+y
	def sub(self,x,y):
		return x-y
# ================================
# from Python之自动单元测试之一（unittest使用实例）
'''
class Widget():
	def __init__(self,size=(40,40)):
		self._size = size
	def getSize(self):
		return self._size
	def resize(self,width,height):
		if width < 0 or height < 0:
			raise ValueError,'illegal size'
		self._size = (width,height)



