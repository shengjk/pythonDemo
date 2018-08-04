#!/usr/bin/env python
'''
-*- coding: utf-8 -*-  
coding=utf-8
AUTHOR: shengjk1
CREATED: 2016/12/12
'''

def ask_ok(prompt,retries=4,complaint='Yes or No,please!'):
    while True:
        ok=raw_input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return True
        if retries<0:
            raise IOError('refusenik user')
        print complaint