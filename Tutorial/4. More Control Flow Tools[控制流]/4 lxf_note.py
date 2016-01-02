#-*- coding: utf-8 -*-

# 4. More Control Flow Tools

'''
# ================================================================
4.1 if声明
	if声明可能是最众所周知的一种声明，以下是例子

x = int(raw_input("Please enter an int:"))
if x < 0:
	x = 0
	print u'Negative changed to zero'
elif x == 0:
	print 'Zero'
elif x == 1:
	print 'Single'
else:
	print 'More'


elif可以没有，也可以有多个，
else 是可选的
elif比else if要短，并且他很使用，因为可以避免过多嵌套
if...elif...elif 序列是替代其他语言里的switch或case声明


#===========================================================
4.2 for声明
	python中的for声明不同于C或Pascal中的；


words = ['cat','window','defenestrate']
for w in words:
	print w,len(w)


words = ['cat','window','defenestrate']
for w in words[:]:
	if len(w)>6:
		words.insert(0,w)	# 0是插入到第1个位置
print words



# 4.3 The range() Function
print range(10)				#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print range(5,10)			#[5, 6, 7, 8, 9]
print range(0,10,3)			#[0, 3, 6, 9]
print range(-10,-100,-30) 	#[-10, -40, -70]


a = ['Mary','had','a','little','lamb']
for i in range(len(a)):
	print i,a[i]


# ================================================================
# 4.4 break and continue Statements, and else Clauses on Loops
# break 如同C中，跳出 for 或者 while 循环
for n in range(2,10):
	for x in range(2,n):
		if n % x == 0:
			print n,'equals',x,'*',n/x
			break
	else:
		print n,'is a prime number' #一个素数



for num in range(2,10):
	if num%2 ==0:
		print 'Found an even number',num 	#偶数
		continue
	print "Found a number",num



# ================================================================
# 4.5 pass Statements
# pass 是什么都不操作；
while True:
	pass	# Busy-wait for keyboard interrupt (Ctrl+C)

class lxfclass:
	pass

def initlog(*args):
	pass    # Remember to implement this!
'''

# ================================================================
# 4.6 Defining Functions




