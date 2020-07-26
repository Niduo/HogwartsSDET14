from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestApp:
    def setup_class(self):
        caps = {"platformName": "Android",
                "platformVersion": "6.0",
                "browserName": "Browser",
                "noRest": True,
                "deviceName": "emulator-5554",
                "automationName": 'UIAutomator2'
                # "chromedriverExecutable": "/usr/local/bin/chromedriver"
                }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def setup(self):
        self.driver.get("http://m.baidu.com")
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable)

    def test_1(self):
        self.driver.find_element(By.ID, "su").click()
