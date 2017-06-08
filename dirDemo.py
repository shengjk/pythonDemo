#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#coding=utf-8
#Create by shengjk1 on  2017/6/8 0008

import os
for filename in  os.listdir('E:\\'):
	print (filename.decode('gbk'))
	print os.path.splitext(filename)#分离文件名和扩展名

import locale
print locale.getdefaultlocale()[1]