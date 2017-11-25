#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create by shengjk1 on  2017/10/30
import logging
import sys

import time

import os

reload(sys)
sys.setdefaultencoding('utf-8')



def get_logger(domain, start_time = time.strftime('%Y%m%d', time.localtime())):
	start_time = start_time[:12]
	path = '/Users/iss/scrapy_spider_logs/'
	if not os.path.exists(path):
		os.makedirs(path)
	path_log = path +domain+"_"+ start_time

	my_logger = logging.getLogger(domain)
	my_logger.setLevel(logging.INFO)
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s[line:%(lineno)d] %(message)s')


	console_info = logging.StreamHandler()
	console_info.setLevel(logging.INFO)
	console_info.setFormatter(formatter)
	my_logger.addHandler(console_info)


	scrapy_logger = logging.getLogger('scrapy')
	#scrapy_logger = logging.getLogger()
	scrapy_logger.setLevel(logging.WARNING)

	handler_info = logging.FileHandler('%s_info.log' % path_log, 'a', encoding='UTF-8')
	handler_info.setLevel(logging.INFO)
	handler_info.setFormatter(formatter)
	my_logger.addHandler(handler_info)
	scrapy_logger.addHandler(handler_info)

	handler_warning = logging.FileHandler('%s_warning.log' % path_log, 'a', encoding='UTF-8')
	handler_warning.setLevel(logging.WARNING)
	handler_warning.setFormatter(formatter)
	my_logger.addHandler(handler_warning)
	scrapy_logger.addHandler(handler_warning)

	handler_error = logging.FileHandler('%s_error.log' % path_log, 'a', encoding='UTF-8')
	handler_error.setLevel(logging.ERROR)
	handler_error.setFormatter(formatter)
	my_logger.addHandler(handler_error)
	scrapy_logger.addHandler(handler_error)

	my_logger.info('Get my_logger success !!!')

	return my_logger

logger=get_logger('test')
if __name__ == '__main__':
    logger.info("test11111")