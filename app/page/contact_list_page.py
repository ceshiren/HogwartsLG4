#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 通讯录页面
# from app.page.member_invite_page import MemberInviteMenuPage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from app.page.base_page import BasePage


class ContactListPage(BasePage):
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver

    def add_member(self):
        '''
        添加成员
        '''
        # 点击【添加成员】
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()
        self.find_by_scroll("添加成员").click()
        from app.page.member_invite_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)
