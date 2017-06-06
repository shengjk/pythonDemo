#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
# Create by shengjk1 on  2017/5/17 0017
import numpy as np
from collections import defaultdict


valid_rules=defaultdict(int)
invalid_rules=defaultdict(int)
num_occurances=defaultdict(int)

dataset_filename = "affinity_dataset.txt"
x = np.loadtxt(dataset_filename)
print(x[5])
n_samples, n_features = x.shape
print(x.shape)
print(n_features)

num_apple_purchases=0
for sample in x:
	if sample[3]==1:
		num_apple_purchases+=1
print("{0} people bought Apples".format(num_apple_purchases))

rule_valid=0
rule_invalid=0
for sample in x:
	if sample[3]==1:
		if sample[4]==1:
			rule_valid+=1
		else:
			rule_invalid+=1
print("{0} cases of the rule being valid were discovered".format(rule_valid))
print("{0} cases of the rule being invalid were discovered".format(rule_invalid))


suport=rule_valid
confidence=rule_valid/num_apple_purchases
print("the support is {0} and the confidence is {1:.3f}.".format(rule_valid,confidence))
print("As a percentage,that is {0:.1f}%.".format(100*confidence))

#  面包、牛奶、奶酪、苹果、香蕉
from collections import defaultdict
valid_rules=defaultdict(int)
invalid_rules=defaultdict(int)
num_occurances=defaultdict(int)
n_samples, n_features = x.shape
for sample in x:
	for premise in range(4):
		if sample[premise]==0:continue
		num_occurances[premise]+=1;
		for conclusion in range(n_features):
			if premise==conclusion:continue
			if sample[conclusion]==1:
				valid_rules[(premise,conclusion)]+=1
			else:
				invalid_rules[(premise,conclusion)]+=1
suport=valid_rules
