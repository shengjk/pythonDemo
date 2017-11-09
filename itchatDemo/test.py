#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#Create by shengjk1 on  2017/11/9
import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
	print msg['Text']

itchat.auto_login(hotReload=True)
itchat.send(u'测试消息','filehelper')
# itchat.run()