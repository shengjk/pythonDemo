#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create by shengjk1 on  2017/12/27
'''
整理中文名字的pdf
'''

import os
import shutil
import re

rootDir = "/Users/iss/Downloads"
dst = "/Users/iss/Desktop"

filterDir = ["/Users/iss/Desktop/book", "/Users/iss/Library","/usr","/Library","/System/Library","/Users/iss/anaconda","/Users/iss/anaconda2","/Users/iss/.m2" ,
             "/Volumes/system","/Volumes/system/Users/iss/Library","/Users/iss/.gradle","/Users/iss/Downloads/NavicatPremium15",
             "/Users/iss/sourceCode","/Users/iss/usersoft","/Applications","/Users/iss/Downloads/textmaterc7","/Users/iss/Downloads/NavicatPremium15",
             "/Users/iss/Downloads/iChm.1.4.3","/Users/iss/Downloads/Postman.app","/Users/iss/Downloads/MacDown.app","/Users/iss/Downloads/CrossOver_wm.app",dst]
# filterDir=[]
zhPattern = re.compile(u'[\u4e00-\u9fa5]+')


def listdir(rootDir):
	for i in os.listdir(rootDir):
		childDir = os.path.join(rootDir, i)
		if os.path.isdir(childDir) and (os.path.isdir(childDir) not in filterDir and os.path.dirname(childDir) not in filterDir):
			listdir(childDir)
		elif (os.path.dirname(childDir) not in filterDir and childDir.endswith('.pdf') and zhPattern.search(childDir)):
			shutil.move(childDir, dst)
			print(childDir, "copy over")
		else:
			print(childDir)

if __name__ == '__main__':
	listdir(rootDir)
