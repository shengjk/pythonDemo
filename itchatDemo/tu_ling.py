#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#Create by shengjk1 on  2017/11/11
import requests
import json



apiUrl='http://www.tuling123.com/openapi/api'
data = {
	'key'    : '8edce3ce905a4c1dbb965e6b35c3834d', # 如果这个Tuling Key不能用，那就换一个
	'info'   : '我爱你一辈子', # 这是我们发出去的消息
	'userid' : 'wechat-robot', # 这里你想改什么都可以
}
r = requests.post(apiUrl, data=data).json()

# 让我们打印一下返回的值，看一下我们拿到了什么
print r['text']
# r=json.dumps(r, encoding="UTF-8", ensure_ascii=False)
# print(r)
