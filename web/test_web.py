from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWeb:
    def setup_method(self):
        #
        chrome_option = Options()
        # 将开启debugger模式， 每次调用
        chrome_option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_option)

    def test_start(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys("hot")
        self.driver.find_element(By.ID, "su").click()

    def test_cookie(self):
        self.driver.get()
