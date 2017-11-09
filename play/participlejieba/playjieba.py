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

stopwords = {}
stopwords_path = 'stopwords.txt'  # 停用词词表
my_words_list = ['想做','干啥']  # 在结巴的词库中添加新词

def add_word(list):
	for items in list:
		jieba.add_word(items)

def jiebaclearText(text):
	mywordlist = []
	seg_list = jieba.cut(text, cut_all=False)
	liststr = "/ ".join(seg_list)
	# print liststr
	f_stop = open(stopwords_path)
	try:
		f_stop_text = f_stop.read()
		f_stop_text = unicode(f_stop_text, 'utf-8')
	# print "f_stop_text "+f_stop_text
	finally:
		f_stop.close()
	f_stop_seg_list = f_stop_text.split('\n')
	for myword in liststr.split('/'):
		if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
			mywordlist.append(myword)
	return ''.join(mywordlist)




#关键词提取
text_path="D:\\tmp\\1111.txt"
text=open(text_path).read()
add_word(my_words_list)
text=jiebaclearText(text)
# for key in analyse.extract_tags(text,10,withWeight=True):
# 	print key[0].encode('UTF-8')+" ========== "+str(key[1])

for key,weight in analyse.extract_tags(text,10,withWeight=True):
	print  key,weight