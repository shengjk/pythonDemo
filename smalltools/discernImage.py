#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#Create by shengjk1 on  2018/4/24

from PIL import Image
import pytesseract
#上面都是导包，只需要下面这一行就能实现图片文字识别
text=pytesseract.image_to_string(Image.open('/Users/iss/sourceCode/pyProject/pythonDemo/smalltools/11111.png'),lang='chi_sim')
# text=pytesseract.image_to_string(Image.open('/Users/iss/sourceCode/pyProject/pythonDemo/smalltools/1111111.png'))
print(text)

