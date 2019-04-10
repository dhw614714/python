#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/4/5 22:21
# @Author : liaochao
# @File   : classmethod.py
class test_classmethod(object):
    @classmethod
    def printed(self,a,b):
        c = a + b
        print(c)
if __name__ == '__main__':
    test_classmethod.printed(3,5)
# class test_classmethod(object):
    def printed(self,a,b):
        c = a + b
        print(c)
if __name__ == '__main__':
    c = test_classmethod()
    c.printed(3,5)


