#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTestcase():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testcase(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()
        element = self.driver.find_element(By.LINK_TEXT, "所有分类")
        result = element.get_attribute("class")
        assert 'active' == result

    def test_wx(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(10)
