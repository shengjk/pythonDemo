#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#coding=utf-8
#Create by shengjk1 on  2017/6/7
import requests
from bs4 import BeautifulSoup
import pdfkit



def parse_uerl_to_HTML(url):
	respone=requests.get(url)
	soup=BeautifulSoup(respone.content,'html.parser')
	body=soup.find_all(class_='x-wiki-content')
	body=soup.find_all(class_='x-wiki-content')[0]
	html=str(body)
	with open("a.html",'wb') as f:
		f.write(html)


def get_url_list():
	response=requests.get("http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000")
	soup=BeautifulSoup(response.content,'html.parser')
	menu_tag=soup.find_all(class_='uk-nav uk-nav-side')
	menu_tag=soup.find_all(class_='uk-nav uk-nav-side')[1]
	urls=[]
	for li in menu_tag.find_all('li'):
		url = "http://www.liaoxuefeng.com" + li.a.get('href')
		urls.append(url)

	return urls

def save_pdf(htmls,file_name):
	options={
		'page-size':'Letter',
		'encoding':'UTF-8',
		'custom-header':[('Accept-Encoding','gzip')]
	}
	pdfkit.from_file(htmls,file_name,options=options)

if __name__ == '__main__':
	parse_uerl_to_HTML('https://www.google.com.hk/search?q=Python+%E5%9B%BE%E7%89%87%E8%BD%AC%E5%AD%97%E7%AC%A6%E7%94%BB&oq=Python+%E5%9B%BE%E7%89%87%E8%BD%AC%E5%AD%97%E7%AC%A6%E7%94%BB&aqs=chrome..69i57j69i61&sourceid=chrome&ie=UTF-8')
	# print get_url_list()
	# save_pdf('a.html','aa')