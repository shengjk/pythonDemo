#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#coding=utf-8
#Create by shengjk1 on  2017/1/9

'''
python的数字类型比java强大，这也是它在做分析方面强于java的地方
python类型完整的工具:
整数、浮点数、复数、固定精度的十进制、有理分数(分数)、集合、布尔类型、无穷的整数精度
各种数字内置函数和模块
'''

if __name__ == '__main__':
    print("a")
    '''
    is判断的是内存地址。
    java中==比较的是内存地址，适用于基本数据类型，而equal比较的内容
    混合类型自动升级，跟java一样。python  整数->浮点数->复数

    关于除法：
    / 、//不一样的

    python支持连续判断 x<y<x =>x<y and y<x 而java不支持

    可以处理任意大小的整数

    print(r'\\\t\\')是不转义的

    '''
    #数字的字符串格式化，结果都是字符串
    a=7/3
    print(a)
    print('%e ' % a)
    print('%4.2f' % a)
    print("{0:4.2f}".format(a) )
    print(repr(7/3))
    print(str(7/3))