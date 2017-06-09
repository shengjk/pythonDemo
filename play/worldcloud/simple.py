#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Minimal Example
===============

Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path

import jieba
from wordcloud import WordCloud

# d = path.dirname(__file__)
d = path.dirname('D:\\tmp\\')
# Read the whole text.
text = open(path.join(d, '1111.txt')).read()

# Generate a word cloud image
# wordcloud = WordCloud().generate(text)
# print type(wordcloud)
# Display the generated image:
# the matplotlib way:

import matplotlib.pyplot as plt

# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")

# lower max_font_size
# generate 可以对全部文本进行自动分词,但是他对中文支持不好
wordcloud = WordCloud(background_color='white', width=10000, height=6000, margin=2, max_font_size=30).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
wordcloud.to_file('test.png')


