#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#Create by shengjk1 on  2017/11/9
import itchat
'''
http://itchat.readthedocs.io/zh/latest/tutorial/tutorial0/
'''
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
	print msg['Text']

itchat.auto_login(hotReload=True)
itchat.send(u'测试消息','filehelper')
# itchat.send('我是微信机器人','小省')
# itchat.run()