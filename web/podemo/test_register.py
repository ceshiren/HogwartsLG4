#!/usr/bin/env python
# -*- coding: utf-8 -*-
from web.podemo.main_page import MainPage


class TestRegister:
    def setup(self):
        self.main = MainPage()

    def test_regist(self):
        # result = self.main.goto_login().goto_register().register()
        result = self.main.goto_register().register()
        assert result
