#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/4/14 9:46
# @Author : liaochao
# @File   : 0x13iter.py
a = [122,221,222]
b = iter(a)
print(b.__next__())
print(b.__next__())
print(b.__next__())

