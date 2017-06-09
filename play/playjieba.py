#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#coding=utf-8
#Create by shengjk1 on  2017/6/9 0009

import jieba

# python分词
set_list = jieba.cut("我在北京大学学习北京大学的文学", cut_all=True, HMM=False)
print ("Full Mode " + "/".join(set_list))
set_list = jieba.cut("我在北京大学学习北京大学的文学", cut_all=False, HMM=False)
print ("Full Mode " + "/".join(set_list))