# -*- coding: utf-8 -*-
# Time : 2022/5/9 15:15
# Author : pxz
# File : runner.py
# Desc :

import unittest
from BeautifulReport import BeautifulReport
from config.config import case_path,report_path

suite=unittest.defaultTestLoader.discover(start_dir=case_path,pattern='test_page2.py')
result=BeautifulReport(suite)
result.report(description='系统登录的测试报告',filename='SIT测试报告',report_dir=report_path)