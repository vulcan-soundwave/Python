#!/usr/bin/env python
# -*- coding: utf-8 -*-

#可以用for循环遍历可迭代(iterable)对象，那这种遍历就是迭代(Iteration)

# judge if can iterable --> 通过collections模块的Iterable类型判断

from collections import Iterable

if isinstance('abc', Iterable):
	print('str can.')
else:
	print('str can not.')

if isinstance([1,2,3], Iterable):
	print('list can.')
else:
	print('list can not.')

if isinstance((1,2,3), Iterable):
	print('tuple can.')
else:
	print('tuple can not.')

if isinstance({'a':1, 'b':2, 'c':3}, Iterable):
	print('dict can.')
else:
	print('dict can not.')

if isinstance(set([1,2,3]), Iterable):
	print('set can.')
else:
	print('set can not.')

if isinstance(123,Iterable):	#int can not
	print('integer can.')
else:
	print('integer can not.')

# 测试后，发现 str, list, tuple, dict, set 是可迭代对象，integer 不可迭代

# test iteration
d = {'a':1, 'b':2, 'c':3}

# dict 迭代 key
for key in d:
	print(key)

# dict 迭代 value
for value in d.values():
	print(value)

# dict 迭代 key, value
for key,value in d.items():
	print(key,value)
