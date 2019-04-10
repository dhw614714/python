#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/4/7 16:39
# @Author : liaochao
# @File   : 0x12isinstance.py
a = 2
print(isinstance(a,int))
print(isinstance(a,str))
print(isinstance(a,(str,int,list)))   #是元组中的一个返回True
