from appium.webdriver.common.mobileby import MobileBy

from app.page.addMember import AddMember
from app.page.basePage import BasePage
from app.page.searchMember import SearchMember


class Contact(BasePage):

    def goto_add_member(self):
        # 列表过长需滚动点击 添加成员
        self.find_by_scroll("添加成员")
        return AddMember(self.driver)

    def goto_search_member(self):
        return SearchMember()
