#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#coding=utf-8
#Create by shengjk1 on  2017/6/6 0006
import re

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
        <p class="bold">如何使用BeautifulSouphajhfjd</p>
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
#标签的属性
print soup.p['class']
#获取标签的内容
print soup.h1.string

'''
如何从 HTML 中找到我们关心的数据？BeautifulSoup 提供了两种方式，一种是遍历，另一种是搜索，通常两者结合来完成查找任务。

遍历文档树

遍历文档树，顾名思义，就是是从根节点 html 标签开始遍历，直到找到目标元素为止，遍历的一个缺陷是，如果你要找的内容在文档的末尾，那么它要遍历整个文档才能找到它，速度上就慢了。因此还需要配合第二种方法。

通过遍历文档树的方式获取标签节点可以直接通过 .标签名的方式获取，例如：

获取 body 标签：

>>> soup.body
<body>\n<h1>BeautifulSoup</h1>\n<p class="bold">\u5982\u4f55\u4f7f\u7528BeautifulSoup</p>\n</body>
获取 p 标签

>>> soup.body.p
<p class="bold">\u5982\u4f55\u4f7f\u7528BeautifulSoup</p>
获取 p 标签的内容

>>> soup.body.p.string
\u5982\u4f55\u4f7f\u7528BeautifulSoup
前面说了，内容也是一个节点，这里就可以用 .string 的方式得到。遍历文档树的另一个缺点是只能获取到与之匹配的第一个子节点，例如，如果有两个相邻的 p 标签时，第二个标签就没法通过 .p 的方式获取，这是需要借用 next_sibling 属性获取相邻且在后面的节点。此外，还有很多不怎么常用的属性，比如：.contents 获取所有子节点，.parent 获取父节点，更多的参考请查看官方文档。


搜索文档树

搜索文档树是通过指定标签名来搜索元素，另外还可以通过指定标签的属性值来精确定位某个节点元素，最常用的两个方法就是 find 和 find_all。这两个方法在 BeatifulSoup 和 Tag 对象上都可以被调用。

find_all()

find_all( name , attrs , recursive , text , **kwargs )
find_all 的返回值是一个 Tag 组成的列表，方法调用非常灵活，所有的参数都是可选的。

第一个参数 name 是标签节点的名字。

# 找到所有标签名为title的节点
>>> soup.find_all("title")
[<title>hello, world</title>]
>>> soup.find_all("p")
[<p class="bold">\xc8\xe7\xba\xce\xca\xb9\xd3\xc3BeautifulSoup</p>, 
<p class="big"> \xb5\xda\xb6\xfe\xb8\xf6p\xb1\xea\xc7\xa9</p>]
第二个参数是标签的class属性值

# 找到所有class属性为big的p标签
>>> soup.find_all("p", "big")
[<p class="big"> \xb5\xda\xb6\xfe\xb8\xf6p\xb1\xea\xc7\xa9</p>]
等效于

>>> soup.find_all("p", class_="big")
[<p class="big"> \xb5\xda\xb6\xfe\xb8\xf6p\xb1\xea\xc7\xa9</p>]
因为 class 是 Python 关键字，所以这里指定为 class_。

kwargs 是标签的属性名值对，例如：查找有href属性值为 "http://foofish.net" 的标签

>>> soup.find_all(href="http://foofish.net")
[<a href="http://foofish.net">python</a>]
当然，它还支持正则表达式

>>> import re
>>> soup.find_all(href=re.compile("^http"))
[<a href="http://foofish.net">python</a>]
属性除了可以是具体的值、正则表达式之外，它还可以是一个布尔值（True/Flase），表示有属性或者没有该属性。

>>> soup.find_all(id="key1")
[<p class="big" id="key1"> \xb5\xda\xb6\xfe\xb8\xf6p\xb1\xea\xc7\xa9</p>]
>>> soup.find_all(id=True)
[<p class="big" id="key1"> \xb5\xda\xb6\xfe\xb8\xf6p\xb1\xea\xc7\xa9</p>]
遍历和搜索相结合查找，先定位到 body 标签，缩小搜索范围，再从 body 中找 a 标签。

>>> body_tag = soup.body
>>> body_tag.find_all("a")
[<a href="http://foofish.net">python</a>]
find()

find 方法跟 find_all 类似，唯一不同的地方是，它返回的单个 Tag 对象而非列表，如果没找到匹配的节点则返回 None。如果匹配多个 Tag，只返回第0个。

>>> body_tag.find("a")
<a href="http://foofish.net">python</a>
>>> body_tag.find("p")
<p class="bold">\xc8\xe7\xba\xce\xca\xb9\xd3\xc3BeautifulSoup</p>
get_text()

获取标签里面内容，除了可以使用 .string 之外，还可以使用 get_text 方法，不同的地方在于前者返回的一个 NavigableString 对象，后者返回的是 unicode 类型的字符串。

>>> p1 = body_tag.find('p').get_text()
>>> type(p1)
<type 'unicode'>
>>> p1
u'\xc8\xe7\xba\xce\xca\xb9\xd3\xc3BeautifulSoup'

>>> p2 = body_tag.find("p").string
>>> type(p2)
<class 'bs4.element.NavigableString'>
>>> p2
u'\xc8\xe7\xba\xce\xca\xb9\xd3\xc3BeautifulSoup'
>>>
实际场景中我们一般使用 get_text 方法获取标签中的内容。

总结

BeatifulSoup 是一个用于操作 HTML 文档的 Python 库，初始化 BeatifulSoup 时，需要指定 HTML 文档字符串和具体的解析器。BeatifulSoup 有3类常用的数据类型，分别是 Tag、NavigableString、和 BeautifulSoup。查找 HTML元素有两种方式，分别是遍历文档树和搜索文档树，通常快速获取数据需要二者结合

'''


# print soup.body.p
# print '=============================='
# print soup.find('title')
# print soup.find_all('p','big')
# print soup.find_all(href=re.compile('^http'))