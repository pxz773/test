# -*- coding: utf-8 -*-
# Time : 2022/5/9 15:02
# Author : pxz
# File : config.py
# Desc :

import os

root_path=os.path.dirname(os.path.dirname(__file__))
print(root_path)

url='http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html'
driver_path=root_path+r'/driver/chromedriver.exe'
case_path=root_path+r'/test_cases'
report_path=root_path+r'/report'
file_path=root_path+r'/data/test.xlsx'

