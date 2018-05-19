#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#Create by shengjk1 on  2018/5/14

def mean(num_list):
    return sum(num_list)/len(num_list)

def add_five(num_list):
    return [n+5 for  n in num_list]

def main():
    n_list=[34,44,23,46,12,24]
    correct_mean=30.5
    assert (mean(n_list))