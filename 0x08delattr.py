#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/4/7 10:32
# @Author : liaochao
# @File   : delattr.py
class Coordinate:
    x = 10
    y = -5
    z = 0

point1 = Coordinate()

print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)

delattr(Coordinate,'z')

print('x = ',point1.x)
print('y = ',point1.y)
print('z = ', point1.z)
