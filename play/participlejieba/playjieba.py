#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#coding=utf-8
#Create by shengjk1 on  2017/6/9 0009

import jieba
# python分词
# jieba.cut的默认参数只有三个,jieba源码如下
# cut(self, sentence, cut_all=False, HMM=True)
# 分别为:输入文本 是否为全模式分词 与是否开启HMM进行中文分词
from jieba import analyse

set_list = jieba.cut("我在北京大学学习北京大学的文学", cut_all=True, HMM=False)
print ("Full Mode " + "/".join(set_list))
set_list = jieba.cut("我在北京大学学习北京大学的文学", cut_all=False, HMM=False)
print ("not Full Mode " + "/".join(set_list))
set_list = jieba.cut("我在北京大学学习北京大学的文学",  HMM=False)
print ("" + "/".join(set_list))

set_list=jieba.cut_for_search("我在北京大学学习北京大学的文学",HMM=False)#搜索引擎的模式
print ("/".join(set_list))


#关键词提取
text_path="D:\\tmp\\1111.txt"
text=open(text_path).read()
for key in analyse.extract_tags(text,10,withWeight=False):
	print (key.encode("utf-8"))