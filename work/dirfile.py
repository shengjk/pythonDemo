#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create by shengjk1 on  2017/6/16 0016
# ============================================================
#
#    DESCRIPTION: 
#   REQUIREMENTS:
#        COMPANY: syph  
#
# ============================================================
import os
import sys


def juge_status(status,f):
    if status==status:
        print f+ "sucees"
    else:
        print f +"失败"




stdo=sys.stdout
# need a file handle with write mode
fhandle=open("out.txt",'w');
sys.stdout=fhandle

root_dir="/home/cdh/20170717/"
for f in os.listdir(root_dir):
     status=os.system("impala-shell -f "+root_dir+f)
     juge_status(status,f)

kylinCubeName=['WeiTuoZhiJieAnZhuangTai','huikuan','KeHuShuLiangStatus','KeHuShuLiangZhiYouXinQianYue','weituo','WeiTuoZhiFenGongSi','CuiShouAnJianLiang','jiekuanrenshu']

for cubname in kylinCubeName:
     status1=os.system("java -jar connkylin-yn.jar "+cubname)
     if status1==0:
        print cubname + " cube  sucees"
     else:
        print cubname  +" cube  失败"

sys.stdout=stdo







