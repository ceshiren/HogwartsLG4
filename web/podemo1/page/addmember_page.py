#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.podemo1.page.base_page import BasePage


class AddMemberPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def add_member(self, name, account, phonenum):
        # name = "aa_0"
        # account = "aa_0_hogwarts"
        # phonenum = "13911111111"
        # sleep(2)
        # input name
        self.find(By.ID, "username").send_keys(name)
        # input account
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        # input phonenum
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        # click save
        # 如果页面上相同属性的元素有多个， 那么 通过 find_element 定位到的元素是第一次出现的元素
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()

        return True

    def get_member(self, value):
        locator = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(locator)
        # sleep(2)
        # find_elements方法返回的是元素列表 [element1,elemnt2,.....]
        titles_total = []
        while True:
            elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            titles = [element.get_attribute("title") for element in elements]
            if value in titles:
                return True
            titles_total.extend(titles)

            page: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = page.split("/", 1)

            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()

        return titles_total
