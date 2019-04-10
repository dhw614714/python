#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/4/7 14:50
# @Author : liaochao
# @File   : 0x11hasattr.py

class Coordinate:
    x = 10
    y = -5
    z = 0
point = Coordinate()
print(hasattr(point,'x'))
print(hasattr(point,'y'))
print(hasattr(point,'z'))
print(hasattr(point,'f'))