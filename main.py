from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

import unittest, os
import selenium.webdriver

execfile("Page\LoginPage.py")
execfile("Page\Logon.py")
execfile("Page\HomePage.py")
execfile("CreateReadCookie.py")


class Test (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.base_url = "http://courses.way2automation.com"
        self.driver.get(self.base_url)
        self.wait = WebDriverWait(self.driver, 10)

    def test_authorize(self):
        logon = ClickLogon(self.driver)
        login_page = LoginPage(self.driver)
        cookie = CreateReadCookie(self.driver)
        home_page = HomePage(self.driver)
        if os.path.isfile("cookies.pkl"):
            cookie.read_cookie()
            self.driver.refresh()
        else:
            logon.logon_click()
            login_page.login_in_form()
            cookie.create_cookie()
        assert home_page.home_page().is_displayed()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

