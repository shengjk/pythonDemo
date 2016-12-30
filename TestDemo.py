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
    str="02-42-AC-11-00-09|1481267157778|1|1|scld01|四川蓝带|null|null|null|null|2016-12-09 15:05:57|null|null|0|android|08f9022b02844c9db99223341a65c74d|27.195.0.0|0|1|null|1|1|1|null"
    print(str.split("|"))
    print(len(str.split("|")))
#数字类的操作跟java差不多
    print(random.randint(1,12))
    '''
    序列包括 列表和元组、字符串,python它把字符串看做单个字符的序列
    与java相似的地方是从0开始的

     作为序列，字符串也支持+来进行拼接，只能是类型相同的才能+拼接

    python中字符串不可变这个java一直
    '''
    s="spam"
    print(len(s))
    print(s[0])
    print(s[1])
    print(s[2])
    print(s[0:2])#[0,2)前包后不包的
    print(s[1:])
    print(s[:3])
    print(s[:])
    print(s+"qqq")
    print((s+"qqq") *8)


