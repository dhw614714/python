#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/4/14 21:28
# @Author : liaochao
# @File   : 0x22 zip.py
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)
print(list(zipped))
print(list(zip(a,c))) #元素个数与最短的列表一致；
x,y=zip(*zip(a,b))  #与zip相反，zip(*)可理解为解压，返回二维矩阵式；
print(x,y)