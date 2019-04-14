#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/4/14 20:22
# @Author : liaochao
# @File   : 0x20 setattr.py
#  给对象的属性赋值，若属性不存在，先创建在赋值
class test():
    name = "fanfan"
    def run(self):
        return "hello world"
t = test()
print(hasattr(t,"age")) #用于判断对象是否包含对应的属性；
print(setattr(t,"age","18"))  #为属性赋值，并没有返回值；
print(hasattr(t,"age"))  #属性存在了