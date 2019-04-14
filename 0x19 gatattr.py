#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/4/14 20:00
# @Author : liaochao
# @File   : 0x19 gatattr.py
class test():
    name = "fanfan"
    def run(self):
        return "hello world"
t = test()
print(getattr(t,"name")) #获取name属性，存在就打印出来；
print(getattr(t,"run"))  #获取run方法，存在就打印出方法的内存地址；
print(getattr(t,"run")())  #获取run方法，后面加括号可以将这个方法运行；
print(getattr(t,"age","18"))  #若属性不存在，返回一个默认值；
print(getattr(t,"age"))  #获取一个不存在的属性；
