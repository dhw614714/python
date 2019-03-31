#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/3/26 16:18
# @Author : dd
# @File   : 0x03any.py
print(any((1,2,3,4))) #元组tuple，元素都不为空或0；
print(any((0,1,2,3))) #元组tuple了，存在一个为0的元素；
print(any([0,2,3,4])) #列表list，存在一个为0的元素；
print(any(()))  #空元组；
print(any([]))  #空列表