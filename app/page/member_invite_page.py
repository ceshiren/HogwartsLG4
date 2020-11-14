#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from app.page.contact_add_page import ContactAddPage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from app.page.base_page import BasePage


class MemberInviteMenuPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def add_member_manul(self):
        # 点击【手动输入添加】
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        from app.page.contact_add_page import ContactAddPage
        return ContactAddPage(self.driver)

    def verify_toast(self):
        # result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        result = self.get_toast_text()
        return result
