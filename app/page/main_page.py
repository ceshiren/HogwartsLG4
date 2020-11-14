#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 主页
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from app.page.base_page import BasePage
from app.page.contact_list_page import ContactListPage


class MainPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver
    # 首页-通讯录
    _contact_list = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contactlist(self):
        '''
        进入到通讯录
        '''
        # 点击【通讯录】

        self.find(*self._contact_list).click()
        return ContactListPage(self.driver)
