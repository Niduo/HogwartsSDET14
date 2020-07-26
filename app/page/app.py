from appium import webdriver
from selenium.webdriver.common.by import By

from app.page.basePage import BasePage
from app.page.mainPage import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {"platformName": "Android",
                    "platformVersion": "6.0",
                    "deviceName": "emulator-5554",
                    "appPackage": "com.tencent.wework",
                    "appActivity": ".launch.LaunchSplashActivity",
                    "skipDeviceInitialization": "true",
                    "skipDeviceInitialization": "true",
                    "noRest": "true"}

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            # launch_app() 这个方法不需要传入任何参数， 会自动启动起来DesireCapa里面定义的activity
            # start_activity(packagename, activityname) 可以启动其它的应用的页面
            self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self

    def stop(self):
        pass

    def restart(self):
        pass

    def goto_main(self):
        return MainPage(self.driver)
