# -*- coding: utf-8 -*-
# Time : 2022/5/9 10:14
# Author : pxz
# File : test_page1.py
# Desc :
import unittest
from log.log import logger

class UserCases(unittest.TestCase):
    a=1
    # testfixture
    @classmethod
    def setUpClass(cls):
        print('打开浏览器')

    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')
    @unittest.skipIf(a==1,'a跳过')
    def test_1(self):
        print('用户的第一个测试用例')


    def test_2(self):
        sum=2+1
        logger.info('测试成功')

if __name__ == '__main__':
        unittest.main()
