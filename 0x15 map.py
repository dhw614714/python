#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/4/14 10:29
# @Author : liaochao
# @File   : 0x15 map.py
def square(x):
    return x ** 2
print(list(map(square,[1,2,3,4,5])))#python 3.x中需要使用list(map())
print(list(map (lambda x: x ** 2,[1,2,3,4,5]))) #使用lamnda匿名函数
print(list(map(lambda x,y:x+y,[1,2,3,4,5],[6,7,8,9,10])))#将两个列表相同位置的数据进行相加；