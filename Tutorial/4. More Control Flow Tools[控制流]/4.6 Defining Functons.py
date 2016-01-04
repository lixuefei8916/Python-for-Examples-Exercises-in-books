#-*- coding: utf-8 -*-

# ================================================================
# 4.6 Defining Functions
# 创建一个函数 来实现斐波那契序列
'''
def fib(n):
	a,b = 0,1
	while a < n:
		print a,
		a,b, = b, a+b
fib(2000)

>>> fib
<function fib at 10042ed0>

>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89

>>> fib(0)
>>> print fib(0)
None
'''
# ===========================================
# return 一个列表，可以取代print
def fib2(n):
	result = []
	a,b = 0,1
	while a<n:
		result.append(a)
		a,b = b,a+b
	return result
lxf = fib2(100)
print lxf



