#!/usr/bin/env python
# -*- coding: utf-8 -*-
from web.podemo1.page.index_page import IndexPage


class TestContact:
    def setup(self):
        self.index = IndexPage()

    def test_addcontact(self):
        name = "aa_0"
        account = "aa_0_hogwarts"
        phonenum = "13911111111"

        addmemberpage = self.index.click_add_member()
        addmemberpage.add_member(name, account, phonenum)
        result = addmemberpage.get_member(name)
        assert result
