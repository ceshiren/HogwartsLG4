import re
from time import sleep

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


def load_data(path):
    with open(path, encoding='utf-8') as f:
        return yaml.load(f)


class TestDemo:
    #测试数据的数据驱动
    # @pytest.mark.parametrize('path', ['test_data.yaml', 'test_data.yaml'])
    #todo: pytest hook机制
    @pytest.mark.parametrize('data', load_data("test_data.yaml")['data'])
    def test_search(self, data):
        #测试步骤的数据驱动
        for step in load_data("test_data.yaml")['steps']:
            print(step)
            if 'webdriver' in step:
                browser = str(step.get("webdriver").get("browser", "chrome")).lower()
                if browser == 'chrome':
                    driver = webdriver.Chrome()
                elif browser == 'firefox':
                    driver = webdriver.Firefox()
                else:
                    print(f"{driver} don't know which browser")

            if 'get' in step:
                url = step.get('get')
                driver.get(url)

            if 'find_element' in step:
                by = step.get("find_element")[0]
                locator = step.get("find_element")[1]
                current_element = driver.find_element(by, locator)

            if 'click' in step:
                current_element.click()

            if 'send_keys' in step:
                value = str(step.get("send_keys"))
                # 判断value是否是变量 ${data}
                value=value.replace('${data}', data)
                current_element.send_keys(value)

        # driver=webdriver.Chrome()
        # driver.get('https://ceshiren.com/')
        # driver.find_element(By.ID, 'search-button').click()
        # driver.find_element(By.ID, 'search-term').send_keys(keyword)
