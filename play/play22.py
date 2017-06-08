#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#coding=utf-8
#Create by shengjk1 on  2017/6/8 0008

#!/usr/bin/env python
#-*- coding: utf-8 -*-
#通过urllib(2)模块下载网络内容
import urllib,urllib2,gevent
#引入正则表达式模块，时间模块
import re,time

import requests
from bs4 import BeautifulSoup
from gevent import monkey

monkey.patch_all()

def geturllist(url):
	url_list=[]
	print url
	s = urllib2.urlopen(url)
	text = s.read()
	#正则匹配，匹配其中的图片
	html = re.search(r'<ol.*</ol>', text, re.S)
	urls = re.finditer(r'<p><img src="(...)jpg" /></p>',html.group(),re.I)
	for i in urls:
		url=i.group(1).strip()+str("jpg")
		url_list.append(url)
	return url_list

def download(down_url):
	name=str(time.time())[:-3]+"_"+re.sub('.+?/','',down_url)
	print name
	urllib.urlretrieve(down_url, "D:\\tmp\\"+name)

def getpageurl():
	page_list = []
	#进行列表页循环
	for page in range(1,700):
		url="http://jandan.net/ooxx/page-"+str(page)+"#comments"
		#把生成的url加入到page_list中
		page_list.append(url)
	print page_list
	return page_list
if __name__ == '__main__':
	jobs = []
	# pageurl = getpageurl()[::-1]
	# 进行图片下载
	# for i in pageurl:
	# 	for downurl in geturllist(i):
	# 		jobs.append(gevent.spawn(download(downurl)))
	#
	# gevent.joinall(jobs)
	import  requests
	r=requests.get('http://jandan.net/ooxx');
	soup=BeautifulSoup(r.content,'html.parser')
	for i in soup.find_all(class_="view_img_link"):
		print i['href'].encode("utf-8")
		r=requests.get('http:'+i['href'].encode("utf-8"))
		picName="D:\\tmp\\"+str(time.time())+".jpg"
		with open(picName,"wb") as f:
			f.write(r.content)

