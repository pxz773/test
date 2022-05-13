# -*- coding: utf-8 -*-
# Time : 2022/5/12 15:13
# Author : pxz
# File : log.txt.py
# Desc :

import logging

logger=logging.getLogger()
logger.setLevel(logging.INFO)  #IFNO 定义级别，普通信息
format=logging.Formatter('%(asctime)s%(filename)s%(levelname)s[line:%(lineno)d]%(message)s')
fh=logging.FileHandler(r'D:\pycharm\py\test\log\log.txt',mode='a',encoding='utf-8')
# %(created)f:时间
# %(name):logger的名字
# %(levelno)s: DEBUG 10 INFO 20 WARNING 30 ERROR 40 CRITICAL 50
# %(levelname):文本形式日志级别
# %(module)s:调用日志输出的模块名
# %(asctime)s:调用日志输出的模块名
# %(message)s:用户输入的信息
# %[line:%(lineno)d] :显示代码所在的行
fh.setLevel(logging.INFO)
fh.setFormatter(format)

logger.addHandler(fh)
