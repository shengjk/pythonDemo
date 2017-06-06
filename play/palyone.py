#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
# Create by shengjk1 on  2017/6/6 0006

import urllib
import urllib2

'''
http://aljun.me/post/17
https://foofish.net/http-requests.html
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
r=requests.get("https://foofish.net")
print r.headers
#响应头
for name,value in r.headers.items():
	print ("%s:%s" % (name,value))
'''
>>> r = requests.post('http://httpbin.org/post', data = {'key':'value'})
>>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})
>>> r = requests.delete('http://httpbin.org/delete')
>>> r = requests.head('http://httpbin.org/get')
>>> r = requests.options('http://httpbin.org/get')
'''
#查询参数
args={"p":4,'s':20}
r=requests.get("http://fav.foofish.net", params = args)
print r.url #http://fav.foofish.net/?p=4&s=20

#请求头
'''
requests 可以很简单地指定请求首部字段 Headers，比如有时要指定 User-Agent 伪装成浏览器发送请求，以此来蒙骗服务器。直接传递一个字典对象给参数 headers 即可。
'''
r = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})

'''
请求体
requests 可以非常灵活地构建 POST 请求需要的数据，如果服务器要求发送的数据是表单数据，则可以指定关键字参数 data，如果要求传递 json 格式字符串参数，则可以使用json关键字参数，参数的值都可以字典的形式传过去。
作为表单数据传输给服务器
'''
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print r.content

import json
url = 'http://httpbin.org/post'
payload = {'some': 'data'}
r = requests.post(url, json=payload)
print r.content

#响应的内容
'''
HTTP返回的响应消息中很重要的一部分内容是响应体，响应体在 requests 中处理非常灵活，
与响应体相关的属性有：content、text、json()。
content 是 byte 类型，适合直接将内容保存到文件系统或者传输到网络中
'''
r=requests.get("https://pic1.zhimg.com/v2-2e92ebadb4a967829dcd7d05908ccab0_b.jpg")
type(r.content)
with open("test.jpg","wb") as f:
	f.write(r.content)

'''
text 是 str 类型，比如一个普通的 HTML 页面，需要对文本进一步分析时，使用 text。
'''
import re
r=requests.get("https://foofish.net/understand-http.html")
print  type(r.content)
print re.compile("xxx").findall(r.text)

'''
如果使用第三方开放平台或者API接口爬取数据时，返回的内容是json格式的数据时，那么可以直接使用json()方法返回一个经过json.loads()处理后的对象。
'''
r=requests.get('https://www.v2ex.com/api/topics/hot.json')
print  r.json()

'''
代理设置

当爬虫频繁地对服务器进行抓取内容时，很容易被服务器屏蔽掉，因此要想继续顺利的进行爬取数据，使用代理是明智的选择。如果你想爬取墙外的数据，同样设置代理可以解决问题，requests 完美支持代理。这里我用的是本地 ShadowSocks 的代理，（socks协议的代理要这样安装 pip install requests[socks]）

import requests

proxies = {
  'http': 'socks5://127.0.0.1:1080',
  'https': 'socks5://127.0.0.1:1080',
}

requests.get('https://foofish.net', proxies=proxies, timeout=5)
超时设置

requests 发送请求时，默认请求下线程一直阻塞，直到有响应返回才处理后面的逻辑。如果遇到服务器没有响应的情况时，问题就变得很严重了，它将导致整个应用程序一直处于阻塞状态而没法处理其他请求。

>>> import requests
>>> r = requests.get("http://www.google.coma")
...一直阻塞中
正确的方式的是给每个请求显示地指定一个超时时间。

>>> r = requests.get("http://www.google.coma", timeout=5)
5秒后报错
Traceback (most recent call last):
socket.timeout: timed out


Session

在爬虫入门系列（一）：快速理解HTTP协议中介绍过HTTP协议是一中无状态的协议，为了维持客户端与服务器之间的通信状态，使用 Cookie 技术使之保持双方的通信状态。

有些网页是需要登录才能进行爬虫操作的，而登录的原理就是浏览器首次通过用户名密码登录之后，服务器给客户端发送一个随机的Cookie，下次浏览器请求其它页面时，就把刚才的 cookie 随着请求一起发送给服务器，这样服务器就知道该用户已经是登录用户。

import requests
# 构建会话
session  = requests.Session()
#　登录url
session.post(login_url, data={username, password})
#　登录后才能访问的url
r = session.get(home_url)
session.close()
构建一个session会话之后，客户端第一次发起请求登录账户，服务器自动把cookie信息保存在session对象中，发起第二次请求时requests 自动把session中的cookie信息发送给服务器，使之保持通信状态。
'''
