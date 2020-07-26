from appium.webdriver.common.mobileby import MobileBy

from app.page.basePage import BasePage
from app.page.contact import Contact


class MainPage(BasePage):
    contact_ele = (MobileBy.XPATH, '//*[@text="通讯录"]')

    def goto_message(self):
        pass

    def goto_contact(self):
        self.find_click(self.contact_ele)
        return Contact(self.driver)

    def goto_work_platform(self):
        pass

    def goto_me(self):
        pass
