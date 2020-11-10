#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# appium-python-client 客户端安装包
from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "hogwarts"
caps["appPackage"] = "com.tencent.wework"
caps["appActivity"] = ".launch.LaunchSplashActivity"
caps["noReset"] = "True"
# 最重要的代码，建立客户端与服务端的连接
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.TextView")
el1.click()
el2 = driver.find_element_by_id("com.tencent.wework:id/gq_")
el2.click()
el3 = driver.find_element_by_id("com.tencent.wework:id/ffq")
el3.send_keys("霍格沃兹测试1")

driver.quit()
