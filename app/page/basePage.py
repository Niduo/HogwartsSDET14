from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from appium.webdriver.webdriver import WebDriver
import logging


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locate):
        logging.info(f'Find {locate}')
        return self.driver.find_element(*locate)

    def find_click(self, locate):
        logging.info(f'Find_click {locate}')
        self.find(locate).click()

    def find_by_scroll(self, text):
        logging.info(f'Find_by_scroll {text}')
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));')
