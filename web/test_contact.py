#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWX:
    def setup(self):
        option = Options()
        # 注意 9222 端口要与命令行启动的端口保持一致 --remote-debugging-port=9222
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_case1(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.ID, "menu_contacts").click()

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'IiwmHmbRQC3UgqmekvGcshQ1v-qTHqscpEcIGoEoWMPWTnpajTBMthrkG8YWHWrD'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a482021'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'ymOxrnOIIGPUw_czEaE-QnCFyfOVoKxA_SXYFOI3OiccWDJ6kWpfWEWTuJpEv0iLHX0sIpIoSHhypsWsKvj5a3FOrel_Uf2rZPARpf7Fs2bQVDVzCAVC0JsqjECKBswOuGqa-MOtv5r47uBnzbi4b7imz8EC1BPb95zBC_msN_Di1tZtBxbdwHWflLlsgs8OHEDq_27P5CkU3bpSwsnUYrAn99cZtDAzI-jE6pP0MYNXWLQjPS3G-wsa6Q3BZ4aMl7C_vPdlSHjDsWmNJLY41w'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851905935585'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851905935585'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325054155915'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635943464, 'httpOnly': False,
                                            'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/',
                                            'secure': False, 'value': '1603101806,1603188257,1603189751,1604407464'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147385600.00002121, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '8205526055'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1919734977, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': 'e13a8a6ceba47c11'},
            {'domain': '.qq.com', 'expiry': 1604461481, 'httpOnly': False, 'name': 'uid', 'path': '/', 'secure': False,
             'value': '320489555'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1604407464'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '2977784949737350'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604433473, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '3p26ept'},
            {'domain': '.qq.com', 'expiry': 1604495231, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.912831238.1604312317'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607000882, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'en'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '75461a3126cbb39ff08f9bd58fe42c2d3b5c887a4e78ca4031e34ead02c3c44c'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635937937, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1667480831, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1737553657.1582007476'}]
        print(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def test_import_contacts(self):
        # shelve 模块， python 自带的对象持久化存储
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()
        # 打开无痕新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 加入cookie
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        # 刷新当前页面，获取登录状态
        self.driver.refresh()
        # 点击【导入联系人】
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 上传文件，选择文件的完整路径上传
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            "/Users/juanxu/Downloads/mydata.xlsx")
        # 断言上传文件名，与实际文件名一致
        result = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "mydata.xlsx" == result
        sleep(5)
