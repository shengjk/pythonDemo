#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#coding=utf-8
#Create by shengjk1 on  2016/12/29
import random
import time
import sys

if __name__ == '__main__':



    f=open("F:\\riotest.txt","w")
    sys.stdout=f
    for i in range(1,101):
        tlogType ="ptfw","fx","fxfw"
        logType=tlogType[random.randint(0,2)]
        ecode="test01"
        ename="test01Name"
        userid=str(random.randint(0,10000))
        produceid=str(random.randint(0,10000))
        activityid=str(random.randint(0,10000))
        shareid=str(random.randint(0,10000))
        pagecode=str(random.randint(0,10000))
        pagename="pageName"+str(random.randint(0,10000))
        time1=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        openid=""
        tyopid=""
        ip=""
        print(logType+"|"+"02-42-AC-11-00-09"+"|"+str(int(time.time())*1000)+"|"+"i"+"|"+ecode+"|"+ename+"|"+userid+"|"
              +produceid+"|"+activityid+"|"+shareid+"|"+pagecode+"|"+pagename+"|"+time1+"|"+openid+"|"
              +tyopid+"|"+ip)
    f.close()






