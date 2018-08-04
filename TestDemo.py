#!/usr/bin/env python
'''
-*- coding: utf-8 -*-  
coding=utf-8
AUTHOR: shengjk1
CREATED: 2016/12/12
'''

import math
import random

if __name__ == '__main__':
    print("a")
    str = "02-42-AC-11-00-09|1481267157778|1|1|scld01|四川蓝带|null|null|null|null|2016-12-09 15:05:57|null|null|0|android|08f9022b02844c9db99223341a65c74d|27.195.0.0|0|1|null|1|1|1|null"
    print(str.split("|"))
    print(len(str.split("|")))
    # 数字类的操作跟java差不多
    print(random.randint(1, 12))
    '''
    也有垃圾回收
    python数据类型：
    数字、字符串、列表、字典、元组、文件、集合等


    序列包括 列表和元组、字符串,python它把字符串看做单个字符的序列
    与java相似的地方是从0开始的

     作为序列，字符串也支持+来进行拼接，只能是类型相同的才能+拼接

    python中字符串不可变这个java一致

    在python中每一个对象都可以分为不可变性或者可变性。在核心类型中，数字、字符串、元组是不可变的
    列表、字典确实自由改变的
    '''

    '''
    列表通用算法
    len/s[0]/+/s[:]
    '''
    s = "spam"
    print(len(s))
    print(s[0])
    print(s[1])
    print(s[2])
    print(s[0:2])  # [0,2)前包后不包的
    print(s[1:])
    print(s[:3])
    print(s[:])
    print(s + "qqq")
    print((s + "qqq") * 8)

    # 字符串特有方法 与java还是比较相似的
    print(s)
    print(s.find("pa"))
    print(s.replace("pa", "wx"))
    print(s.isalpha())
    print(s.isalnum())
    print(s.strip())

    # 寻求帮助
    print(dir(s))
    print(help(s.strip))

    print(len("A\nB\nC"))
    print(ord("a"))  # 转化为ASCII编码
    print("'''''\0")
    print("'\0")
    print("\'\0")

    # 字符串的模式匹配
    import re

    match = re.match("Hello[\t]*(.*)world", "Hello   python nihao world")
    print(match.group(0))
    print(match.group(1))
    print(match.groups())

    # 列表  相当于java中list，但没有类型的约束，没有固定大小
    L = [123, 'spam', 12.01]
    print(len(L))
    print(L[1])
    print(L[:])
    print("======================== ")
    L = L + [1, 2, 3]

    # 列表特有操作
    L.append("a")
    print(L)
    L.pop(2)  # 与redis中函数相似
    print(L)
    L.insert(2, '2')
    print(L.index('2'))
    print(L)
    print(L.remove(1))
    print(L.reverse())
    print(L)
    # 支持任意的嵌套
    M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(M)
    print([row[1] for row in M])
    print([row[1] + 1 for row in M])
    print([row[1] + 1 for row in M if row[1] % 2 == 0])  # 相当于java8中filter算子
    print([M[i][i] for i in [0, 1, 2]])  # 这涉及到矩阵操作
    print([c * 2 for c in 'spam'])

    # 字典 相当于java中map
    d = {"food": "spam", "quamtity": 4, "color": "pink"}
    print(d["food"])
    d["quamtity"] += 1
    print(d)

    d = {}  # 相当于java中的add方法
    d["name"] = "bob"
    d["age"] = 32
    d["job"] = "it"
    print(d)

    # 也支持重复嵌套 跟java一样。有点像redis zset


    print(list(d.keys()))
    ks=list(d.keys())
    ks.sort()
    print("====================== ")
    print(list(ks))
    for key in ks:
        print(key,"=>",d[key])

    print("================")

    for w in "spam":
        print(w.upper())

    if not "f" in d:
        print("missing")

    print(d.get("x",0))
    print(d["x"] if "x" in d else 0)

    #元组  不可变:分两部分 1是值不可变  2是长度不可变
    t=(1,2,3,4,5,'a')
    print(len(t))
    t=t+(6,7)
    print("================= ")
    print(t[0])
    print("================= ")
    print(t)
    print(t[:])
    print(t.count(4))
    print(t.index(4))



class worker:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self,percent):
        self.pay*=(1.0+percent)