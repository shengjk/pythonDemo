#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#coding=utf-8
#Create by shengjk1 on  2017/6/6 0006

from bs4 import BeautifulSoup
'''
构建一个 BeautifulSoup 对象需要两个参数，第一个参数是将要解析的 HTML 文本字符串，第二个参数告诉 BeautifulSoup 使用哪个解析器来解析 HTML。
解析器负责把 HTML 解析成相关的对象，而 BeautifulSoup 负责操作数据（增删改查）。”html.parser” 是Python内置的解析器，”lxml” 则是一个基于c语言开发的解析器，它的执行速度更快，不过它需要额外安装
'''
'''
BeatifulSoup 将 HTML 抽象成为 4 类主要的数据类型，分别是Tag , NavigableString , BeautifulSoup，Comment 。每个标签节点就是一个Tag对象，NavigableString 对象一般是包裹在Tag对象中的字符串，BeautifulSoup 对象代表整个 HTML 文档。例如：

>>> type(soup)
<class 'bs4.BeautifulSoup'>
>>> type(soup.h1)
<class 'bs4.element.Tag'>
>>> type(soup.p.string)
<class 'bs4.element.NavigableString'>
'''

text = """
<html>  
    <head>
     <title >hello, world</title>
    </head>
    <body>
        <h1>BeautifulSoup</h1>
        <p class="bold">如何使用BeautifulSoup</p>
        <p class="big" id="key1"> 第二个p标签</p>
        <a href="http://foofish.net">python</a>
    </body>
</html>  
"""
soup=BeautifulSoup(text,'html.parser')
print soup.title
print soup.body
print '=============\n'
print soup.p.string
'''
每一个tag都有一个name
'''
print soup.h1.name