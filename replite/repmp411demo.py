#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create by shengjk1 on  2017/11/25
''''
获取百思不得其姐的小视频
'''

import requests
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36'}

# url = 'http://upos-hz-mirrorks3.acgvideo.com/upgcxcode/38/58/26275838/26275838-1-16.mp4?um_deadline=1511594696&platform=html5&rate=65000&oi=3025706585&um_sign=a423bf1caa6d25b60bb3ca84b1b37c05&gen=playurl&os=ks3&hfb=M2Y2ZWYwZjM2YmRiYmY5MDljYTBiOWE2ZmEwYjJmYTM='
url = 'http://mvideo.spriteapp.cn/video/2017/1124/5a17f634c02ad_wpc.mp4'
r=requests.get(url,headers=headers,stream=True)
f = open("file.mp4", "wb")
for chunk in r.iter_content(chunk_size=512):
    if chunk:
        f.write(chunk)
# with open("code3.MP4", "wb") as code:
#     code.write(r.content)
