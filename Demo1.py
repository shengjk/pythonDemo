#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#Create by shengjk1 on  2017/11/5
import sys

import time
import os
import logging

reload(sys)
sys.setdefaultencoding('utf-8')

class Student():
	Tab="aaaaa"
	def __init__(self,name,score):
		self._name=name
		self._score=score
		self.list=['a','v','c']


	def get_list(self):
		return self.list

	def print_score(self):
		print('%s : %s ' % (self._name,self._score))



b=Student('aaaa',334)
b.get_list()
print b.Tab
print Student.Tab

