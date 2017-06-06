#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
# Create by shengjk1 on  2017/6/6 0006

import urllib
import urllib2

'''
http://aljun.me/post/17
'''
if __name__ == '__main__':
	header = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Host": "aljun.me"
	}
	# request = urllib2.request("http://aljun.me/post/17", header=header)
	# response = urllib2.urlopen(request)
	# respone = urllib2.urlopen("http://aljun.me/post/17")
	# print response.read()

'''
下载图片
'''
import urllib2

response=urllib2.urlopen("http://zhaduixueshe.com/static/pic/discovery.png")

with open("xxx.png","wb") as f:
	f.write(response.read())


import urllib

path="xxx1.png"
url="http://zhaduixueshe.com/static/pic/discovery.png"

urllib.urlretrieve(url,path)

#request库
import requests
r=requests.get('https://api.github.com/events')
print r.json()

