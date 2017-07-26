#!/usr/bin/env python
# -*- coding: utf-8 -*-

height = float(input('Please input height: '))
weight = float(input('Please input weight: '))
bmi = weight / height**2
if bmi < 18.5:
	print('体重过轻','BMI: %.2f' % bmi)
elif bmi < 25:
	print('体重正常','BMI: %.2f' % bmi)
elif bmi < 28:
	print('体重过重','BMI: %.2f' % bmi)
elif bmi <= 32:
	print('肥胖','BMI: %.2f' % bmi)
else:
	print('严重肥胖','BMI: %.2f' % bmi)
