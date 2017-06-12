#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#coding=utf-8
#Create by shengjk1 on  2017/6/8 0008
import requests
from bs4 import BeautifulSoup

headers = {
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}
payload={'word':'python 好玩的事情'}
r=requests.get('https://www.zhihu.com/topic/19552832#1488',headers=headers)
soup=BeautifulSoup(r.content,'html.parser')
print(soup)
print(soup.find_all("li"))