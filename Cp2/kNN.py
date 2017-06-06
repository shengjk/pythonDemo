#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
# Create by shengjk1 on  2017/5/17 0017
import numpy
from numpy import *
import operator


def createDataSet():
	group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
	labels = ['A', 'A', 'B', 'B']
	return group, labels


def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances ** 0.5

	print distances
	sortedDisIndicies = distances.argsort()  # 返回索引[2, 3, 1, 0]

	print sortedDisIndicies
	classCount = {}  # 字典
	for i in range(k):
		voteIlabel = labels[sortedDisIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.iteritems(),
	                          key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]


# [] 列表
# 1,2 tuple
def file2matrix(filename):
	fr = open(filename)
	arrayOlines = fr.readlines()
	numberOfLines = len(arrayOlines)
	returnMat = zeros((numberOfLines, 3))
	classLabelVector = []
	index = 0
	for line in arrayOlines:
		line = line.strip()
		listFormLine = line.split('\t')
		returnMat[index, :] = listFormLine[0:3]
		classLabelVector.append(int(listFormLine[-1]))
		index += 1
	return returnMat, classLabelVector


def autoNorm(dataSet):
	minVals = dataSet.min(0)  # 列
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))

	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals, (m, 1))
	normDataSet = normDataSet / tile(ranges, (m, 1))
	return normDataSet, ranges, minVals


if __name__ == '__main__':
	datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
	print autoNorm(datingDataMat)
	print datingDataMat.min(0)
	print datingDataMat.shape

# import matplotlib.pyplot as plt
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(datingDataMat[:,1],datingDataMat[:,2],
#            15.0*array(datingLabels),15.0*array(datingLabels))
# plt.show()
