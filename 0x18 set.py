#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/4/14 12:21
# @Author : liaochao
# @File   : 0x18 set.py
x = set('runoob')
y = set('google')
print(x,y)  #重复的元素被删除
print(x & y)  #交集
print (x | y)  #并集
print(x - y) #差集