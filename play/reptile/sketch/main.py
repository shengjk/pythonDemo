#!/usr/bin/env python
#-*- coding: utf-8 -*-
#coding=utf-8
#Create by shengjk1 on  2017/6/7

import os
from Tix import Tk, Label, W, E, Entry, Button

from image import mains
from tkinter import *

def exists_mkdir():
    if os.path.exists('disdir') and os.path.exists('srcdir'):
        pass
    else:
        os.mkdir('disdir')
        os.mkdir('srcdir')

def images():
    try:
        s1 = e1.get()
        a = mains(s1)
        c["text"] = "我们的程序运行成功了"
    except Exception:
        c["text"] = "程序运行出错了,可能是缺少了两个配置文件"

#创建程序运行需要的工作目录
exists_mkdir()

tk = Tk()
# 设置窗口大小和位置
tk.geometry('430x350+80+60')

# 不允许改变窗口大小
tk.resizable(False, False)

## 用来显示Label组件
tk.title('素描图生成器')
w1 = Label(tk,text='作者博客：www.liuchaoblog.live')
w = Label(tk,text='')
w2 = Label(tk,text='欢迎使用：')
w3 = Label(tk,text='步骤一：将需要转化的图片放入  srcdir  文件夹下')
w4 = Label(tk,text='步骤二：输入 0-100的数值，数值越大，颜色越深。--------标准参数是 10 ')
w5 = Label(tk,text='步骤三：点击确认 运行程序  等待出现提示')
w6 = Label(tk,text='步骤四：到输入----图片  文件夹找到素描图')
w1.grid(row=0,column=0,sticky=W)
w.grid(row=1,column=0,sticky=W)
w2.grid(row=2,column=0,sticky=W)
w3.grid(row=3,column=0,sticky=W)
w4.grid(row=4,column=0,sticky=W)
w5.grid(row=5,column=0,sticky=W)
w6.grid(row=6,column=0,sticky=W)


l = Label(tk,text="输入 0-100的数值")
l.grid(row=8,column=0,sticky=E)

## 用来显示输入框
e1 = Entry(tk)
e1.grid(row=10,column=0,sticky=E)

## 用来显示Button
b = Button(tk,text='确定',command=images)
b.grid(row=12,column=0,sticky=E)

c = Label(tk,text="",background="yellow")
c.grid(row = 15)

# 启动消息主循环
tk.mainloop()