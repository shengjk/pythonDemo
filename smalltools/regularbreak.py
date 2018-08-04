#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create by shengjk1 on  2018/4/12
# -*- coding: utf-8 -*-
import threading
import time
import sys

# # 判断python的版本然后import对应的模块
# if sys.version < '3':
# 	from Tkinter import *
# else:
from tkinter import *

import math

mydelaymin = 60  # 窗口提示的延迟时间，以分钟计


# 学完java的多线程后在来完善它

# ------------------def-------------------
def showMessage():
    # show reminder message window
    root = Tk()  # 建立根窗口
    # root.minsize(500, 200)   #定义窗口的大小
    # root.maxsize(1000, 400)  #不过定义窗口这个功能我没有使用
    root.withdraw()  # hide window
    # 获取屏幕的宽度和高度，并且在高度上考虑到底部的任务栏，为了是弹出的窗口在屏幕中间
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight() - 100
    root.resizable(False, False)
    # 添加组件
    root.title("工作已经很努力了，吃块狗屁丹药，休息会吧！")
    frame = Frame(root, relief=RIDGE, borderwidth=3)
    frame.pack(fill=BOTH, expand=1)  # pack() 放置组件若没有则组件不会显示
    # 窗口显示的文字、并设置字体、字号
    label = Label(
        frame,
        text="You have been working 60 minutes! Please have a break!!",
        font="Monotype\ Corsiva -20 bold")
    label.pack(fill=BOTH, expand=1)
    # 按钮的设置
    button = Button(
        frame,
        text="OK",
        font="Cooper -25 bold",
        fg="red",
        command=root.destroy)
    button.pack(side=BOTTOM)

    root.update_idletasks()
    root.deiconify()  # now the window size was calculated
    root.withdraw()  # hide the window again 防止窗口出现被拖动的感觉 具体原理未知？
    root.geometry(
        '%sx%s+%s+%s' %
        (math.ceil(
            root.winfo_width()) +
            10,
            math.ceil(
            root.winfo_height()) +
            10,
            math.ceil(
            (screenwidth -
             root.winfo_width()) /
            2),
            math.ceil(
            (screenheight -
             root.winfo_height()) /
            2)))
    # root.geometry("425x72+100+100.0")
    root.wm_attributes('-topmost', 1)
    root.deiconify()
    root.mainloop()
    # 点击ok按钮后，开始进入休息时间
    print("休息3min")
    time.sleep(3 * 60)
    print("休息结束，开始工作")


# showMessage()
def count():
    countTime1 = mydelaymin
    while (countTime1 > 0):
        countTime1 = countTime1 - 1
        print(countTime1)
        time.sleep(1 * 60)


while True:
    print("===================================")
    threading.Thread(target=count).start()

    time.sleep(mydelaymin * 60)  # 参数为秒
    showMessage()
