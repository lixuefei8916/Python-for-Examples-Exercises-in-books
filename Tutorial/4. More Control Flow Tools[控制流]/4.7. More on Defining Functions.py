#-*- coding: utf-8 -*-

# 默认参数
# 4.7.1. Default Argument Values

def ask_ok(prompt,retries=4,complaint='Yes or on,please!'):
	while True:
		ok = raw_input(prompt)
		if ok in ('y','ye','yes'):
			return True
		if ok in ('n','no','nop','nope'):
			return False
		retries = retries - 1
		if retries < 0:
			raise IOError('refusenik user')
		print complaint


#ask_ok('Do you really want to quit?')		#询问3次 报错并结束
#ask_ok('OK to overwrite the file?', 2)		#询问1次 结束
#ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# ================================================================

i = 5
def f(arg=i):
	print arg
i = 6
#f()

# ================================================================

def f(a,L=[]):
	L.append(a)
	return L
'''
print f('a')
print f('b')
print f(3)

[1]
[1, 2]
[1, 2, 3]
'''

# ================================================================

def f(a,L=None):
	if L is None:
		L = []
	L.append(a)
	return L
'''
print f('a')
print f('b')
print f(1)
['a']
['b']
[1]

'''

# ================================================================
# 4.7.2 keyword Arguments 关键字参数
# ================================================================
def parrot(voltage,state='a stiff', action='voom',type='Norwegian Blue'):
	print "-- this parrot wouldn't", action,
	print "if you put", voltage, "volts through it."
	print "-- Lovely plumage, the", type
	print "-- It's",state, "!"

#parrot(1000)				# voltage=1000,其他仍用默认参数值
#parrot(voltage=1000)		# [同上]voltage=1000,其他仍用默认参数值
#parrot(voltage=1000000, action='VOOOOOM')  #当action='VOOOOOM'后，默认值的voom'将被覆盖
#parrot(action='VOOOOOM', voltage=1000000)   # 颠倒顺序，但必须有参数名
#parrot('a million', 'bereft of life', 'jump') # voltage='a million' ， state='bereft of life' ， action='jump'
#parrot('a thousand', state='pushing up the daisies') # voltage='a thousand' ，state='pushing up the daisies'

#但下面这样是错误的
#parrot()    						#缺少1个参数
#parrot(voltage=1000,'lxf')			#因为缺省参数voltage有值了，没有被省略的参数了，所以'lxf'找不到可被赋值的参数
#parrot(110, voltage=220)			#voltage被赋予2次值 
#parrot(actor='John Cleese')			# 错误的参数

# --------------------------------------------------------------

def cheeseshop(kind,*arguments,**keywords):
	print "-- Do you have any",kind,"?"
	print "-- I'm sorry, we're all out of", kind
	print arguments
	#for arg in arguments:
	#	print arg
	print "-" * 10
	print keywords
	#keys = sorted(keywords.keys())
	#for kw in keys:
	#	print kw,":",keywords[kw]

#cheeseshop("Limburger")
#cheeseshop("Limburger","It's very runny,sir.")
#cheeseshop("Limburger","It's very runny,sir.","It's really very, VERY runny, sir.")
#cheeseshop("Limburger","It's very runny,sir.","It's really very, VERY runny, sir.",shopkeeper='Michael Palin',client="John Cleese",sketch="Cheese Shop Sketch")
# 形参 kind = Limburger
# 形参*arguments（可存储元组）= "It's very runny,sir.","It's really very, VERY runny, sir."
# 形参**keywords（可存储字典）= 'Michael Palin',client="John Cleese",sketch="Cheese Shop Sketch"

# ================================================================
# 4.7.3 Arbitrary Arguments Lists
# ================================================================
def write_multiple_items(file,separator,*args):
	file.write(separator.join(args))


# ================================================================
# 4.7.4 Unpacking Arguments Lists 
# ================================================================
#range(3,6)

args = [3,6]
range(*args)

def parrot(voltage,state='a stiff',action='voom'):
	print "-- This parrot wouldn't",action,
	print "if you put",voltage,"volts through it.",
	print "E's",state,"!"
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
#parrot(**d)


# ================================================================
# 4.7.5 Lambda Expressions 
# ================================================================

def make_incrementor(n):
	return lambda x:x + n

>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43

>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]






>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it doesn't do anything.
...     """
...     pass
...
>>> print my_function.__doc__
Do nothing, but document it.





