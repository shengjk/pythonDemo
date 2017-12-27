#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#Create by shengjk1 on  2017/11/25
from urllib import request

url='http://p.bokecc.com/playhtml.bo?vid=B26FE855C0F7AEA79C33DC5901307461&siteid=BBC7552FC4418E60&autoStart=true&playerid=18CA88D83340DAD2&playertype=1'
url1='http://www.chinahadoop.cn/course/1029/lesson/19486'

headers='Accept:application/json, text/javascript, */*; q=0.01',
'Accept-Encoding:gzip, deflate',
'Accept-Language:zh-CN,zh;q=0.9,en;q=0.8',
'Connection:keep-alive',
'Host:www.chinahadoop.cn',
'Referer:http://www.chinahadoop.cn/course/1029/learn',
'User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36',
'X-Requested-With:XMLHttpRequest'

cookie={'PHPSESSID':'soctsi5009secv41qcq6ctu4p5',
        'pgv_pvi':'1114586112' ,
        'pgv_si':'s2073257984',
        'nTalk_CACHE_DATA':'{uid:kf_9301_ISME9754_93417,tid:1511588344638944}',
        'NTKF_T2D_CLIENTID':'guest7A95C137-E475-E4CC-3CA2-F1AFB33E46A1',
        'Hm_lvt_42496acfe194e26aac402105799876ef':'1511588345',
        'Hm_lpvt_42496acfe194e26aac402105799876ef':'1511588576',
        'zg_did':'%7B%22did%22%3A%20%2215ff1afb2cb7ca-05c4209819dfa6-17386d57-fa000-15ff1afb2ccc6%22%7D',
        'zg_727f75a76e954bc385156eb7ff3fb110':'%7B%22sid%22%3A%201511590982082%2C%22updated%22%3A%201511592144905%2C%22info%22%3A%201511588344533%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.chinahadoop.cn%22%2C%22cuid%22%3A%20%2293417%22%7D'
}


request.Request(url1,headers=headers,method='GET')
request.urlretrieve(url,'./2.mp4')

