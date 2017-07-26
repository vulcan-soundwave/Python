#!/usr/bin/env python
# -*- codingL: utf-8 -*-

import math

def fun(a, b, c):
	if not isinstance(a, (int, float)):
		raise TypeError('bad operand type')
	if not isinstance(b, (int, float)):
		raise TypeError('bad operand type')	
	if not isinstance(c, (int, float)):
		raise TypeError('bad operand type')
	temp = b*b - 4*a*c
	if a == 0:
		return '不是一元二次方程'
	if temp < 0:
		return '无解'
	elif temp == 0:
		x1 = -b / 2*a
		return x1, x1
	else:
		temp = math.sqrt(b*b - 4*a*c)
		x1 = (-b + temp) / (2*a)
		x2 = (-b - temp) / (2*a)
		return x1, x2

a = float(input('Please input a:'))
b = float(input('Please input b:'))
c = float(input('Please input c:'))

print(fun(a, b, c))
