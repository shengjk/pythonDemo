#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
# Create by shengjk1 on  2017/6/8 0008

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 通过urllib(2)模块下载网络内容
import urllib, urllib2, gevent
# 引入正则表达式模块，时间模块
import re, time

import requests
from bs4 import BeautifulSoup


def jandanpicture():
	for page in range(1, 200):
		url = "http://jandan.net/ooxx/page-" + str(page) + "#comments"
		print url;
		r = requests.get(url);
		soup = BeautifulSoup(r.content, 'html.parser')
		for i in soup.find_all(class_="view_img_link"):
			print i['href']
			r = requests.get('http:' + i['href'])
			picName = "D:\\tmp\\" + str(time.time()) + "." + i['href'][-3:]
			with open(picName, 'wb') as f:
				f.write(r.content)


def jandanduanzi():
	for page in range(1, 3000):
		# http://jandan.net/duan/page-2244#comments
		url = "http://jandan.net/duan/page-" + str(page) + "#comments"
		print url;
		r = requests.get(url);
		soup = BeautifulSoup(r.content, 'html.parser')
		fileName = ('D:\\tmp\\煎蛋段子.txt').decode('UTF-8')
		file = open(fileName, 'a')
		for div in soup.find_all('div', class_='text'):
			str1 = div.p.get_text().encode('UTF-8')
			file.write(str1)
			file.write('\n======================="\n"')
	file.close()


if __name__ == '__main__':
	jobs = []

	# pageurl = getpageurl()[::-1]
	# 进行图片下载
	# for i in pageurl:
	# 	for downurl in geturllist(i):
	# 		jobs.append(gevent.spawn(download(downurl)))
	#
	# gevent.joinall(jobs)


	fileName = ('D:\\tmp\\煎蛋段子.txt').decode('UTF-8')
	file = open(fileName, 'a')
	for page in range(1, 3000):
		# http://jandan.net/duan/page-2244#comments
		url = "http://jandan.net/duan/page-" + str(page) + "#comments"
		print url;
		r = requests.get(url);
		soup = BeautifulSoup(r.content, 'html.parser')
		for div in soup.find_all('div', class_='text'):
			str1 = div.p.get_text().encode('UTF-8')
			file.write(str1)
			file.write('\n======================="\n"')
	file.close()
