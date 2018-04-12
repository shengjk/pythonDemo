#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#Create by shengjk1 on  2018/4/12


import os
import shutil
import re
import codecs
import subprocess
import threading

rootDir = "/Users/iss/Desktop"
# dst = "/Users/iss/Desktop/文档"
dst=""
filterDir = ["/Users/iss/Desktop/book", "/Users/iss/Library","/usr","/Library","/System/Library","/Users/iss/anaconda","/Users/iss/anaconda2","/Users/iss/.m2" ,
             "/Volumes/system","/Volumes/system/Users/iss/Library","/Users/iss/.gradle","/Users/iss/Downloads/NavicatPremium15",
             "/Users/iss/sourceCode","/Users/iss/usersoft","/Applications","/Users/iss/Downloads/textmaterc7","/Users/iss/Downloads/NavicatPremium15",
             "/Users/iss/Downloads/iChm.1.4.3","/Users/iss/Downloads/Postman.app","/Users/iss/Downloads/MacDown.app","/Users/iss/Downloads/CrossOver_wm.app",dst]
# filterDir=[]
zhPattern = re.compile(u'[\u4e00-\u9fa5]+')


def listdir(rootDir):
	f=codecs.open("/Users/iss/Desktop/1.md", 'a', encoding='utf-8')

	for i in os.listdir(rootDir):
		childDir = os.path.join(rootDir, i)
		if os.path.isdir(childDir) and (os.path.isdir(childDir) not in filterDir and os.path.dirname(childDir) not in filterDir):
			listdir(childDir)

		elif (os.path.dirname(childDir) not in filterDir and childDir.endswith('mhtml')):
			# shutil.move(childDir, dst)
			(filepath,filename)=os.path.split(childDir)
			(fileNamePrex,filenameSuf)=os.path.splitext(filename)
			print ("["+fileNamePrex+"]("+childDir+")",end='\n\n',file=f,flush=True)

			print(childDir, "copy over")
		else:
			pass
			# print(childDir)

		f.close

if __name__ == '__main__':
	listdir(rootDir)
	# subprocess.call("open /Users/iss/Desktop/1.md ",shell=True)
	# subprocess.call("ls -l ./ ",shell=True)