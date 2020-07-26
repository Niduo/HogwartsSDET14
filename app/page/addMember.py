from appium.webdriver.common.mobileby import MobileBy

from app.page.basePage import BasePage
from app.page.manualAddMember import ManualAddMember


class AddMember(BasePage):
    manual_add_ele = (MobileBy.XPATH, '//*[@text="手动输入添加"]')

    def goto_manual_add_member(self):
        self.find_click(self.manual_add_ele)
        return ManualAddMember(self.driver)
