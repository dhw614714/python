#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/4/14 10:04
# @Author : liaochao
# @File   : 0x14locals.py
def runoob(arg):
    z = 1
    print (locals())
    print(globals()) # globals函数返回一个全局变量的字典，包括所有导入的变量。

if __name__ == '__main__':
     runoob(4)
