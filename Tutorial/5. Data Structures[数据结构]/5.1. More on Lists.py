#-*- coding: utf-8 -*-

# ========================================================
# 5.1 More on Lists 列表
# ========================================================
'''
list.append(X)		添加到末尾
list.extend(L)		所有元素，添加到另一个list末尾
list.insert(i,x)	在指定位置添加元素 a.insert(0,x)
list.remove(x)		删除 值=x 的元素
list.pop([i])		删除 第i个位置的元素
list.index(x)		返回 值=x 的索引位置
list.count(x)		统计 值=x 的出现次数
list.sort(cmp=None,key=None,reverse=False)  排序
list.reverse()		反转列表中的元素
'''

a = [66.25,333,333,1,1234.5]
#print a.count(333)			# 显示 值=333 的索引位置：2
#print a.count(66.25)		# 显示 值=333 的索引位置：1
#print a.count('x')			# 0

a.insert(2,1)				# 在2的位置，添加值=1 [66.25, 333, 1, 333, 1, 1234.5]
a.append(333)				# [66.25, 333, 1, 333, 1, 1234.5, 333]

#print a.index(333)			# 1

a.remove(333)				# [66.25, 1, 333, 1, 1234.5, 333]
a.reverse()					# 反转元素 [333, 1234.5, 1, 333, 1, 66.25]
a.sort()					# 排序 [1, 1, 66.25, 333, 333, 1234.5]

a.pop()						# [1, 1, 66.25, 333, 333]


# ========================================================
# 5.1.1. Using Lists as Stacks 用列表作为栈
# ========================================================

stack = [3,4,5]
stack.append(6)				#[3, 4, 5, 6]
stack.append(7)				#[3, 4, 5, 6, 7]
stack.pop()					# 删除 7
stack.pop()					# 删除 6


# ========================================================
# 5.1.2. Using Lists as Queues 用列表作为队列
# ========================================================
from collections import deque
queue = deque(['Eric','John','Michael'])
queue.append("Terry")
queue.append("Graham")		# deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])

#print queue.popleft()		# 删除 左边第1个：Eric
#print queue 				# deque(['John', 'Michael', 'Terry', 'Graham'])


# ========================================================
# 5.1.3. Functional Programming Tools  函数式编程工具
# ========================================================
def f(x): return x % 2 != 0 and x % 3 != 0
filter(f,range(2,25))		# [5, 7, 11, 13, 17, 19, 23]

def cube(x): return x*x*x
map(cube, range(1, 11))		# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]



>>> seq = range(8)
>>> def add(x, y): return x+y
...
>>> map(add, seq, seq)
[0, 2, 4, 6, 8, 10, 12, 14]




>>> def add(x,y): return x+y
...
>>> reduce(add, range(1, 11))
55


>>> def sum(seq):
...     def add(x,y): return x+y
...     return reduce(add, seq, 0)
...
>>> sum(range(1, 11))
55
>>> sum([])
0


# ========================================================
# 5.1.4. List Comprehensions  列表推导式
# ========================================================
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


squares = [x**2 for x in range(10)]


>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]


>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']


# -----------------------------

>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]


>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


>>> zip(*matrix)
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]


