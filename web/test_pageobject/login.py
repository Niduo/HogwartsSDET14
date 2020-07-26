from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Login:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan(self):
        pass

    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link')
