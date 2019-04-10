#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/4/7 11:35
# @Author : liaochao
# @File   : format.py

print("{} {}".format("hello","world"))
print("{0} {1}".format("hello","world"))
print("{1} {0}".format("hello","world"))
print ("网站名：{name},地址{url}".format(name="百度",url="www.baidu.com"))
# 通过字典设置参数
site = {"name":"百度","url":"www.baidu.com"}
print("网站名：{name}，地址:{url}".format(**site))
#通过列表索引设置参数
my_list=["name","www.baidu.com"]
print("网站名：{0[0]},地址：{0[1]}".format(my_list))