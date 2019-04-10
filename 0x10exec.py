#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/4/6 9:20
# @Author : liaochao
# @File   : exec.py

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
