from selenium import webdriver

import pickle
import selenium.webdriver


class CreateReadCookie:
    def __init__(self, driver):
        self.driver = driver

    def create_cookie(self):
        all_cookies = self.driver.get_cookies()
        with open("cookies.pkl", "wb") as create:
            pickle.dump(all_cookies, create)

    def read_cookie(self):
        with open("cookies.pkl", "rb") as read:
            cookies = pickle.load(read)
        for cookie in cookies:
            self.driver.add_cookie(cookie)

