import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestW():
    def setup_method(self, method):
        chrome_options = Options()
        # 和浏览器打开的调试端口进行通信
        # 浏览器要使用 --remote-debugging-port=9222 开启调试
        chrome_options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(5)

    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        time.sleep(3)
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, "kw").send_keys("大大咧咧")
        self.driver.get("https://www.163.com")
        time.sleep(3)
