# -*- coding: utf-8 -*-
# Time : 2022/5/9 10:32
# Author : pxz
# File : test_page2.py
# Desc :

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from objectpage.login_page import LoginPage
from config.config import url,driver_path
from data.data import ReadWrite

class LoginCases(unittest.TestCase):
    #testfixture
    @classmethod
    def setUpClass(cls):
        print('打开浏览器')
        e = Service(executable_path=driver_path)
        cls.driver = webdriver.Chrome(service=e)
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.loginpage=LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')
        cls.driver.quit()

    def test_1(self):
        '''
        验证有效地用户名和密码成功登录系统
        '''
        print('登录的第一个测试用例')
        user_list=ReadWrite().excelread('users')
        username=user_list[0][0]
        password=user_list[0][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        sleep(0.5)
        self.loginpage.click_logout()


    def test_2(self):
        '''
        验证密码为空时登录失败
        '''
        self.loginpage.input_username('shelly')
        self.loginpage.click_login()
        sleep(0.5)
        alert_login=self.driver.switch_to.alert
        alert_login.accept()

    # def testlogin(self):
    #     print('第一个用例')
    #     usename1=usename
    #     password1=password
    #     self.driver.find_element(By.ID, 'account').send_keys(usename1)
    #     self.driver.find_element(By.NAME, 'password').send_keys(password1)
    #     self.driver.find_element(By.ID, 'submit').click()
    #     sleep(0.5)
    #
    # def testlogot(self):
    #     print('第二个用例')
    #     self.driver.find_element(By.CLASS_NAME,'dropdown-toggle').click()
    #     self.driver.find_element(By.LINK_TEXT,'退出').click()
