from selenium import webdriver
from selenium.webdriver.common.by import By

from test_pageobject.login import Login
from test_pageobject.register import Register


class Index:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self.driver)

    def login(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self.driver)
