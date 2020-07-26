"""
debug 模式启动浏览器测试，方便调试不会每次启动浏览器
mac操作命令， 先关闭浏览器退出进程
sudo /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

# sudo /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --test-type --ignore-certificate-error --remote-debugging-port=9222
"""


import shelve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWeb:
    def setup_method(self, method):
        op = Options()
        # 将开启debugger模式， 每次调用
        op.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=op)

    def test_start(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys("hot")
        self.driver.find_element(By.ID, "su").click()

    def test_cookie_login(self):
        # 先登录ceshiren
        self.driver.get("https://www.ceshiren.com")
        print("cookie 测试")
        cookies = self.driver.get_cookies()
        print(type(cookies), print("cookies::::", cookies))

        # shelve用法.open创建一个数据库，将列表的值或取到后， 加到db['key']里即可。db会保存此数据。之后可将复制到
        db = shelve.open("cookies")
        # cookies = [{'domain': 'ceshiren.com', 'httpOnly': True, 'name': '_forum_session', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'm1DU2dsSXl1NEZUL202NmRrcTR3Tnk4KzZ5Y1F6NmhMY3VNc25JZVZIZUNSeVBrNEZsR2k4U0t0SjJ2UWlDejhpcWlRUDB0STRjdkEzeHJlZ3ZkcVRzQkQxa2FzblFUVGtTSVgya2MrWmcwbzJhTkpWSlhqSDNiR2JWQXV2cFhOUHBJeFhZaHlFbzd0WFNsbUVrcWZqc3UvN2xlZ1JoeU54dVZxbWlIZENIS3FMSUZwb3BZaXF1ZVNkSW5CTGYrOEhFQUt4ZnZOa0w5MVlGb3UrSEZRQVJZV21MK2dYd1lqOHFpSHYrTDZQcDZxMUg5V0VDUkFvenB3SjFKVnIxV3owdm1sYVdHMldGa1RtUUVXejlwNkE9PS0teG8waUF5YjhINlVncU4xRGZ0M1VTQT09--fded2cfcbcc4f12264b3a42fea764ce3047ad4b0'}, {'domain': 'ceshiren.com', 'expiry': 1600269837, 'httpOnly': True, 'name': '_t', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '8cefe38a90651bd5121cbaca549286d5'}]
        # db['cookies'] = cookies
        cookies = db['cookies']
        for cookie in cookies:
            if "expiry" in cookie.key():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://ceshiren.com/t/topic/3496")
