from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        pass

    def register(self):
        """
        输入注册用户
        点击注册
        :return:
        """
        self.driver.find_element(By.ID, 'corp_name').send_keys("nana")
        self.driver.find_element(By.ID, 'manager_name').send_keys("kobi")
        self.driver.find_element(By.ID, "register_tel").send_keys(19900001111)
