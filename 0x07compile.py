#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/4/5 22:37
# @Author : liaochao
# @File   : compile.py

x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""


def func():
    y = 20
    exec(expr)
    exec(expr, {'x': 1, 'y': 2})
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})


func()
