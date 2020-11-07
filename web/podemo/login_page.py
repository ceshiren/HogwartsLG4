#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan(self):
        pass

    def goto_register(self):
        # click register
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        # enter register page
        return RegisterPage(self.driver)
