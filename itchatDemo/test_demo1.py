#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#Create by shengjk1 on  2017/11/11
import requests
import itchat
import sys
reload(sys)
sys.setdefaultencoding('utf8')

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg):
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
		'key'    : KEY,
		'info'   : msg,
		'userid' : 'wechat-robot',
	}
	try:
		r = requests.post(apiUrl, data=data).json()
		return r.get('text')
	except:
		# 将会返回一个None
		return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
	defaultReply = u'[小省机器人]: I received: ' + msg['Text']
	reply = get_response(msg['Text'])
	# print msg.User['NickName']
	# print '消息来源于 省:'+msg.User['Province']
	# print msg.User['City']
	print '消息来源于 省:'+msg.User['Province']+" 城市:"+msg.User['City']+" 微信昵称："+msg.User['NickName']+" 备注:"+msg.User['RemarkName']
	return u'[小省机器人]:'+reply or defaultReply


def greet():
	itchat.send(u'早呀','filehelper')
	author = itchat.search_friends(remarkName=u'小省')[0]
	author.send(u'greeting, 小省!')



# @itchat.msg_register(itchat.content.TEXT)
# def bay():
# 	# itchat.send(u'晚安','filehelper')
# 	print 'bay'

# itchat.auto_login(hotReload=True,loginCallback=greet,exitCallback=bay)
itchat.auto_login(hotReload=True,loginCallback=greet)
# time.sleep(3)
# itchat.logout()
itchat.run()
